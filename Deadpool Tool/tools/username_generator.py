import random
import time
from pystyle import Colors, Colorate, Center
import os

NAMES = [
    "dragon", "wolf", "ninja", "ghost", "shadow", "knight", "pirate",
    "sniper", "hunter", "wizard", "king", "queen", "alpha", "omega",
    "storm", "blaze", "ice", "fire", "dark", "light", "zero"
]

def show_menu():
    title = r"""
 ____ ___                       ________               
|    |   \______ ___________   /  _____/  ____   ____  
|    |   /  ___// __ \_  __ \ /   \  ____/ __ \ /    \ 
|    |  /\___ \\  ___/|  | \/ \    \_\  \  ___/|   |  \
|______//____  >\___  >__|     \______  /\___  >___|  /
             \/     \/                \/     \/     \/ 
    """
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(title)))

    untertext = "[0] Back to Main Menu"
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(untertext)))


def generate_usernames(count):
    for i in range(1, count + 1):
        name = random.choice(NAMES)
        number = random.randint(10, 9999)
        username = f"{name}{number}"
        print(Colorate.Horizontal(Colors.green_to_blue, f"[{i}/{count}] Username: {username}"))
        time.sleep(0.1)
    
    print(Colorate.Horizontal(Colors.green_to_blue, "\nGeneration complete."))
    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter to return to the main menu..."))
    os.system("python main.py")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    show_menu()
    
    try:
        user_input = input(Colorate.Horizontal(Colors.green_to_blue, "Generate usernames >> ")).strip()
        if user_input == "0":
            os.system("python main.py")
            return
        count = int(user_input)
        if count <= 0:
            raise ValueError
        generate_usernames(count)
    except ValueError:
        print(Colorate.Horizontal(Colors.green_to_blue, "Invalid entry. Please enter a positive number."))
        time.sleep(2)
        main()

if __name__ == "__main__":
    main()
