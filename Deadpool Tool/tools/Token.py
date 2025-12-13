import random
import string
import time
import os
from pystyle import Colors, Colorate, Center

def show_menu():
    title = r"""
___________     __                  
\__    ___/___ |  | __ ____   ____  
  |    | /  _ \|  |/ // __ \ /    \ 
  |    |(  <_> )    <\  ___/|   |  \
  |____| \____/|__|_ \\___  >___|  /
                    \/    \/     \/ 
    """
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(title)))
    
    untertext = "[0] Back to Main Menu"
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(untertext)))

def generate_token(length=32):
    chars = string.ascii_letters + string.digits + "-_"
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    show_menu()
    count = int(input(Colorate.Horizontal(Colors.green_to_blue, "Generate tokens >> ")))
    length = input(Colorate.Horizontal(Colors.green_to_blue, "Token length >> "))
    length = int(length) if length.strip() != "" else 32
    print()
    for i in range(1, count + 1):
        token = generate_token(length)
        print(Colorate.Horizontal(Colors.green_to_blue, f"[{i}/{count}] Token: {token}"))
        time.sleep(0.1)
    print(Colorate.Horizontal(Colors.green_to_blue, "\nGeneration complete."))
    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter to return to the main menu..."))
    os.system('python main.py')

if __name__ == "__main__":
    main()
