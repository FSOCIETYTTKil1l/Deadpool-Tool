import os
import socket
import requests
from pystyle import Colorate, Colors, Center

menu = r"""   
  __________________________________   _________________________  .___ _______  ___________________   
 /   _____/\_   _____/\______   \   \ /   /\_   _____/\______   \ |   |\      \ \_   _____/\_____  \  
 \_____  \  |    __)_  |       _/\   Y   /  |    __)_  |       _/ |   |/   |   \ |    __)   /   |   \ 
 /        \ |        \ |    |   \ \     /   |        \ |    |   \ |   /    |    \|     \   /    |    \
/_______  //_______  / |____|_  /  \___/   /_______  / |____|_  / |___\____|__  /\___  /   \_______  /
        \/         \/         \/                   \/         \/              \/     \/            \/   
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(menu)))
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter("[0] Back to Main Menu\n")))

def get_ip(domain):
    domain = domain.replace("https://", "").replace("http://", "").split("/")[0]
    try:
        return socket.gethostbyname(domain)
    except:
        return None

def scan_ports(ip, ports=[21,22,23,25,53,80,110,143,443,465,587,993,995,3306,3389,8080]):
    open_ports = []
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.3)
            if s.connect_ex((ip, port)) == 0:
                open_ports.append(port)
            s.close()
        except:
            continue
    return open_ports

def server_info(domain_or_ip):
    ip = domain_or_ip
    if ip == "0":
        return False  
    if not ip.replace('.', '').isdigit():
        ip = get_ip(domain_or_ip)
        if not ip:
            print(Colorate.Horizontal(Colors.red, f"[-] Could IP for {domain_or_ip} not investigate."))
            input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter to return..."))
            return False

    clear_screen()
    print_banner()

    try:
        response = requests.get(f"https://ipapi.co/{ip}/json/", timeout=5)
        data = response.json()
        if "error" in data:
            print(Colorate.Horizontal(Colors.red, f"[-] Error: {data.get('reason', 'Invalid IP')}"))
            input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter to return..."))
            return False
    except:
        print(Colorate.Horizontal(Colors.red, "[-] Error retrieving IP data."))
        input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter to return..."))
        return False

    info_keys = [
        "ip", "hostname", "city", "region", "region_code", "country", "country_name",
        "continent_code", "in_eu", "postal", "latitude", "longitude", "timezone",
        "utc_offset", "org", "asn"
    ]

    print(Colorate.Horizontal(Colors.green_to_blue, f"\nServer/Domain information for '{domain_or_ip}':\n"))

    for key in info_keys:
        value = data.get(key)
        if value:
            print(Colorate.Horizontal(Colors.green_to_blue, f"{key.replace('_',' ').title()}: {value}"))

    print(Colorate.Horizontal(Colors.green_to_blue, "\nScanning common ports..."))
    open_ports = scan_ports(ip)
    if open_ports:
        print(Colorate.Horizontal(Colors.red_to_yellow, f"Open ports: {open_ports}"))
    else:
        print(Colorate.Horizontal(Colors.gray_to_white, "No open ports found."))

    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter to return...."))
    return True

def main():
    while True:
        clear_screen()
        print_banner()
        domain_or_ip = input(Colorate.Horizontal(Colors.green_to_blue, "Enter domain or IP >> ")).strip()
        if domain_or_ip == "0":
            break  
        server_info(domain_or_ip)

if __name__ == "__main__":
    main()
