import random
import os
from pystyle import Center, Colorate, Colors

menu = r"""
_________  ________  .____    ________ __________ 
\_   ___ \ \_____  \ |    |   \_____  \\______   \
/    \  \/  /   |   \|    |    /   |   \|       _/
\     \____/    |    \    |___/    |    \    |   \
 \______  /\_______  /_______ \_______  /____|_  /
        \/         \/        \/       \/       \/ 
"""

def random_hex():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def color_generator():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(menu)))
        print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter("[0] Back to Main Menu\n")))

        input(Colorate.Horizontal(Colors.green_to_blue, "Press Enter to generate a color >> "))

        hex_color = random_hex()

        print(Colorate.Horizontal(Colors.green_to_blue, f"\n[+] Generierte HEX-Farbe: {hex_color}"))
        print(Colorate.Horizontal(Colors.green_to_blue, "[+] HEX is used in CSS, HTML, FiveM UI, and scripts.\n"))

        zurück = input(Colorate.Horizontal(Colors.green_to_blue, "[0] Back to main menu")).strip()
        if zurück == "0":
            os.system('python tool.py')
            break

if __name__ == "__main__":
    color_generator()
