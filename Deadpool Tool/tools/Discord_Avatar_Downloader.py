import requests
import os
from pystyle import Colors, Colorate, Center

def show_menu():
    title = r"""
   _____                __                
  /  _  \___  _______ _/  |______ _______ 
 /  /_\  \  \/ /\__  \\   __\__  \\_  __ \
/    |    \   /  / __ \|  |  / __ \|  | \/
\____|__  /\_/  (____  /__| (____  /__|   
        \/           \/          \/       
"""
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(title)))

    untertext = "[0] Back to Main Menu"
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(untertext)))

def main():
    os.system("cls" if os.name == "nt" else "clear")
    show_menu()

    user_id = input(Colorate.Horizontal(Colors.green_to_blue, "User ID >> "))

    url = f"https://discord.com/api/v10/users/{user_id}"
    r = requests.get(url)

    if r.status_code != 200:
        print(Colorate.Horizontal(Colors.green_to_blue, "Error or user not public"))
    else:
        avatar = r.json().get("avatar")
        if avatar:
            avatar_url = f"https://cdn.discordapp.com/avatars/{user_id}/{avatar}.png?size=4096"
            img = requests.get(avatar_url).content
            with open(f"{user_id}.png", "wb") as f:
                f.write(img)
            print(Colorate.Horizontal(Colors.green_to_blue, f"Avatar saved: {user_id}.png"))
        else:
            print(Colorate.Horizontal(Colors.green_to_blue, "User does not have an avatar"))

    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter..."))
    os.system("python main.py")

if __name__ == "__main__":
    main()
