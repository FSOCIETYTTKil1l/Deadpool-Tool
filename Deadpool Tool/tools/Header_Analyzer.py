import requests
import os
import time
from pystyle import Colors, Colorate, Center

def show_menu():
    title = r"""
  ___ ___                     .___                _____                .__                              
 /   |   \   ____ _____     __| _/___________    /  _  \   ____ _____  |  | ___.__.________ ___________ 
/    ~    \_/ __ \\__  \   / __ |/ __ \_  __ \  /  /_\  \ /    \\__  \ |  |<   |  |\___   // __ \_  __ \
\    Y    /\  ___/ / __ \_/ /_/ \  ___/|  | \/ /    |    \   |  \/ __ \|  |_\___  | /    /\  ___/|  | \/
 \___|_  /  \___  >____  /\____ |\___  >__|    \____|__  /___|  (____  /____/ ____|/_____ \\___  >__|   
       \/       \/     \/      \/    \/                \/     \/     \/     \/           \/    \/       
"""
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(title)))

    untertext = "[0] Back to Main Menu"
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(untertext)))

def main():
    os.system("cls" if os.name == "nt" else "clear")
    show_menu()

    url = input(Colorate.Horizontal(Colors.green_to_blue, "URL input (https://...) >> "))

    try:
        r = requests.get(url, timeout=5)
        print()
        for k, v in r.headers.items():
            print(Colorate.Horizontal(Colors.green_to_blue, f"{k}: {v}"))
    except:
        print(Colorate.Horizontal(Colors.green_to_blue, "Error during retrieval."))

    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter..."))
    os.system("python main.py")

if __name__ == "__main__":
    main()
