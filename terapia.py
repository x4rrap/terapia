import requests
import re

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
    print("\n┌───────────────┐")
    print(f"│ {Figlet().render('HAGG4R')} │")
    print("└───────────────┘\n")
    print(f"\t{target}\t")
    print("\n┌───────────────┐")
    print("│ IP Address:   │")
    print(f"│ {ip_address}  │")
    print("└───────────────┘\n")

    print("\n┌───────────────┐")
    print("│ Email Addresses: │")
    print("└───────────────┘\n")
    for email in email_addresses:
        print(f"\t{email}\n")

    print("\n┌───────────────┐")
    print("│ Admin Details:  │")
    print("└───────────────┘\n")
    for detail in admin_details:
        print(f"\t{detail}\n")

# Prompt user for target
target = input("Enter the target's name: ")
get_info(target)
