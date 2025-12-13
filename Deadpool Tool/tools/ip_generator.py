import random
import time
from pystyle import Colors, Colorate, Center
import os

def show_menu():
    title = r"""
.___           ________               
|   |_____    /  _____/  ____   ____  
|   \____ \  /   \  ____/ __ \ /    \ 
|   |  |_> > \    \_\  \  ___/|   |  \
|___|   __/   \______  /\___  >___|  /
    |__|             \/     \/     \/ 
    """
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(title)))

    untertext = "[0] Back to Main Menu"
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(untertext)))

def generate_ips(amount):
    for i in range(1, amount + 1):
        ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
        print(Colorate.Horizontal(Colors.green_to_blue, f"[{i}/{amount}] IP: {ip}"))
        time.sleep(0.05)
    print(Colorate.Horizontal(Colors.green_to_blue, "\nGeneration complete."))
    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter to return to the main menu..."))
    os.system("python main.py") 

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    show_menu()
    
    user_input = input(Colorate.Horizontal(Colors.green_to_blue, "\nHow many IPs are generated? >> ")).strip()
    if user_input == "0":
        os.system("python main.py")
        return

    try:
        amount = int(user_input)
        if amount <= 0:
            raise ValueError
        generate_ips(amount)
    except ValueError:
        print(Colorate.Horizontal(Colors.green_to_blue, "Invalid entry. Please enter a positive number."))
        time.sleep(2)
        main()

if __name__ == "__main__":
    main()
