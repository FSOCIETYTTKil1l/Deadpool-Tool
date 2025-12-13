import requests
from pystyle import Colors, Colorate, Center
import os
import re

menu = r"""
   ________  .__                              .____________                               .___        _____       
   \______ \ |__| ______ ____  ___________  __| _/   _____/ ______________  __ ___________|   | _____/ ____\____  
    |    |  \|  |/  ___// ___\/  _ \_  __ \/ __ |\_____  \_/ __ \_  __ \  \/ // __ \_  __ \   |/    \   __\/  _ \ 
    |    `   \  |\___ \\  \__(  <_> )  | \/ /_/ |/        \  ___/|  | \/\   /\  ___/|  | \/   |   |  \  | (  <_> )
   /_______  /__/____  >\___  >____/|__|  \____ /_______  /\___  >__|    \_/  \___  >__|  |___|___|  /__|  \____/ 
           \/        \/     \/                 \/       \/     \/                 \/               \/                         
"""

def show_menu():
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(menu)))

def extract_invite_code(link_or_code):
    pattern = r"(?:https?://)?(?:www\.)?(?:discord\.gg|discordapp\.com/invite)/([a-zA-Z0-9\-]+)"
    match = re.search(pattern, link_or_code)
    if match:
        return match.group(1)
    else:
        return link_or_code.strip()

def get_discord_invite_info(invite_code):
    urls = [
        f"https://discord.com/api/v10/invites/{invite_code}?with_counts=true&with_expiration=true",
        f"https://discord.com/api/v10/invites/{invite_code}"
    ]
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
        except Exception:
            pass
    return None

def print_info(data):
    guild = data.get('guild', {})
    inviter = data.get('inviter', {})
    channels = data.get('channels', [])
    roles = guild.get('roles', {})
    presence_count = data.get('approximate_presence_count', 'Unknown')
    member_count = data.get('approximate_member_count', 'Unknown')
    expires_at = data.get('expires_at', None)
    created_at = data.get('created_at', 'Unknown')
    uses = data.get('uses', 'Unknown')
    max_uses = data.get('max_uses', 'Unknown')
    max_age = data.get('max_age', 'Unknown')
    temporary = data.get('temporary', 'Unknown')
    vanity_url_code = guild.get('vanity_url_code', 'No')
    description = guild.get('description', 'No description')
    owner_id = guild.get('owner_id', 'Unknown')
    Token = guild.get('Token', 'Unknown')

    print(Colorate.Horizontal(Colors.green_to_blue, f"Server Name: {guild.get('name', 'Unknown')}"))
    print(Colorate.Horizontal(Colors.green_to_blue, f"Server ID: {guild.get('id', 'Unknown')}"))
    print(Colorate.Horizontal(Colors.green_to_blue, f"Members (approximately): {member_count}"))
    print(Colorate.Horizontal(Colors.green_to_blue, f"Online (approximately): {presence_count}"))
    print(Colorate.Horizontal(Colors.green_to_blue, f"Description: {description}"))
    print(Colorate.Horizontal(Colors.green_to_blue, f"Vanity URL Code: {vanity_url_code}"))
    print(Colorate.Horizontal(Colors.green_to_blue, f"Owner ID: {owner_id}"))

    print(Colorate.Horizontal(Colors.green_to_blue, f"Invite Code: {data.get('code', 'Unknown')}"))
    print(Colorate.Horizontal(Colors.green_to_blue, f"Created on: {created_at}"))
    if expires_at:
        print(Colorate.Horizontal(Colors.green_to_blue, f"Expires on: {expires_at}"))
    print(Colorate.Horizontal(Colors.green_to_blue, f"Use: {uses}/{max_uses}"))
    print(Colorate.Horizontal(Colors.green_to_blue, f"Maximum age (sec.): {max_age}"))
    print(Colorate.Horizontal(Colors.green_to_blue, f"Temporary membership (only until logout): {temporary}"))

    if inviter:
        print(Colorate.Horizontal(Colors.green_to_blue, "\nInvitation information:"))
        print(Colorate.Horizontal(Colors.green_to_blue, f"Name: {inviter.get('username', 'Unknown')}#{inviter.get('discriminator', '')}"))
        print(Colorate.Horizontal(Colors.green_to_blue, f"ID: {inviter.get('id', 'Unknown')}"))

    if channels:
        print(Colorate.Horizontal(Colors.green_to_blue, "\nChannels in the invite:"))
        for channel in channels:
            print(Colorate.Horizontal(Colors.green_to_blue, f"- {channel.get('name', 'Unknown')} (ID: {channel.get('id', 'Unknown')}, Typ: {channel.get('type', 'Unknown')})"))

    if roles:
        print(Colorate.Horizontal(Colors.green_to_blue, "\nRoles on the server:"))
        for role_id, role_data in roles.items():
            role_name = role_data.get('name', 'Unknown')
            role_color = role_data.get('color', 0)
            role_hoist = role_data.get('hoist', False)
            role_position = role_data.get('position', 0)
            role_permissions = role_data.get('permissions', 'Keine')
            print(Colorate.Horizontal(Colors.green_to_blue,
                f"- {role_name} (ID: {role_id}, Position: {role_position}, Color: {role_color}, Visible: {role_hoist}, Permissions: {role_permissions})"))

    features = guild.get('features', [])
    if features:
        print(Colorate.Horizontal(Colors.green_to_blue, "\nServer Features:"))
        for feature in features:
            print(Colorate.Horizontal(Colors.green_to_blue, f"- {feature}"))

    if guild.get('banner'):
        print(Colorate.Horizontal(Colors.green_to_blue, f"\nBanner URL: https://cdn.discordapp.com/banners/{guild.get('id')}/{guild.get('banner')}.png"))
    if guild.get('splash'):
        print(Colorate.Horizontal(Colors.green_to_blue, f"Splash URL: https://cdn.discordapp.com/splashes/{guild.get('id')}/{guild.get('splash')}.png"))

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        show_menu()
        print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter("Press 0 to return to the tool.\n")))
        user_input = input(Colorate.Horizontal(Colors.green_to_blue, "Invite code or link >> ")).strip()
        
        if user_input == "0":
            os.system('python tool.py')
            break
        
        invite_code = extract_invite_code(user_input)
        data = get_discord_invite_info(invite_code)
        if data:
            print(Colorate.Horizontal(Colors.green_to_blue, "\nServer information:\n"))
            print_info(data)
        else:
            print(Colorate.Horizontal(Colors.green_to_blue, "\nError: Invalid or missing invite code."))

        input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter...Press Enter to return to the menu..."))

if __name__ == "__main__":
    main()
