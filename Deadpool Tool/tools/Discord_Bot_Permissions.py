import os
from pystyle import Colors, Colorate, Center

def show_menu():
    title = r"""
__________        __    __________   __           
\______   \ _____/  |_  \______   \_/  |_  _____  
 |    |  _//  _ \   __\  |       _/\   __\/     \ 
 |    |   (  <_> )  |    |    |   \ |  | |  Y Y  \
 |______  /\____/|__|    |____|_  / |__| |__|_|  /
        \/                      \/             \/ 
"""
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(title)))

    untertext = "[0] Back to Main Menu"
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(untertext)))

PERMISSIONS = {
    "1": ("CREATE_INSTANT_INVITE", 0x00000001),
    "2": ("KICK_MEMBERS",         0x00000002),
    "3": ("BAN_MEMBERS",          0x00000004),
    "4": ("ADMINISTRATOR",        0x00000008),
    "5": ("MANAGE_CHANNELS",      0x00000010),
    "6": ("MANAGE_GUILD",         0x00000020),
    "7": ("ADD_REACTIONS",        0x00000040),
    "8": ("VIEW_AUDIT_LOG",       0x00000080),
    "9": ("VIEW_CHANNEL",         0x00000400),
    "10": ("SEND_MESSAGES",       0x00000800),
}

def main():
    os.system("cls" if os.name == "nt" else "clear")
    show_menu()

    bot_id = input(Colorate.Horizontal(Colors.green_to_blue, "Bot ID >> "))
    print()

    print(Colorate.Horizontal(Colors.green_to_blue, "Select Permissions (separated by commas):"))
    for k,v in PERMISSIONS.items():
        print(Colorate.Horizontal(Colors.green_to_blue, f"{k}. {v[0]}"))

    choice = input(Colorate.Horizontal(Colors.green_to_blue, "\nSelection >> ")).split(",")

    perms = 0
    for c in choice:
        c = c.strip()
        if c in PERMISSIONS:
            perms |= PERMISSIONS[c][1]

    invite = f"https://discord.com/oauth2/authorize?client_id={bot_id}&permissions={perms}&scope=bot"
    print(Colorate.Horizontal(Colors.green_to_blue, f"\nInvite-Link:\n{invite}"))

    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter..."))
    os.system("python main.py")


if __name__ == "__main__":
    main()
