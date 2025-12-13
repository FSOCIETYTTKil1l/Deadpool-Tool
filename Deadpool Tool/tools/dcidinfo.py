import datetime
from pystyle import Colors, Colorate, Center, Write
import os

menu = r"""
________  _________   .___________    .___        _____       
\______ \ \_   ___ \  |   \______ \   |   | _____/ ____\____  
 |    |  \/    \  \/  |   ||    |  \  |   |/    \   __\/  _ \ 
 |    `   \     \____ |   ||    `   \ |   |   |  \  | (  <_> )
/_______  /\______  / |___/_______  / |___|___|  /__|  \____/ 
        \/        \/              \/           \/             
"""

DISCORD_EPOCH = 1420070400000  

def snowflake_to_time(snowflake_id):
    try:
        snowflake_int = int(snowflake_id)
        timestamp = ((snowflake_int >> 22) + DISCORD_EPOCH) / 1000
        return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc)
    except:
        return None

def get_public_avatar_url(user_id):
    return f"https://cdn.discordapp.com/avatars/{user_id}/avatar.png"

def get_discord_username(user_id):
    return "Not publicly available"

def get_public_servers(user_id):
    
    return [
        "discord.gg/S9KSWwtuyk",
        "discord.gg/PublicServer2"
    ]

def discord_osint():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(menu)))
        print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter("[0] Back to Main Menu\n")))

        user_id = Write.Input("Discord User ID >> ", Colors.green_to_blue).strip()
        if user_id == "0":
            break

        created_time = snowflake_to_time(user_id)
        if created_time:
            account_age_days = (datetime.datetime.now(datetime.timezone.utc) - created_time).days

            print(Colorate.Horizontal(Colors.green_to_blue, f"\n[+] Discord ID: {user_id}"))
            print(Colorate.Horizontal(Colors.green_to_blue, f"[+] Account creation date (UTC): {created_time}"))
            print(Colorate.Horizontal(Colors.green_to_blue, f"[+] Account age: {account_age_days} Tage"))
            print(Colorate.Horizontal(Colors.green_to_blue, f"[+] Public avatar URL: {get_public_avatar_url(user_id)}"))
            print(Colorate.Horizontal(Colors.green_to_blue, f"[+] User name: {get_discord_username(user_id)}"))

            print(Colorate.Horizontal(Colors.green_to_blue, "\n[+] Possible OSINT clues (public):"))
            print(Colorate.Horizontal(Colors.green_to_blue, "- Avatar can provide clues (if image is public)"))
            print(Colorate.Horizontal(Colors.green_to_blue, "- Discord Snowflake indicates the age of the account"))
            print(Colorate.Horizontal(Colors.green_to_blue, "- Username (optional) for searching on social media/web"))

            servers = get_public_servers(user_id)
            print(Colorate.Horizontal(Colors.green_to_blue, "\n[+] Public servers where the user is visible:"))
            if servers:
                for server in servers:
                    print(Colorate.Horizontal(Colors.green_to_blue, f"- {server}"))
            else:
                print(Colorate.Horizontal(Colors.red, "- No public servers found"))

        else:
            print(Colorate.Horizontal(Colors.red, "[!] Invalid Discord ID or error determining the creation date."))

        input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter...Press Enter to return to the menu..."))

if __name__ == "__main__":
    discord_osint()
