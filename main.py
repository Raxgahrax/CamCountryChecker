import os
import socket
import random
import ssl
import locale
from urllib.parse import urlparse
import geoip2.database
from fake_useragent import UserAgent  # Importer la bibliothèque fake-useragent

# Définir la locale en français
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

def extract_ip_from_url(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc

def get_country_from_ip(ip):
    with geoip2.database.Reader('/var/lib/GeoIP/GeoLite2-Country.mmdb') as reader:
        try:
            response = reader.country(ip)
            return response.country.name
        except geoip2.errors.AddressNotFoundError:
            return None

def check_ip(url, port, user_agents):
    ip_address = extract_ip_from_url(url)
    user_agent_http = user_agents[0]
    user_agent_https = user_agents[1]

    try:
        with socket.create_connection((ip_address, port)) as sock:
            sock.send(f'GET /anony/mjpg.cgi HTTP/1.0\r\n\r\n'.encode('utf-8'))
            response = sock.recv(1024)

        return "HTTP/1.1 200 OK" in response.decode('utf-8')
    except (socket.error, ssl.SSLError):
        return False

def main(input_file, output_folder, sort_unique, sort_by_country):
    with open(input_file, 'r') as file:
        urls = [line.strip() for line in file if line.strip() and line.startswith("http")]

    if sort_unique:
        urls = list(set(urls))

    # Utilisation de fake-useragent pour générer les user agents aléatoires
    user_agents = UserAgent()
    print(user_agents)  # Afficher les user agents générés (optionnel)

    for url in urls:
        url = url.strip()
        country = get_country_from_ip(extract_ip_from_url(url))

        if country is not None:
            country_folder = os.path.join(output_folder, country)
            os.makedirs(country_folder, exist_ok=True)
            output_file_path = os.path.join(country_folder, 'online_urls.txt')

            # Sélectionner un user agent différent pour chaque URL
            user_agent_http = user_agents.random
            user_agent_https = user_agents.random

            with open(output_file_path, 'a') as output_file:
                if check_ip(url, 80, user_agent_http) or check_ip(url, 443, user_agent_https):
                    output_file.write(f"{url}\n")
                    print(f"L'URL {url} répond avec le code de statut HTTP 200:\nUser-Agent HTTP: {user_agent_http},\nUser-Agent HTTPS: {user_agent_https}.\n")
                else:
                    print(f"L'URL {url} ne répond pas ou le code de statut n'est pas 200:\nUser-Agent HTTP: {user_agent_http},\nUser-Agent HTTPS: {user_agent_https}.\n")



# Spécifiez le fichier d'entrée, le dossier de sortie, et les options de tri
input_file_path = '.../cameras_temp.txt'
output_folder_path = '.../output_countries'
sort_unique_addresses = True
sort_by_country = True

# Appeler la fonction principale sans le fichier des agents utilisateurs, user_agents_file_path n'est plus nécessaire
main(input_file_path, output_folder_path, sort_unique_addresses, sort_by_country)
