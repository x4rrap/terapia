import os
import requests
from bs4 import BeautifulSoup

def google_search(query):
    url = "https://www.google.com/search?q=" + query
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find_all('div', {'class': 'ZINbbc'})

def extract_account_info(account):
    account_info = {}
    soup = BeautifulSoup(requests.get("https://twitter.com/" + account).text, 'html.parser')
    try:
        name = soup.find('span', {'class': 'b-0'}).text
        account_info['name'] = name
    except AttributeError:
        pass

    soup = BeautifulSoup(requests.get("https://www.facebook.com/" + account).text, 'html.parser')
    try:
        about = soup.find('div', {'class': '_6qdp7'}).find('p').text
        account_info['about'] = about
    except AttributeError:
        pass

    return account_info

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

                    account_links = [a['href'] for a in result.find_all('a')]
                    for link in account_links:
                        if "twitter.com/" in link:
                            twitter_account = link.split("/")[-1]
                            print("Twitter account:", twitter_account)
                            twitter_info = extract_account_info(twitter_account)
                            if 'name' in twitter_info:
                                print(f"Name: {twitter_info['name']}")
                            if 'about' in twitter_info:
                                print(f"About: {twitter_info['about']}")

                        elif "facebook.com/" in link:
                            facebook_account = link.split("/")[-1]
                            print("Facebook account:", facebook_account)
                            facebook_info = extract_account_info(facebook_account)
                            if 'name' in facebook_info:
                                print(f"Name: {facebook_info['name']}")
                            if 'about' in facebook_info:
                                print(f"About: {facebook_info['about']}")

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

                    account_links = [a['href'] for a in result.find_all('a')]
                    for link in account_links:
                        if "twitter.com/" in link:
                            twitter_account = link.split("/")[-1]
                            print("Twitter account:", twitter_account)
                            twitter_info = extract_account_info(twitter_account)
                            if 'name' in twitter_info:
                                print(f"Name: {twitter_info['name']}")
                            if 'about' in twitter_info:
                                print(f"About: {twitter_info['about']}")

                        elif "facebook.com/" in link:
                            facebook_account = link.split("/")[-1]
                            print("Facebook account:", facebook_account)
                            facebook_info = extract_account_info(facebook_account)
                            if 'name' in facebook_info:
                                print(f"Name: {facebook_info['name']}")
                            if 'about' in facebook_info:
                                print(f"About: {facebook_info['about']}")

    else:
        print("Opzione non disponibile. Prova di nuovo.")

if __name__ == "__main__":
    main()
