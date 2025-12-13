import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import os
from pystyle import Colorate, Colors, Center

menu = """
 _______               ___.                  .____                  __                 
 \      \  __ __  _____\_ |__   ___________  |    |    ____   ____ |  | ____ ________  
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ |    |   /  _ \ /  _ \|  |/ /  |  \____ \ 
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ |    |__(  <_> |  <_> )    <|  |  /  |_> >
\____|__  /____/|__|_|  /___  /\___  >__|    |_______ \____/ \____/|__|_ \____/|   __/ 
        \/            \/    \/     \/                \/                 \/     |__|              
"""

def number_type_name(num_type):
    mapping = {
        phonenumbers.PhoneNumberType.FIXED_LINE: "Fixed Line",
        phonenumbers.PhoneNumberType.MOBILE: "Mobile",
        phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixed Line or Mobile",
        phonenumbers.PhoneNumberType.TOLL_FREE: "Toll Free",
        phonenumbers.PhoneNumberType.PREMIUM_RATE: "Premium Rate",
        phonenumbers.PhoneNumberType.SHARED_COST: "Shared Cost",
        phonenumbers.PhoneNumberType.VOIP: "VoIP",
        phonenumbers.PhoneNumberType.PERSONAL_NUMBER: "Personal Number",
        phonenumbers.PhoneNumberType.PAGER: "Pager",
        phonenumbers.PhoneNumberType.UAN: "UAN",
        phonenumbers.PhoneNumberType.VOICEMAIL: "Voicemail",
        phonenumbers.PhoneNumberType.UNKNOWN: "Unknown"
    }
    return mapping.get(num_type, "Unknown")

def track_phone_number(phone_number):
    phone_number = ''.join(filter(str.isdigit, phone_number))
    try:
        parsed_number = phonenumbers.parse(f"+{phone_number}", None)

        if not phonenumbers.is_valid_number(parsed_number):
            print(Colorate.Horizontal(Colors.green_to_blue, "[!] Invalid phone number format [!]"))
            return

        number_info = {
            "Country": geocoder.description_for_number(parsed_number, 'en'),
            "Carrier": carrier.name_for_number(parsed_number, 'en'),
            "Time Zones": ", ".join(timezone.time_zones_for_number(parsed_number)),
            "National Number": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL),
            "International Number": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
            "E.164 Format": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164),
            "Number Type (Int)": phonenumbers.number_type(parsed_number),
            "Number Type (Name)": number_type_name(phonenumbers.number_type(parsed_number)),
            "Is Possible": phonenumbers.is_possible_number(parsed_number),
            "Is Valid": phonenumbers.is_valid_number(parsed_number),
            "Geographical Area Code Length": phonenumbers.length_of_geographical_area_code(parsed_number),
            "National Destination Code Length": phonenumbers.length_of_national_destination_code(parsed_number),
            "Country Code": parsed_number.country_code,
            "National Number (Raw)": parsed_number.national_number,
            "Leading Zero(s) Present": parsed_number.italian_leading_zero if hasattr(parsed_number, "italian_leading_zero") else False,
            "Number of Extensions": parsed_number.extension if hasattr(parsed_number, "extension") else None,
            "Raw Input": parsed_number.raw_input if hasattr(parsed_number, "raw_input") else phone_number
        }

        print(Colorate.Horizontal(Colors.green_to_blue, f"\nLookup for number '+{phone_number}'..\n"))

        for key, value in number_info.items():
            print(Colorate.Horizontal(Colors.green_to_blue, f"{key}: {value}"))

    except phonenumbers.NumberParseException:
        print(Colorate.Horizontal(Colors.green_to_blue, "[!] Failed to parse phone number [!]"))

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    for line in menu.splitlines():
        print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(line)))
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter("[0] Back to Main Menu\n")))

    phone_number = input(Colorate.Horizontal(Colors.green_to_blue, "Phone Number >> "))

    os.system('cls' if os.name == 'nt' else 'clear')
    for line in menu.splitlines():
        print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(line)))
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter("[0] Back to Main Menu\n")))

    track_phone_number(phone_number)

    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter to exit..."))

if __name__ == "__main__":
    main()
