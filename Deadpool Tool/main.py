import os
import shutil
import time
from pystyle import Colorate, Colors
import os
import sys

def get_terminal_size():
    return shutil.get_terminal_size()

def center_text(text, width):
    lines = text.splitlines()
    centered_lines = [line.center(width) for line in lines]
    return "\n".join(centered_lines)

def blinking():
    text = """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⣀⣠⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢉⠄⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠔⠀⢂⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⡀⠂⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⡂⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠎⠁⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠸⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠐⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡧⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠈⠿⢿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠸⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⢀⣶⣾⣾⣿⣿⣿⠇⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠣⠀⣠⢀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⠏⢠⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠅⠙⠊⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⡿⠋⢠⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠡⡀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⢀⢌⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠈⠀⠀⡄⠀⠀⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⡿⠟⡛⠉⢀⠄⢡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠃⢀⠀⠀⠀⠀⡔⢢⠉⠉⠉⠉⠉⠉⠀⠀⡀⠀⠂⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠀⠀⠀⠈⠐⠂⠬⠅⠀⠀⠀⠠⠼⠑⠂⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
 (Loading)
    """
    terminal_size = get_terminal_size()
    centered_text = center_text(text, terminal_size.columns)

    for _ in range(3):
        os.system('cls' if os.name == 'nt' else 'clear')
        # Hier Farbverlauf auf den gesamten Text anwenden:
        print(Colorate.Horizontal(Colors.green_to_blue, centered_text))
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.5)

nheader = r"""
  ________                     .___                    ._____________           .____     
  \______ \   ____ _____     __| _/_____   ____   ____ |  \__    ___/___   ____ |    |    
   |    |  \_/ __ \\__  \   / __ |\____ \ /  _ \ /  _ \|  | |    | /  _ \ /  _ \|    |    
   |        \  ___/ / __ \_/ /_/ ||  |_> >  <_> |  <_> )  |_|    |(  <_> |  <_> )    |___ 
  /_______  /\___  >____  /\____ ||   __/ \____/ \____/|____/____| \____/ \____/|_______ \
          \/     \/     \/      \/|__|                                                  \/
"""

menu = """
████████████████████████████████████████████████████████████████████████████████████████   ╔══════════════════╗  
██     Discord Tools       ██           OSINT             ██         Generator        ██   ║ Deadpool Tool V1 ║  
████████████████████████████████████████████████████████████████████████████████████████   ╚══════════════════╝ 
██                         ██                             ██                          ██   ╔═══════════════════╗
██   [1] DC Id info        ██   [12] IP Lookup            ██   [23] Email GEN         ██   ║    Made by Kil1l  ║
██   [2] DC Server info    ██   [13] Mail Info            ██   [24] IP GEN            ██   ╚═══════════════════╝     
██   [3] DC SMGI Download  ██   [14] Username Tracker     ██   [25] Adresse GEN       ██   ╔═══════════════════╗
██   [4] DC Token Checker  ██   [15] Phone Number Lookup  ██   [26] Benutzer GEN      ██   ║   Name : root     ║
██   [5] DC Server Fetcher ██   [16] Port Scanner         ██   [27] DC id GEN         ██   ╚═══════════════════╝
██   [6] DC Bot Perms      ██   [17] Network Scanner      ██   [28] Password GEN      ██   ╔═══════════════════╗        
██   [7] DC Webhook Tester ██   [18] Server info          ██   [29] Tel GEN           ██   ║ WLANSTATUS : ON   ║
██   [8] DC Role Analyzer  ██   [19] SSL Scanner          ██   [30] Token GEN         ██   ╚═══════════════════╝
██   [9] DC Avata Download ██   [20] Subdomin Scanner     ██   [31] User GEN          ██   ╔════════════════════════╗
██   [10] DC Markdown      ██   [21] DNS Lookup           ██   [32] UUID GEN          ██   ║  discord.gg/qJxYDurpKk ║
██   [11] DC invite info   ██   [22] Header Analazer      ██   [33] Color GEN         ██   ╚════════════════════════╝
██                         ██                             ██                          ██   ╔════════════════════════╗
████████████████████████████████████████████████████████████████████████████████████████   ║   Version : 1.20.1     ║
                                                                                           ╚════════════════════════╝         
"""                   

def choice_script(choice):
    if choice == 1:
        os.system('python ./tools/dcidinfo.py')  
    elif choice == 2:
        os.system('python ./tools/Discord-Server-Info.py')
    elif choice == 3:
        os.system('python ./tools/Discord_Emoji_Downloader.py')
    elif choice == 4:
        os.system('python ./tools/Token_check.py')
    elif choice == 5:
        os.system('python ./tools/Discord_Server_Banner_Fetcher.py')
    elif choice == 6:
        os.system('python ./tools/Discord_Bot_Permissions.py')
    elif choice == 7:
        os.system('python ./tools/Discord_Webhook_Tester.py')
    elif choice == 8:
        os.system('python ./tools/Discord_Role_Analyzer.py')
    elif choice == 9:
        os.system('python ./tools/Discord_Avatar_Downloader.py')
    elif choice == 10:
        os.system('python ./tools/Discord_Markdown_Message.py')
    elif choice == 11:
        os.system('python ./tools/DC_invite_info.py')
    elif choice == 12:
        os.system('python ./tools/location.py')
    elif choice == 13:
        os.system('python ./tools/mail_info.py')
    elif choice == 14:
        os.system('python ./tools/username_tracker.py')
    elif choice == 15:
        os.system('python ./tools/Phone_Number_Lookup.py')
    elif choice == 16:
        os.system('python ./tools/portscanner.py')
    elif choice == 17:
        os.system('python ./tools/Netzwerk_scannt.py')
    elif choice == 18:
        os.system('python ./tools/Server_info.py')
    elif choice == 19:
        os.system('python ./tools/SSL_Certificate_Info.py')
    elif choice == 20:
        os.system('python ./tools/Subdomain_Scanner.py')
    elif choice == 21:
        os.system('python ./tools/DNS_Lookup.py')
    elif choice == 22:
        os.system('python ./tools/Header_Analyzer.py')
    elif choice == 23:
        os.system('python ./tools/emailgenerator.py')
    elif choice == 24:
        os.system('python ./tools/ip_generator.py')
    elif choice == 25:
        os.system('python ./tools/addrese.py')
    elif choice == 26:
        os.system('python ./tools/benutzer.py')
    elif choice == 27:
        os.system('python ./tools/discord_id_generator.py')
    elif choice == 28:
        os.system('python ./tools/password_generator.py')
    elif choice == 29:
        os.system('python ./tools/tel.py')
    elif choice == 30:
        os.system('python ./tools/Token.py')
    elif choice == 31:
        os.system('python ./tools/username_generator.py')
    elif choice == 32:
        os.system('python ./tools/UUID-GENERATOR.py')
    elif choice == 33:
        os.system('python ./tools/RANDOM_COLOR_GENERATOR.py')
    else:
        raise ValueError


def main():  
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Colorate.Horizontal(Colors.green_to_blue, nheader))
        print() 
        print(Colorate.Horizontal(Colors.green_to_blue, menu))
        print()
        
        try:
            print(Colorate.Horizontal(Colors.green_to_blue, "╔═══[root@Deadpool]"))
            choice = int(input(Colorate.Horizontal(Colors.green_to_blue, "╚══> ")))
            choice_script(choice)
        except ValueError:
            print("\033[31m[!] >\033[0m Invalid choice \033[31m< [!]\033[0m")
            time.sleep(2)

if __name__ == "__main__":
    blinking()
    main()