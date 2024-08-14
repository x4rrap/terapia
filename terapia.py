import os
import requests
from bs4 import BeautifulSoup

def google_search(query):
    url = "https://www.google.com/search?q=" + query
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find_all('div', {'class': 'ZINbbc'})

def main():
    print("OSINT Tool - Selezione un'opzione:")
    print("1. Numero di telefono")
    print("2. Indirizzo email")

    choice = input("Scegli un'opzione (1/2): ")

    if choice == "1":
        number = input("Inserisci il numero di telefono: ")
        prefixed_numbers = {
            "+39": ["393", "380", "348"],
            "03": ["039", "0369"]
            # aggiungi altri prefissi italiani qui
        }

        for prefix, codes in prefixed_numbers.items():
            if number.startswith(prefix):
                print(f"Numero di telefono: {number}")
                print("Esecuzione di OSINT...")
                query = f"{prefix}{number} +italia"
                results = google_search(query)
                for result in results:
                    print("-" * 20)
                    name = result.find('span', {'class': 'LC20lb'}).text
                    print(f"Nome: {name}")
                    # ... estrai altre informazioni come necessario

    elif choice == "2":
        email = input("Inserisci l'indirizzo email: ")
        prefixed_emails = {
            "@gmail.com": ["@hotmail.it", "@yahoo.it"],
            "@libero.it": ["@virgilio.it"]
            # aggiungi altri prefissi italiani qui
        }

        for prefix in prefixed_emails.keys():
            if email.endswith(prefix):
                print(f"Indirizzo email: {email}")
                print("Esecuzione di OSINT...")
                query = f"{email} +italia"
                results = google_search(query)
                for result in results:
                    print("-" * 20)
                    name = result.find('span', {'class': 'LC20lb'}).text
                    print(f"Nome: {name}")
                    # ... estrai altre informazioni come necessario

    else:
        print("Opzione non disponibile. Prova di nuovo.")

if __name__ == "__main__":
    main()
