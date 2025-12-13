import requests
import os
from pystyle import Colors, Colorate, Center

def show_menu():
    title = r"""
 __      __      ___.   .__                   __    
/  \    /  \ ____\_ |__ |  |__   ____   ____ |  | __
\   \/\/   // __ \| __ \|  |  \ /  _ \ /  _ \|  |/ /
 \        /\  ___/| \_\ \   Y  (  <_> |  <_> )    < 
  \__/\  /  \___  >___  /___|  /\____/ \____/|__|_ \
       \/       \/    \/     \/                   \/
"""
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(title)))

    untertext = "[0] Back to Main Menu"
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(untertext)))

def main():
    os.system("cls" if os.name == "nt" else "clear")
    show_menu()

    webhook = input(Colorate.Horizontal(Colors.green_to_blue, "Webhook URL >> "))
    message = input(Colorate.Horizontal(Colors.green_to_blue, "News >> "))

    r = requests.post(webhook, json={"content": message})

    if r.status_code == 204:
        print(Colorate.Horizontal(Colors.green_to_blue, "Message sent successfully"))
    else:
        print(Colorate.Horizontal(Colors.green_to_blue, f"Mistake ({r.status_code})"))

    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter..."))
    os.system("python main.py")

if __name__ == "__main__":
    main()
