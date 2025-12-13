import random
import string
import time
from pystyle import Colors, Colorate, Center
import os

def show_menu():
    title = r"""
__________                          ________               
\______   \_____    ______ ______  /  _____/  ____   ____  
 |     ___/\__  \  /  ___//  ___/ /   \  ____/ __ \ /    \ 
 |    |     / __ \_\___ \ \___ \  \    \_\  \  ___/|   |  \
 |____|    (____  /____  >____  >  \______  /\___  >___|  /
                \/     \/     \/          \/     \/     \/ 
    """
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(title)))

    untertext = "[0] Back to Main Menu"
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(untertext)))

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def generate_passwords(count, length=12):
    for i in range(1, count + 1):
        password = generate_password(length)
        print(Colorate.Horizontal(Colors.green_to_blue, f"[{i}/{count}] Password: {password}"))
        time.sleep(0.1)
    
    print(Colorate.Horizontal(Colors.green_to_blue, "\nGeneration complete."))
    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter to return to the main menu..."))
    os.system("python main.py")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    show_menu()

    user_input = input(Colorate.Horizontal(Colors.green_to_blue, "\nGenerate passwords >> ")).strip()
    if user_input == "0":
        os.system("python main.py")
        return

    try:
        count = int(user_input)
        if count <= 0:
            raise ValueError

        length = int(input(Colorate.Horizontal(Colors.green_to_blue, "Length of passwords >> ")))
        if length < 4:
            print(Colorate.Horizontal(Colors.green_to_blue, "Password length too short. Minimum 4 characters."))
            time.sleep(2)
            return main()

        generate_passwords(count, length)

    except ValueError:
        print(Colorate.Horizontal(Colors.green_to_blue, "Invalid entry. Please enter numbers only."))
        time.sleep(2)
        main()

if __name__ == "__main__":
    main()
