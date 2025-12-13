import dns.resolver
import os
from pystyle import Colors, Colorate, Center
import time

def show_menu():
    title = r"""
________    _______    _________ .____                  __                 
\______ \   \      \  /   _____/ |    |    ____   ____ |  | ____ ________  
 |    |  \  /   |   \ \_____  \  |    |   /  _ \ /  _ \|  |/ /  |  \____ \ 
 |    `   \/    |    \/        \ |    |__(  <_> |  <_> )    <|  |  /  |_> >
/_______  /\____|__  /_______  / |_______ \____/ \____/|__|_ \____/|   __/ 
        \/         \/        \/          \/                 \/     |__|    
"""
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(title)))

    untertext = "[0] Back to Main Menu"
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(untertext)))

def dns_lookup(domain):
    record_types = ["A", "AAAA", "MX", "NS", "TXT"]
    for rtype in record_types:
        print(Colorate.Horizontal(Colors.green_to_blue, f"\n--- {rtype} ---"))
        try:
            answers = dns.resolver.resolve(domain, rtype)
            for ans in answers:
                print(Colorate.Horizontal(Colors.green_to_blue, str(ans)))
        except:
            print(Colorate.Horizontal(Colors.green_to_blue, "No entries."))

def main():
    os.system("cls" if os.name == "nt" else "clear")
    show_menu()

    domain = input(Colorate.Horizontal(Colors.green_to_blue, "Domain >> "))
    dns_lookup(domain)

    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter..."))
    os.system("python main.py")

if __name__ == "__main__":
    main()
