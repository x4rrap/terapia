import requests
import re
from termcolor import colored

def get_info(target):
    # Fetch IP address
    ip_response = requests.get(f"https://api.hackertarget.com/geoip/?q={target}")
    ip_data = ip_response.json()
    ip_address = ip_data['IP']

    # Fetch email addresses
    email_response = requests.get(f"https://api.hackertarget.com/breachto/?q={target}")
    email_data = email_response.json()
    email_addresses = [match.group(1) for match in re.finditer(r'[\w\.-]+@[\w\.-]+', email_data['data'])]

    # Fetch admin details
    admin_response = requests.get(f"https://api.hackertarget.com/mxtool/?q={target}")
    admin_data = admin_response.json()
    admin_details = admin_data['data']

    # Display results in a formatted table
    print("\n" + colored("------------------------", "red") + "\n")
    print(colored("┌───────────────┐", "yellow") + "\n")
    print(colored(f"│ {Figlet().render('HAGG4R')} │", "green") + "\n")
    print(colored("└───────────────┘\n\t{target}\t", "cyan"))
    print(colored("------------------------\n┌───────────────┐", "red"))
    print(colored("│ IP Address:   │", "yellow"))
    print(colored(f"│ {ip_address}  │", "green") + "\n")
    print(colored("------------------------\n┌───────────────┐", "red"))
    print(colored("│ Email Addresses: │", "yellow"))
    for email in email_addresses:
        print(colored("\t{email}", "cyan") + "\n")
    print(colored("------------------------\n┌───────────────┐", "red"))
    print(colored("│ Admin Details:  │", "yellow"))
    for detail in admin_details:
        print(colored(f"\t{detail}", "cyan") + "\n")
    print(colored("------------------------", "red"))

# Prompt user for target
target = input("Enter the target's name: ")
get_info(target)
