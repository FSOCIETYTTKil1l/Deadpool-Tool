import uuid
import os
from pystyle import Center, Colorate, Colors

menu = r"""
 ____ ___ ____ ___.___________   
|    |   \    |   \   \______ \  
|    |   /    |   /   ||    |  \ 
|    |  /|    |  /|   ||    `   \
|______/ |______/ |___/_______  /
                              \/ 
"""

def uuid_generator():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(menu)))
        print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter("[0] Back to Main Menu\n")))

        Write = input(Colorate.Horizontal(Colors.green_to_blue, "UUID Generieren >> "))

        new_uuid = str(uuid.uuid4())

        print(Colorate.Horizontal(Colors.green_to_blue, f"\n[+] Generierte UUID: {new_uuid}"))
        print(Colorate.Horizontal(Colors.green_to_blue, "[+] UUIDs are used for sessions, FiveM scripts, logging, and tokens.\n"))

        zurück = input(Colorate.Horizontal(Colors.green_to_blue, "[0] Back to Main Menu")).strip()
        if zurück == "0":
            os.system('python tool.py')
            break

if __name__ == "__main__":
    uuid_generator()
