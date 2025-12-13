import ssl
import socket
import os
from datetime import datetime
from pystyle import Colors, Colorate, Center

def show_menu():
    title = r"""
  _________ _________.____      .___        _____       
 /   _____//   _____/|    |     |   | _____/ ____\____  
 \_____  \ \_____  \ |    |     |   |/    \   __\/  _ \ 
 /        \/        \|    |___  |   |   |  \  | (  <_> )
/_______  /_______  /|_______ \ |___|___|  /__|  \____/ 
        \/        \/         \/          \/             
"""
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(title)))

    untertext = "[0] Back to Main Menu"
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(untertext)))

def ssl_info(host):
    ctx = ssl.create_default_context()
    with socket.create_connection((host, 443)) as sock:
        with ctx.wrap_socket(sock, server_hostname=host) as s:
            cert = s.getpeercert()
            return cert

def main():
    os.system("cls" if os.name == "nt" else "clear")
    show_menu()

    host = input(Colorate.Horizontal(Colors.green_to_blue, "Domain >> "))

    try:
        cert = ssl_info(host)
        print(Colorate.Horizontal(Colors.green_to_blue, f"Issuer: {cert['issuer']}"))
        print(Colorate.Horizontal(Colors.green_to_blue, f"Subject: {cert['subject']}"))
        print(Colorate.Horizontal(Colors.green_to_blue, f"Valid From: {cert['notBefore']}"))
        print(Colorate.Horizontal(Colors.green_to_blue, f"Valid To  : {cert['notAfter']}"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.green_to_blue, "Error during SSL scan."))

    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter..."))
    os.system("python main.py")

if __name__ == "__main__":
    main()
