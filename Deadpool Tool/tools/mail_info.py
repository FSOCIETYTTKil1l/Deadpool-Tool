import os
import re
import dns.resolver
from pystyle import Colorate, Colors, Center

menu = r"""

   _____         .__.__  .__        _____       
  /     \ _____  |__|  | |__| _____/ ____\____  
 /  \ /  \\__  \ |  |  | |  |/    \   __\/  _ \ 
/    Y    \/ __ \|  |  |_|  |   |  \  | (  <_> )
\____|__  (____  /__|____/__|___|  /__|  \____/ 
        \/     \/                \/                   

"""

resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = ['8.8.8.8', '8.8.4.4']

def get_email_info(email):
    info = {}
    try:
        domain_all = email.split('@')[-1]
    except:
        domain_all = None

    try:
        name = email.split('@')[0]
    except:
        name = None

    try:
        domain = re.search(r"@([^@.]+)\.", email).group(1)
    except:
        domain = None

    try:
        tld = f".{email.split('.')[-1]}"
    except:
        tld = None

    try:
        mx_records = resolver.resolve(domain_all, 'MX')
        mx_servers = [str(record.exchange) for record in mx_records]
        info["mx_servers"] = mx_servers
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
        info["mx_servers"] = None

    try:
        txt_records = resolver.resolve(domain_all, 'TXT')
        spf_records = [str(record).strip('"') for record in txt_records if "v=spf1" in str(record).lower()]
        info["spf_records"] = spf_records if spf_records else None
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
        info["spf_records"] = None

    try:
        dmarc_records = resolver.resolve(f'_dmarc.{domain_all}', 'TXT')
        info["dmarc_records"] = [str(record).strip('"') for record in dmarc_records]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
        info["dmarc_records"] = None

    try:
        a_records = resolver.resolve(domain_all, 'A')
        info["a_records"] = [str(record) for record in a_records]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
        info["a_records"] = None

    try:
        aaaa_records = resolver.resolve(domain_all, 'AAAA')
        info["aaaa_records"] = [str(record) for record in aaaa_records]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
        info["aaaa_records"] = None

    try:
        txt_records = resolver.resolve(domain_all, 'TXT')
        other_txt = [str(record).strip('"') for record in txt_records if "v=spf1" not in str(record).lower() and "_dmarc" not in str(record).lower()]
        info["txt_records"] = other_txt if other_txt else None
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
        info["txt_records"] = None

    if info.get("mx_servers"):
        for server in info["mx_servers"]:
            if "google.com" in server:
                info["google_workspace"] = True
            elif "outlook.com" in server or "office365.com" in server:
                info["microsoft_365"] = True

    return info, domain_all, domain, tld, name

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(menu)))
        print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter("Press [0] to return to the tool.\n")))

        user_input = input(Colorate.Horizontal(Colors.green_to_blue, "Input >> ")).strip()
        if user_input == "0":
            os.system('python tool.py')
            break
        else:
            info, domain_all, domain, tld, name = get_email_info(user_input)

            def join_or_none(key):
                val = info.get(key)
                if isinstance(val, list):
                    return ' / '.join(val)
                return val

            os.system('cls' if os.name == 'nt' else 'clear')
            print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(menu)))
            print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter("Press [0] to return to the tool.\n")))
            print(Colorate.Horizontal(Colors.green_to_blue, f"""
[+] Email         : {user_input}
[+] Name          : {name}
[+] Domain        : {domain}
[+] TLD           : {tld}
[+] Domain All    : {domain_all}
[+] MX Servers    : {join_or_none("mx_servers")}
[+] SPF Records   : {join_or_none("spf_records")}
[+] DMARC Records : {join_or_none("dmarc_records")}
[+] A Records     : {join_or_none("a_records")}
[+] AAAA Records  : {join_or_none("aaaa_records")}
[+] TXT Records   : {join_or_none("txt_records")}
[+] Workspace     : {info.get("google_workspace") or info.get("microsoft_365")}
"""))
            input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter to continue..."))

if __name__ == "__main__":
    main()
