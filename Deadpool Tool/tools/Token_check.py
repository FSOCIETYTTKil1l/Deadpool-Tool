import os
import re
from pystyle import Colors, Colorate, Center

def show_menu():
    title = r"""
___________     __                   _________ .__                   __                 
\__    ___/___ |  | __ ____   ____   \_   ___ \|  |__   ____   ____ |  | __ ___________ 
  |    | /  _ \|  |/ // __ \ /    \  /    \  \/|  |  \_/ __ \_/ ___\|  |/ // __ \_  __ \
  |    |(  <_> )    <\  ___/|   |  \ \     \___|   Y  \  ___/\  \___|    <\  ___/|  | \/
  |____| \____/|__|_ \\___  >___|  /  \______  /___|  /\___  >\___  >__|_ \\___  >__|   
                    \/    \/     \/          \/     \/     \/     \/     \/    \/       
"""
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(title)))

    untertext = "[0] Back to Main Menu"
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(untertext)))

def is_valid_token(token):
    pattern = r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}"
    return bool(re.fullmatch(pattern, token))

def main():
    os.system("cls" if os.name == "nt" else "clear")
    show_menu()

    token = input(Colorate.Horizontal(Colors.green_to_blue, "Enter token >> "))

    if is_valid_token(token):
        print(Colorate.Horizontal(Colors.green_to_blue, "Token format correct"))
    else:
        print(Colorate.Horizontal(Colors.green_to_blue, "Token format invalid"))

    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter..."))
    os.system("python main.py")

if __name__ == "__main__":
    main()
