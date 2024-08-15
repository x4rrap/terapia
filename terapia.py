import os
import requests
from subprocess import Popen, PIPE

def whois_lookup(url):
    """Esegue il lookup Whois per l'URL specificato"""
    try:
        whois_data = Popen(["whois", url], stdout=PIPE).communicate()
        print(f"Whois informazioni per {url}:")
        sys.stdout.write(whois_data.decode().strip())
    except Exception as e:
        print(f"Errore nel recupero delle informazioni Whois: {e}")

def find_admin_page(url):
    """Cerca la pagina amministrativa dell'Site"""
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(f"{url}/wp-admin/", headers=headers)
    if response.status_code == 200:
        print("Pagina amministrativa trovata!")
        print(f"URL: {response.url}")
    else:
        print("Pagina amministrativa non trovata.")

def bypass_database(url):
    """Cerca la pagina di database bypassato"""
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(f"{url}/wp-login.php", headers=headers)
    if response.status_code == 200:
        print("Pagina di database bypassata trovata!")
        print(f"URL: {response.url}")
    else:
        print("Pagina di database bypassata non trovata.")

def sql_injection(url):
    """Esegue un'iniezione SQL per l'URL specificato"""
    try:
        sqlmap_output = Popen(["sqlmap", "-u", url, "--dbs"], stdout=PIPE).communicate()
        print("Risultati dell'iniezione SQL:")
        sys.stdout.write(sqlmap_output.decode().strip())
    except Exception as e:
        print(f"Errore nell'esecuzione dell'iniezione SQL: {e}")

def scan_website(url):
    """Esegue la scansione del sito web"""
    results_dir = "results"

    # Creare un directory di risultati
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    whois_lookup(url)
    find_admin_page(url)
    bypass_database(url)
    sql_injection(url)

def scan_vulnerabilities(url):
    """Esegue lo scanning delle vulnerabilità sul sito web"""
    # Usa nmap per eseguire lo scanning delle porte e delle servizi
    nmap_output = Popen(["nmap", "-sV", url], stdout=PIPE).communicate()
    print("Risultati dello scanning con Nmap:")
    sys.stdout.write(nmap_output.decode().strip())

def is_honeypot(url):
    """Controlla se il sito è un honeypot"""
    # Usa un altro indirizzo IP per evitare di essere rilevato come honeypot
    fake_ip = "8.8.8.8"  # Puoi utilizzare un altro indirizzo IP falso

    try:
        response = requests.get(url, headers={"X-Forwarded-For": fake_ip}, timeout=5)
        if response.status_code == 200:
            print("Il sito potrebbe essere un honeypot.")
            return True
        else:
            return False
    except Exception as e:
        print(f"Errore nella connessione: {e}")
        return False

def main():
    install_tools()
    url = input("Inserisci l'URL del sito da analizzare (es.: http://example.com, https://example.onion o http://example.gov): ")
    if is_honeypot(url):
        print("Il sito è probabilmente un honeypot. Utilizzo un altro indirizzo IP falso...")
        url = f"{url}?X-Forwarded-For={fake_ip}"
    scan_website(url)
    scan_vulnerabilities(url)

if __name__ == "__main__":
    main()
