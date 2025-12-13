import requests
import os
from pystyle import Colors, Colorate, Center

def show_menu():
    title = r"""
________  _________   .__            .__  __           .___        _____        
\______ \ \_   ___ \  |__| _______  _|__|/  |_  ____   |   | _____/ ____\____   
 |    |  \/    \  \/  |  |/    \  \/ /  \   __\/ __ \  |   |/    \   __\/  _ \  
 |    `   \     \____ |  |   |  \   /|  ||  | \  ___/  |   |   |  \  | (  <_> ) 
/_______  /\______  / |__|___|  /\_/ |__||__|  \___  > |___|___|  /__|  \____/  
        \/        \/          \/                   \/           \/              
"""
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(title)))

    untertext = "[0] Back to Main Menu"
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(untertext)))

def main():
    os.system("cls" if os.name == "nt" else "clear")
    show_menu()

    invite_code = input(Colorate.Horizontal(Colors.green_to_blue, "Discord Invite Code >> ")).strip()

    url = f"https://discord.com/api/v10/invites/{invite_code}?with_counts=true"
    r = requests.get(url)

    if r.status_code != 200:
        print(Colorate.Horizontal(Colors.green_to_blue, "Invalid invite or server not public"))
    else:
        data = r.json()
        guild = data.get("guild", {})
        print(Colorate.Horizontal(Colors.green_to_blue, f"\nServer Name: {guild.get('name')}"))
        print(Colorate.Horizontal(Colors.green_to_blue, f"Mitglieder: {guild.get('approximate_member_count')}"))
        print(Colorate.Horizontal(Colors.green_to_blue, f"Online: {guild.get('approximate_presence_count')}"))
        print(Colorate.Horizontal(Colors.green_to_blue, f"Boost Level: {guild.get('premium_tier')}"))
        print(Colorate.Horizontal(Colors.green_to_blue, f"Region: {guild.get('region', 'N/A')}"))

    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter..."))
    os.system("python main.py")

if __name__ == "__main__":
    main()
