import os
import socket
import ipaddress
import platform
from pystyle import Colors, Colorate, Center

def show_menu():
    menu = r"""
 _______          __                       __       _________                                         
 \      \   _____/  |___  _  _____________|  | __  /   _____/ ____ _____    ____   ____   ___________ 
 /   |   \_/ __ \   __\ \/ \/ /  _ \_  __ \  |/ /  \_____  \_/ ___\\__  \  /    \ /    \_/ __ \_  __ \
/    |    \  ___/|  |  \     (  <_> )  | \/    <   /        \  \___ / __ \|   |  \   |  \  ___/|  | \/
\____|__  /\___  >__|   \/\_/ \____/|__|  |__|_ \ /_______  /\___  >____  /___|  /___|  /\___  >__|   
        \/     \/                              \/         \/     \/     \/     \/     \/     \/       
    """
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(menu)))
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter("[0] Back to main menu\n")))

def ping_host(ip):
    if platform.system().lower() == "windows":
        return os.system(f"ping -n 1 -w 1000 {ip} >nul 2>&1")
    else:
        return os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
    
def scan_ports(ip, max_port):
    open_ports = []
    for port in range(1, max_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        if s.connect_ex((ip, port)) == 0:
            open_ports.append(port)
        s.close()
    return open_ports

def ip_scan(subnet, max_port=0):
    print(Colorate.Horizontal(Colors.green_to_blue, f"\nScan network {subnet}...\n"))
    for ip in ipaddress.IPv4Network(subnet, strict=False):
        ip = str(ip)
        if ping_host(ip) == 0:
            print(Colorate.Horizontal(Colors.green_to_blue, f"[+] Device found: {ip}"))
            if max_port > 0:
                ports = scan_ports(ip, max_port)
                if ports:
                    print(Colorate.Horizontal(Colors.red_to_yellow, f"    Open ports: {ports}"))
                else:
                    print(Colorate.Horizontal(Colors.gray_to_white, "    No open ports found"))
    print(Colorate.Horizontal(Colors.green_to_blue, "\nIP scan completed\n"))

def start_scanner():
    while True:
        subnet = input(Colorate.Horizontal(
            Colors.green_to_blue, 
            "Enter your subnet mask >> "
        )).strip()

        if subnet.lower() == "ende":
            print(Colorate.Horizontal(Colors.red, "Program ended."))
            break

        if subnet == "0":
            os.system('python main.py')
            break

        try:
            ipaddress.IPv4Network(subnet, strict=False)
        except ValueError:
            print(Colorate.Horizontal(Colors.red, f"Invalid subnet: {subnet}"))
            continue

        max_port = 0
        scan_ports_choice = input(Colorate.Horizontal(
            Colors.green_to_blue,
            "Ports are also scanned. (y/n) >> "
        )).strip().lower()
        if scan_ports_choice == "y":
            try:
                max_port = int(input(Colorate.Horizontal(
                    Colors.green_to_blue,
                    "Scan to which port >> "
                )))
            except ValueError:
                print(Colorate.Horizontal(Colors.red, "Scan to which port"))

        ip_scan(subnet, max_port)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    show_menu()
    start_scanner()
    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter to exit the program..."))

if __name__ == "__main__":
    main()
