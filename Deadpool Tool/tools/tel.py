import random
import time
import os
from pystyle import Colors, Colorate, Center

GERMAN_PREFIXES = ["015", "016", "017", "030", "040", "069", "089"]

def show_menu():
    title = r"""
 _______                                         ________               
 \      \  __ __  _____   _____   ___________   /  _____/  ____   ____  
 /   |   \|  |  \/     \ /     \_/ __ \_  __ \ /   \  ____/ __ \ /    \ 
/    |    \  |  /  Y Y  \  Y Y  \  ___/|  | \/ \    \_\  \  ___/|   |  \
\____|__  /____/|__|_|  /__|_|  /\___  >__|     \______  /\___  >___|  /
        \/            \/      \/     \/                \/     \/     \/ 
    """
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(title)))
    
    untertext = "[0] Back to Main Menu"
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(untertext)))

def generate_phone_number():
    prefix = random.choice(GERMAN_PREFIXES)
    length = 7 if prefix in ["015", "016", "017"] else 8
    number = ''.join(str(random.randint(0,9)) for _ in range(length))
    return f"+49 {prefix} {number}"

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    show_menu()
    
    user_input = input(Colorate.Horizontal(Colors.green_to_blue, "Generate phone numbers >> ")).strip()
    if user_input == "0":
        os.system("python main.py")
        return

    count = int(user_input)
    print()
    for i in range(1, count + 1):
        phone = generate_phone_number()
        print(Colorate.Horizontal(Colors.green_to_blue, f"[{i}/{count}] {phone}"))
        time.sleep(0.1)
        
    print(Colorate.Horizontal(Colors.green_to_blue, "\nGeneration complete."))
    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter to return to the main menu..."))
    os.system('python main.py')

if __name__ == "__main__":
    main()
