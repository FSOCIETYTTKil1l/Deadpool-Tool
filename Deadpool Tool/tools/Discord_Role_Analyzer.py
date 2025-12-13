import requests
import os
from pystyle import Colors, Colorate, Center

def show_menu():
    title = r"""
__________       .__          
\______   \ ____ |  |   ____  
 |       _//  _ \|  | _/ __ \ 
 |    |   (  <_> )  |_\  ___/ 
 |____|_  /\____/|____/\___  >
        \/                 \/ 
"""
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(title)))

    untertext = "[0] Back to Main Menu"
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(untertext)))

def main():
    os.system("cls" if os.name == "nt" else "clear")
    show_menu()

    guild_id = input(Colorate.Horizontal(Colors.green_to_blue, "Server ID >> "))

    url = f"https://discord.com/api/v10/guilds/{guild_id}/roles"
    r = requests.get(url)

    if r.status_code != 200:
        print(Colorate.Horizontal(Colors.green_to_blue, "Server not public or ID invalid"))
    else:
        roles = r.json()
        for rle in roles:
            name = rle["name"]
            pos  = rle["position"]
            color = rle["color"]
            print(Colorate.Horizontal(Colors.green_to_blue, f"Role: {name}  |  Position: {pos}  |  Color: #{color:06X}"))

    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter..."))
    os.system("python main.py")

if __name__ == "__main__":
    main()
