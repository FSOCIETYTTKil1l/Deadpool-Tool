import random
import time
import os
from pystyle import Colors, Colorate, Center

STREET_NAMES = [
    "Hauptstraße", "Bahnhofstraße", "Gartenweg", "Bergstraße", "Schulstraße",
    "Ringstraße", "Dorfstraße", "Wiesenweg", "Feldweg", "Kirchweg"
]

CITIES = [
    "Berlin", "München", "Hamburg", "Köln", "Frankfurt", "Stuttgart", "Dresden",
    "Leipzig", "Dortmund", "Bremen"
]

POSTAL_CODES = [
    "10115", "80331", "20095", "50667", "60311", "70173", "01067", "04109", "44135", "28195"
]

COUNTRIES = [
    "Deutschland", "Österreich", "Schweiz"
]

def show_menu():
    title = r"""
   _____       .___                                       ________               
  /  _  \    __| _/______   ____   ______ ______ ____    /  _____/  ____   ____  
 /  /_\  \  / __ |\_  __ \_/ __ \ /  ___//  ___// __ \  /   \  ____/ __ \ /    \ 
/    |    \/ /_/ | |  | \/\  ___/ \___ \ \___ \\  ___/  \    \_\  \  ___/|   |  \
\____|__  /\____ | |__|    \___  >____  >____  >\___  >  \______  /\___  >___|  /
        \/      \/             \/     \/     \/     \/          \/     \/     \/ 
    """
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(title)))

    untertext = "[0] Back to main"
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(untertext)))

def generate_address():
    street = random.choice(STREET_NAMES)
    house_number = random.randint(1, 200)
    postal_code = random.choice(POSTAL_CODES)
    city = random.choice(CITIES)
    country = random.choice(COUNTRIES)

    address = f"{street} {house_number}\n{postal_code} {city}\n{country}"
    return address

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    show_menu()
    print()
    user_input = input(Colorate.Horizontal(Colors.green_to_blue, "Generate addresses >> ")).strip()
    if user_input == "0":
        os.system('python main.py')
        return
    count = int(user_input)
    print()
    for i in range(1, count + 1):
        address = generate_address()
        print(Colorate.Horizontal(Colors.green_to_blue, f"[{i}/{count}]\n{address}\n"))
        time.sleep(0.1)
    print(Colorate.Horizontal(Colors.green_to_blue, "\n Generation complete.."))
    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter to return to the main menu..."))
    os.system('python main.py')

if __name__ == "__main__":
    main()
