import requests
import os
from pystyle import Colors, Colorate, Center

def show_menu():
    title = r"""
  _________   _____    ________.____________ .___  ________                      .__                    .___
 /   _____/  /     \  /  _____/|   \_   ___ \|   | \______ \   ______  _  ______ |  |   _________     __| _/
 \_____  \  /  \ /  \/   \  ___|   /    \  \/|   |  |    |  \ /  _ \ \/ \/ /    \|  |  /  _ \__  \   / __ | 
 /        \/    Y    \    \_\  \   \     \___|   |  |    `   (  <_> )     /   |  \  |_(  <_> ) __ \_/ /_/ | 
/_______  /\____|__  /\______  /___|\______  /___| /_______  /\____/ \/\_/|___|  /____/\____(____  /\____ | 
        \/         \/        \/            \/              \/                  \/                \/      \/ 
"""
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(title)))

    untertext = "[0] Back to Main Menu"
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(untertext)))

def main():
    os.system("cls" if os.name == "nt" else "clear")
    show_menu()

    emoji_id = input(Colorate.Horizontal(Colors.green_to_blue, "Emoji ID >> "))

    url = f"https://cdn.discordapp.com/emojis/{emoji_id}.png?size=4096"
    r = requests.get(url)

    if r.status_code == 200:
        with open(f"{emoji_id}.png", "wb") as f:
            f.write(r.content)
        print(Colorate.Horizontal(Colors.green_to_blue, f"Emoji saved: {emoji_id}.png"))
    else:
        print(Colorate.Horizontal(Colors.green_to_blue, "Emoji not found."))

    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter..."))
    os.system("python main.py")

if __name__ == "__main__":
    main()
