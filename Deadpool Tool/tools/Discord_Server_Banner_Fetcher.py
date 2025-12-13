import requests
import os
from pystyle import Colors, Colorate, Center

def show_menu():
    title = r"""
___________     __         .__                  
\_   _____/____/  |_  ____ |  |__   ___________ 
 |    __)/ __ \   __\/ ___\|  |  \_/ __ \_  __ \
 |     \\  ___/|  | \  \___|   Y  \  ___/|  | \/
 \___  / \___  >__|  \___  >___|  /\___  >__|   
     \/      \/          \/     \/     \/       
"""
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(title)))

    untertext = "[0] Back to Main Menu"
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(untertext)))

def main():
    os.system("cls" if os.name == "nt" else "clear")
    show_menu()

    gid = input(Colorate.Horizontal(Colors.green_to_blue, "Server-ID >> "))

    url = f"https://discord.com/api/v10/guilds/{gid}?with_counts=true"
    r = requests.get(url)

    if r.status_code != 200:
        print(Colorate.Horizontal(Colors.green_to_blue, "Error! Invalid ID or server not public."))
    else:
        data = r.json()
        if data.get("banner"):
            banner_url = f"https://cdn.discordapp.com/banners/{gid}/{data['banner']}.png?size=4096"
            print(Colorate.Horizontal(Colors.green_to_blue, f"Banner URL:\n{banner_url}"))
        else:
            print(Colorate.Horizontal(Colors.green_to_blue, "This server has no banner."))

    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter..."))
    os.system("python main.py")

if __name__ == "__main__":
    main()
