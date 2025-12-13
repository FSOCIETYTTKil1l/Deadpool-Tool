import random
import time
import os
from pystyle import Colors, Colorate, Center

BROWSERS = [
    "Firefox", "Chrome", "Safari", "Edge", "Opera"
]

OS = [
    "Windows NT 10.0; Win64; x64",
    "Macintosh; Intel Mac OS X 10_15_7",
    "X11; Linux x86_64",
    "Windows NT 6.1; Win64; x64",
    "Android 10; Mobile"
]

def show_menu():
    title = r"""
__________                      __                          ________               
\______   \ ____   ____  __ ___/  |_________ ___________   /  _____/  ____   ____  
 |    |  _// __ \ /    \|  |  \   __\___   // __ \_  __ \ /   \  ____/ __ \ /    \ 
 |    |   \  ___/|   |  \  |  /|  |  /    /\  ___/|  | \/ \    \_\  \  ___/|   |  \
 |______  /\___  >___|  /____/ |__| /_____ \\___  >__|     \______  /\___  >___|  /
        \/     \/     \/                  \/    \/                \/     \/     \/ 
    """
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(title)))

    untertext = "[0] Back to Main Menu"
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(untertext)))

def generate_user_agent():
    browser = random.choice(BROWSERS)
    os_part = random.choice(OS)
    version = f"{random.randint(50,100)}.0"
    if browser == "Firefox":
        ua = f"Mozilla/5.0 ({os_part}; rv:{version}) Gecko/20100101 Firefox/{version}"
    elif browser == "Chrome":
        build = f"{random.randint(500,600)}.{random.randint(0,3000)}.{random.randint(0,200)}"
        ua = f"Mozilla/5.0 ({os_part}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version}.{build} Safari/537.36"
    elif browser == "Safari":
        webkit_version = f"{random.randint(600,700)}.{random.randint(0,50)}"
        ua = f"Mozilla/5.0 ({os_part}) AppleWebKit/{webkit_version} (KHTML, like Gecko) Version/{version} Safari/{webkit_version}"
    elif browser == "Edge":
        ua = f"Mozilla/5.0 ({os_part}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Safari/537.36 Edg/{version}"
    else: 
        ua = f"Mozilla/5.0 ({os_part}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Safari/537.36 OPR/{version}"
    return ua

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    show_menu()
    user_input = input(Colorate.Horizontal(Colors.green_to_blue, "Generate strings? >> ")).strip()
    if user_input == "0":
        os.system('python main.py')
        return
    count = int(user_input)
    print()
    for i in range(1, count + 1):
        ua = generate_user_agent()
        print(Colorate.Horizontal(Colors.green_to_blue, f"[{i}/{count}] {ua}"))
        time.sleep(0.1)
    print(Colorate.Horizontal(Colors.green_to_blue, "\nGeneration complete."))
    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter to return to the main menu..."))
    os.system('python main.py')

if __name__ == "__main__":
    main()
