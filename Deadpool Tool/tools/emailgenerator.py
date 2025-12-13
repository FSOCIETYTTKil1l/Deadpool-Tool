import os
import random
import time
from pystyle import Colors, Colorate, Center

MAIL_DOMAINS = [
    "gmail.com", "yahoo.com", "hotmail.com", "gmx.de", "web.de",
    "outlook.com", "icloud.com", "proton.me"
]

VORNAMEN = [
    "alex", "max", "sarah", "julia", "tom", "lisa", "jan", "nina", "paul", "emma",
    "leon", "maria", "sophie", "michael", "andreas", "martin", "johanna",
    "lena", "felix", "emil", "paula", "jonas", "maja", "noah", "ole", "ida", "otto",
    "anna", "eva", "leo", "ben", "carla", "david", "finn", "greta", "hannah",
    "jakob", "karl", "laura", "mila", "niklas", "quinn", "rosa", "simon",
    "ursula", "valentin", "wilma", "xaver", "yara", "zoe", "janine", "christian",
    "oliver", "leonie", "daniel", "philipp", "paulina", "sebastian", "melanie",
    "katharina", "florian", "daniela", "andrea"
]

NACHNAMEN = [
    "mustermann", "schmidt", "mueller", "schneider", "fischer", "weber", "meyer", "wagner",
    "becker", "hoffmann", "schäfer", "koch", "richter", "klein", "wolf", "schröder",
    "neumann", "braun", "huber", "bauer", "krüger", "hartmann", "lange", "schmitt",
    "werner", "franke", "berger", "kaiser", "walter", "hofer", "lorenz", "peters",
    "jung", "heger", "schuster", "barth", "bender", "mayr", "engel", "zahn",
    "fuchs", "jung", "horn", "vogel", "martin", "seidel", "otto", "maier",
    "friedrich", "keller", "ludwig", "arnold", "lang", "jung"
]

def show_menu():
    menu = r"""
___________              .__.__      ________               
\_   _____/ _____ _____  |__|  |    /  _____/  ____   ____  
 |    __)_ /     \\__  \ |  |  |   /   \  ____/ __ \ /    \ 
 |        \  Y Y  \/ __ \|  |  |__ \    \_\  \  ___/|   |  \
/_______  /__|_|  (____  /__|____/  \______  /\___  >___|  /
        \/      \/     \/                  \/     \/     \/ 
"""
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(menu)))

    untertext = "[0] Back to Main Menu"
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(untertext)))

def generate_emails(domain, count):
    for i in range(1, count + 1):
        vorname = random.choice(VORNAMEN)
        nachname = random.choice(NACHNAMEN)
        email_name = f"{vorname}.{nachname}"
        email = f"{email_name}@{domain}"
        print(Colorate.Horizontal(Colors.green_to_blue, f"[{i}/{count}] {email}"))
        time.sleep(0.05)
    
    print(Colorate.Horizontal(Colors.green_to_blue, "\nGeneration complete."))
    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter to return to the main menu..."))
    os.system('python main.py')

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    show_menu()

    user_input = input(Colorate.Horizontal(Colors.green_to_blue, "Choose an email domain >> ")).strip().lower()
    if user_input == "0":
        os.system("python main.py")
        return

    domain = None
    for d in MAIL_DOMAINS:
        if d.startswith(user_input):
            domain = d
            break

    if domain is None:
        print(Colorate.Horizontal(Colors.green_to_blue, f"Invalid domain '{user_input}'. Try again"))
        time.sleep(2)
        main()
        return

    try:
        count = int(input(Colorate.Horizontal(Colors.green_to_blue, "Generate emails >> ")))
        if count <= 0:
            raise ValueError

        generate_emails(domain, count)

    except ValueError:
        print(Colorate.Horizontal(Colors.green_to_blue, "Invalid entry. Please enter a positive number."))
        time.sleep(2)
        main()

if __name__ == "__main__":
    main()
