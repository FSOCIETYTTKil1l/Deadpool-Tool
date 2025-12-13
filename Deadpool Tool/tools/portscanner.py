import os
import socket
import time
from pystyle import Colors, Colorate, Center

def show_menu():
    menu = r"""
   __________              __      _________                                         
   \______   \____________/  |_   /   _____/ ____ _____    ____   ____   ___________ 
    |     ___/  _ \_  __ \   __\  \_____  \_/ ___\\__  \  /    \ /    \_/ __ \_  __ \
    |    |  (  <_> )  | \/|  |    /        \  \___ / __ \|   |  \   |  \  ___/|  | \/
    |____|   \____/|__|   |__|   /_______  /\___  >____  /___|  /___|  /\___  >__|   
                                      \/     \/     \/     \/     \/     \/                     
    """
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(menu)))
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter("[0] Back to main menu\n")))

def port_scanner(target, ports):
    print(Colorate.Horizontal(Colors.green_to_blue, f"\nScanne {target}...\n"))
    for port in range(1, ports + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  
        result = s.connect_ex((target, port))  
        if result == 0:
            print(Colorate.Horizontal(Colors.green_to_blue, f"[+] Port {port} open"))
        s.close()
    print(Colorate.Horizontal(Colors.red_to_yellow, "\nScan completed\n"))

def start_scanner():
    while True:
        user_input = input(Colorate.Horizontal(Colors.green_to_blue, "Enter a target IP address or domain >> ")).strip().lower()

        if user_input == "ende":
            print(Colorate.Horizontal(Colors.red, "Program ended."))
            break

        if user_input == "0":
            os.system('python main.py')  
            break

        try:
            target = socket.gethostbyname(user_input)  
        except socket.gaierror:
            print(Colorate.Horizontal(Colors.red, f"Invalid address: {user_input}"))
            continue

        try:
            ports = int(input(Colorate.Horizontal(Colors.green_to_blue, "Scan to which port >> ")))
        except ValueError:
            print(Colorate.Horizontal(Colors.red, "Invalid number."))
            continue

        port_scanner(target, ports)
        time.sleep(1)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    show_menu()
    start_scanner()
    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter to exit the program..."))

if __name__ == "__main__":
    main()
