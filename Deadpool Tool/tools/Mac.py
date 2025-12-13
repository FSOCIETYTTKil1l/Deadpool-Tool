import random
import time
import os
from pystyle import Colors, Colorate, Center

def show_menu():
    title = r"""
   _____                    ________               
  /     \ _____    ____    /  _____/  ____   ____  
 /  \ /  \\__  \ _/ ___\  /   \  ____/ __ \ /    \ 
/    Y    \/ __ \\  \___  \    \_\  \  ___/|   |  \
\____|__  (____  /\___  >  \______  /\___  >___|  /
        \/     \/     \/          \/     \/     \/ 
    """
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(title)))

    untertext = "[0] Back to Main Menu"
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(untertext)))

def generate_mac():
    mac = [random.randint(0x00, 0xFF) for _ in range(6)]
    return ':'.join(f"{b:02X}" for b in mac)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    show_menu()
    
    user_input = input(Colorate.Horizontal(Colors.green_to_blue, "Generate MAC addresses >> ")).strip()
    if user_input == "0":
        os.system("python main.py")
        return

    count = int(user_input)
    print()
    for i in range(1, count + 1):
        mac = generate_mac()
        print(Colorate.Horizontal(Colors.green_to_blue, f"[{i}/{count}] MAC-Adresse: {mac}"))
        time.sleep(0.1)
        
    print(Colorate.Horizontal(Colors.green_to_blue, "\nGeneration complete."))
    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter to return to the main menu..."))
    os.system('python main.py')

if __name__ == "__main__":
    main()
