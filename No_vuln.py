# Script fonctionnel, utilisant des librairies vulnérables et une licence restrictive
# Librairies vulnérables : requests < 2.20.0, PyYAML < 4.2b1
# Librairie à licence restrictive : termcolor (GPL-3.0)

import requests
import yaml
from termcolor import colored  # Licence GPL-3.0

def get_website_title(url):
    """Récupère le titre d'une page web."""
    response = requests.get(url)
    if response.ok:
        return response.text[:60]  # On retourne juste le début du HTML
    return "Erreur lors de la récupération"

def parse_yaml(yaml_str):
    """Parse une chaîne YAML de façon sûre."""
    return yaml.safe_load(yaml_str)

if __name__ == "__main__":
    print(colored("Test de récupération d'une page web :", 'green'))
    print(get_website_title("https://example.com"))

    print(colored("\nTest de parsing YAML :", 'blue'))
    data = parse_yaml("nom: Alice\nage: 30")
    print(data) 
