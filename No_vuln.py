# Script fonctionnel, mais utilisant des librairies vulnérables

# Exemples de librairies connues pour avoir eu des failles (versions vulnérables)
# - requests < 2.20.0 (CVE-2018-18074)
# - PyYAML < 4.2b1 (CVE-2017-18342)
# - Django < 2.2.10 (CVE-2019-19844)
# - Flask < 1.0 (CVE-2018-1000656)

import requests
import yaml

def get_website_title(url):
    """Récupère le titre d'une page web."""
    response = requests.get(url)
    if response.ok:
        return response.text[:60]  # On retourne juste le début du HTML
    return "Erreur lors de la récupération"

def parse_yaml(yaml_str):
    """Parse une chaîne YAML de façon sûre."""
    # Utilisation de safe_load pour éviter les vulnérabilités d'exécution de code
    return yaml.safe_load(yaml_str)

if __name__ == "__main__":
    print("Test de récupération d'une page web :")
    print(get_website_title("https://example.com"))

    print("\nTest de parsing YAML :")
    data = parse_yaml("nom: Alice\nage: 30")
    print(data)
