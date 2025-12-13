import requests
import os
from pystyle import Colors, Colorate, Center

SUBS = ["www", "mail", "ftp", "api", "dev", "test", "ns1", "ns2", "shop", "blog"]

def show_menu():
    title = r"""
  _________    ___.       _________                                         
 /   _____/__ _\_ |__    /   _____/ ____ _____    ____   ____   ___________ 
 \_____  \|  |  \ __ \   \_____  \_/ ___\\__  \  /    \ /    \_/ __ \_  __ \
 /        \  |  / \_\ \  /        \  \___ / __ \|   |  \   |  \  ___/|  | \/
/_______  /____/|___  / /_______  /\___  >____  /___|  /___|  /\___  >__|   
        \/          \/          \/     \/     \/     \/     \/     \/       
"""
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(title)))

    untertext = "[0] Back to Main Menu"
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(untertext)))

def main():
    os.system("cls" if os.name == "nt" else "clear")
    show_menu()

    domain = input(Colorate.Horizontal(Colors.green_to_blue, "Main domain >> "))

    for sub in SUBS:
        url = f"http://{sub}.{domain}"
        try:
            r = requests.get(url, timeout=2)
            if r.status_code < 400:
                print(Colorate.Horizontal(Colors.green_to_blue, f"[+] Found: {url}"))
        except:
            pass

    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter..."))
    os.system("python main.py")

if __name__ == "__main__":
    main()
