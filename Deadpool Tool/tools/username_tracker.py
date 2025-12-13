import requests
import os
import time
from pystyle import Colorate, Colors, Center

menu = """
   ___________                     __                 
   \\__    ___/___________    ____ |  | __ ___________ 
     |    |  \\_  __ \\__  \\ _/ ___\\|  |/ // __ \\_  __ \\
     |    |   |  | \\// __ \\\\  \\___|    <\\  ___/|  | \\/
     |____|   |__|  (____  /\\___  >__|_ \\\\___  >__|   
                         \\/     \\/     \\/    \\/       
"""

def print_menu():
    centered_text = Center.XCenter(menu)
    print(Colorate.Horizontal(Colors.green_to_blue, centered_text))

    untertext = "[0] Back to Main Menu"
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(untertext)))


def username(username):
    sites = {
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Tumblr": f"https://{username}.tumblr.com",
        "YouTube": f"https://www.youtube.com/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "Patreon": f"https://www.patreon.com/{username}",
        "WordPress": f"https://{username}.wordpress.com",
        "Spotify": f"https://open.spotify.com/user/{username}",
        "GitLab": f"https://gitlab.com/{username}",
        "Mixcloud": f"https://www.mixcloud.com/{username}",
        "PayPal": f"https://www.paypal.me/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "Guns.lol": f"https://guns.lol/{username}",
        "Flickr": f"https://www.flickr.com/photos/{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "Discord": f"https://discord.com/users/{username}",
        "HackerOne": f"https://hackerone.com/{username}",
        "RedBubble": f"https://www.redbubble.com/people/{username}",
        "Medium": f"https://medium.com/@{username}",
        "Dribbble": f"https://dribbble.com/{username}",
        "Behance": f"https://www.behance.net/{username}",
        "CodePen": f"https://codepen.io/{username}",
        "ProductHunt": f"https://www.producthunt.com/@{username}",
        "Knuddels": f"https://knuddels.de/profile/{username}",
        "DiscordBots": f"https://discord.bots.gg/u/{username}",
        "Etsy": f"https://www.etsy.com/people/{username}",
        "Goodreads": f"https://www.goodreads.com/user/show/{username}",
        "IFTTT": f"https://ifttt.com/p/{username}",
        "Kaggle": f"https://www.kaggle.com/{username}",
        "Letterboxd": f"https://letterboxd.com/{username}",
        "Lichess": f"https://lichess.org/@/{username}",
        "Mastodon": f"https://mastodon.social/@{username}",
        "Notion": f"https://www.notion.so/{username}",
        "Quora": f"https://www.quora.com/profile/{username}",
        "StackOverflow": f"https://stackoverflow.com/users/{username}",
        "Strava": f"https://www.strava.com/athletes/{username}",
        "Telegram": f"https://t.me/{username}",
        "Unsplash": f"https://unsplash.com/@{username}",
        "VK": f"https://vk.com/{username}",
        "Weebly": f"https://{username}.weebly.com",
        "Wikipedia": f"https://en.wikipedia.org/wiki/User:{username}",
        "Wikidot": f"https://{username}.wikidot.com",
        "Xing": f"https://www.xing.com/profile/{username}",
        "Yelp": f"https://www.yelp.com/user_details?userid={username}",
        "Zoom": f"https://zoom.us/{username}",
        "AngelList": f"https://angel.co/u/{username}",
        "Blogger": f"https://{username}.blogspot.com",
        "Coub": f"https://coub.com/{username}",
        "Deezer": f"https://www.deezer.com/profile/{username}",
        "Ello": f"https://ello.co/{username}",
        "Flipboard": f"https://flipboard.com/@{username}",
        "Hootsuite": f"https://hootsuite.com/{username}",
        "Imgur": f"https://imgur.com/user/{username}",
        "Loom": f"https://www.loom.com/@{username}",
        "Mix": f"https://mix.com/{username}",
        "MyAnimeList": f"https://myanimelist.net/profile/{username}",
        "Periscope": f"https://www.pscp.tv/{username}",
        "Photobucket": f"https://photobucket.com/{username}",
        "ReverbNation": f"https://www.reverbnation.com/{username}",
        "Scribd": f"https://www.scribd.com/{username}",
        "Shutterstock": f"https://www.shutterstock.com/g/{username}",
        "Slideshare": f"https://www.slideshare.net/{username}",
        "TripAdvisor": f"https://www.tripadvisor.com/members/{username}",
        "Vine": f"https://vine.co/u/{username}",
        " Academia.edu": f"https://www.academia.edu/{username}",
        "About.me": f"https://about.me/{username}",
        "Allociné": f"https://www.allocine.fr/personne/{username}",
        "Angel.co": f"https://angel.co/{username}",
        "Badoo": f"https://badoo.com/en/{username}",
        "Behance": f"https://www.behance.net/{username}",
        "Bitbucket": f"https://bitbucket.org/{username}",
        "Booking.com": f"https://www.booking.com/profile/{username}",
        "BuzzFeed": f"https://www.buzzfeed.com/{username}",
        "CafeMom": f"https://www.cafemom.com/user/{username}",
        "CaringBridge": f"https://www.caringbridge.org/visit/{username}",
        "Classmates": f"https://www.classmates.com/member/{username}",
        "Codecademy": f"https://www.codecademy.com/{username}",
        "Codewars": f"https://www.codewars.com/users/{username}",
        "Couchsurfing": f"https://www.couchsurfing.com/people/{username}",
        "Coursera": f"https://www.coursera.org/user/{username}",
        "Crunchbase": f"https://www.crunchbase.com/person/{username}",
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "Diigo": f"https://www.diigo.com/user/{username}",
        "Disqus": f"https://disqus.com/{username}",
        "Dribbble": f"https://dribbble.com/{username}",
        "Duolingo": f"https://www.duolingo.com/profile/{username}",
        "Ebay": f"https://www.ebay.com/usr/{username}",
        "Etsy": f"https://www.etsy.com/shop/{username}",
        "Eventbrite": f"https://www.eventbrite.com/o/{username}",
        "Foursquare": f"https://foursquare.com/user/{username}",
        "Gaia Online": f"https://www.gaiaonline.com/profiles/{username}",
        "Goodreads": f"https://www.goodreads.com/user/show/{username}",
        "Gravatar": f"https://en.gravatar.com/{username}",
        "HackerRank": f"https://www.hackerrank.com/{username}",
        "Houzz": f"https://www.houzz.com/user/{username}",
        "IMDb": f"https://www.imdb.com/user/{username}",
        "Instructables": f"https://www.instructables.com/member/{username}",
        "Issuu": f"https://issuu.com/{username}",
        "Kik": f"https://kik.me/{username}",
        "Last.fm": f"https://www.last.fm/user/{username}",
        "Lynda": f"https://www.lynda.com/profile/{username}",
        "Minds": f"https://www.minds.com/{username}",
        "Mixcloud": f"https://www.mixcloud.com/{username}",
        "Myspace": f"https://myspace.com/{username}",
        "OkCupid": f"https://www.okcupid.com/profile/{username}",
        "Patreon": f"https://www.patreon.com/{username}",
        "Periscope": f"https://www.pscp.tv/{username}",
        "Photobucket": f"https://photobucket.com/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Quora": f"https://www.quora.com/profile/{username}",
        "ReverbNation": f"https://www.reverbnation.com/{username}",
        "Roblox": f"https://www.roblox.com/user.aspx?username={username}",
        "ScholarGoogle": f"https://scholar.google.com/citations?user={username}",
        "Skillshare": f"https://www.skillshare.com/user/{username}",
        "Slack": f"https://{username}.slack.com",
        "Slideshare": f"https://www.slideshare.net/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "StackExchange": f"https://stackexchange.com/users/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "Strava": f"https://www.strava.com/athletes/{username}",
        "Tumblr": f"https://{username}.tumblr.com",
        "Twitch": f"https://www.twitch.tv/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Uber": f"https://www.uber.com/profile/{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "VK": f"https://vk.com/{username}",
        "Weibo": f"https://weibo.com/{username}",
        "Wikipedia": f"https://en.wikipedia.org/wiki/User:{username}",
        "WordPress": f"https://{username}.wordpress.com",
        "XING": f"https://www.xing.com/profile/{username}",
        "Yelp": f"https://www.yelp.com/user_details?userid={username}",
        "YouTube": f"https://www.youtube.com/{username}",
        "Zillow": f"https://www.zillow.com/profile/{username}",
    }

    print(Colorate.Horizontal(Colors.green_to_blue, f"\nChecking usernames for '{username}'...\n"))

    found_any = False
    for site, url in sites.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(Colorate.Horizontal(Colors.green_to_blue, f"[+] {site}: {url}"))
                found_any = True
            else:
                print(Colorate.Horizontal(Colors.red_to_black, f"[-] {site}: {url}"))
        except requests.RequestException:
            print(Colorate.Horizontal(Colors.red_to_black, f"[-] {site}: {url}"))

    if not found_any:
        print(Colorate.Horizontal(Colors.red_to_black, "\nNo valid profile found"))

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_menu()
        user = input(Colorate.Horizontal(Colors.green_to_blue, "\nName >> ")).strip()
        if user == "0":
            print(Colorate.Horizontal(Colors.green_to_blue, "\n\n"))
            time.sleep(1)
            break
        elif user:
            os.system('cls' if os.name == 'nt' else 'clear')
            print_menu()
            username(user)
            input(Colorate.Horizontal(Colors.green_to_blue, "\n"))
        else:
            print(Colorate.Horizontal(Colors.red_to_black, "\nNo name entered"))
            time.sleep(1)

if __name__ == "__main__":
    main()
