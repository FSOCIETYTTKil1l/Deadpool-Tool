import os
import requests
import socket
from pystyle import Center, Colorate, Colors

menu = """
._____________  .____                  __                 
|   \\______   \\ |    |    ____   ____ |  | ____ ________  
|   ||     ___/ |    |   /  _ \\ /  _ \\|  |/ /  |  \\____ \\ 
|   ||    |     |    |__(  <_> |  <_> )    <|  |  /  |_> >
|___||____|     |_______ \\____/ \\____/|__|_ \\____/|   __/ 
                        \\/                 \\/     |__|    
"""

def reverse_dns(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "N/A"

def ip_info(ip):
    try:
        url = f"http://ip-api.com/json/{ip}?fields=66846719"
        r = requests.get(url, timeout=10)
        data = r.json()

        if data.get('status') != 'success':
            print(Colorate.Horizontal(Colors.red_to_yellow, f"Error: {data.get('message', 'Invalid IP address or no data')}"))
            return

        hostname = reverse_dns(ip)

        fields = {
            "IP": data.get('query', 'N/A'),
            "Status": data.get('status', 'N/A'),
            "Country": f"{data.get('country', 'N/A')} ({data.get('countryCode', 'N/A')})",
            "Region": f"{data.get('regionName', 'N/A')} ({data.get('region', 'N/A')})",
            "City": data.get('city', 'N/A'),
            "ZIP": data.get('zip', 'N/A'),
            "Latitude": data.get('lat', 'N/A'),
            "Longitude": data.get('lon', 'N/A'),
            "Timezone": data.get('timezone', 'N/A'),
            "ISP": data.get('isp', 'N/A'),
            "Organisation": data.get('org', 'N/A'),
            "AS": data.get('as', 'N/A'),
            "Mobile": data.get('mobile', 'N/A'),
            "Proxy": data.get('proxy', 'N/A'),
            "Hosting": data.get('hosting', 'N/A'),
            "Reverse DNS (Hostname)": hostname,
            "Currency": data.get('currency', 'N/A'),
            "Offset": data.get('offset', 'N/A'),
            "Region Code": data.get('region', 'N/A'),
        }

        for key, value in fields.items():
            print(Colorate.Horizontal(Colors.green_to_blue, f"{key} : {value}"))

        lat = data.get('lat', 0)
        lon = data.get('lon', 0)
        print(Colorate.Horizontal(Colors.green_to_blue, f"Google Maps: https://www.google.com/maps/search/?api=1&query={lat},{lon}"))

    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_yellow, f"Query error: {e}"))

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(menu)))
        print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter("[0] Back to Main Menu\n")))
        
        ip_address = input(Colorate.Horizontal(Colors.green_to_blue, "IP >> ")).strip()
        
        if ip_address == "0":
            os.system('python tool.py')
            break
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(menu)))
        print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter("[0] Back to Main Menu\n")))
        ip_info(ip_address)
        
        print()
        print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter("Press Enter for a new query or 0 to exit.")))
        zurück = input(Colorate.Horizontal(Colors.green_to_blue, "input : ")).strip()
        if zurück == "0":
            os.system('python tool.py')
            break

if __name__ == "__main__":
    main()
