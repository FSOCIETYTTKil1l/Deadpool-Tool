import os
from pystyle import Colors, Colorate, Center

def show_menu():
    title = r"""
   _____                __       .___                   
  /     \ _____ _______|  | __ __| _/______  _  ______  
 /  \ /  \\__  \\_  __ \  |/ // __ |/  _ \ \/ \/ /    \ 
/    Y    \/ __ \|  | \/    </ /_/ (  <_> )     /   |  \
\____|__  (____  /__|  |__|_ \____ |\____/ \/\_/|___|  /
        \/     \/           \/    \/                 \/ 
"""
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(title)))

    untertext = "[0] Back to Main Menu"
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(untertext)))

def main():
    os.system("cls" if os.name == "nt" else "clear")
    show_menu()

    text = input(Colorate.Horizontal(Colors.green_to_blue, "Text >> "))

    formats = {
        "Bold": f"**{text}**",
        "Italic": f"*{text}*",
        "Underline": f"__{text}__",
        "Spoiler": f"||{text}||",
        "Code": f"`{text}`",
        "Block": f"```\n{text}\n```"
    }

    print()
    for k,v in formats.items():
        print(Colorate.Horizontal(Colors.green_to_blue, f"{k}: {v}"))

    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter..."))
    os.system("python main.py")

if __name__ == "__main__":
    main()
