import random 
import time
import os
from pystyle import Colors, Colorate, Center

def show_menu():
    title = r"""
.___________      ________               
|   \______ \    /  _____/  ____   ____  
|   ||    |  \  /   \  ____/ __ \ /    \ 
|   ||    `   \ \    \_\  \  ___/|   |  \
|___/_______  /  \______  /\___  >___|  /
            \/          \/     \/     \/ 
    """
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(title)))

    untertext = "[0] Back to Main Menu"
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(untertext)))

def generate_discord_ids(amount):
    for i in range(1, amount + 1):
        snowflake = random.randint(100000000000000000, 999999999999999999)
        print(Colorate.Horizontal(Colors.green_to_blue, f"[{i}/{amount}] Discord ID: {snowflake}"))
        time.sleep(0.05)

    print(Colorate.Horizontal(Colors.green_to_blue, "\nGeneration complete."))
    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter to return to the main menu..."))
    os.system('python main.py')

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    show_menu()
    try:
        user_input = input(Colorate.Horizontal(Colors.green_to_blue, "\nHow many Discord IDs can I generate >> ")).strip()
        if user_input == "0":
            os.system("python main.py")
            return
        amount = int(user_input)
        if amount <= 0:
            raise ValueError
        generate_discord_ids(amount)
    except ValueError:
        print(Colorate.Horizontal(Colors.green_to_blue, "Invalid entry. Please enter a positive number."))
        time.sleep(2)
        main()

if __name__ == "__main__":
    main()
