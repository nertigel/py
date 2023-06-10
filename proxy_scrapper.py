from asyncio.windows_events import NULL
from os import system
from colorama import Fore, Back, Style
import requests

total_scrapped = 0
export_to_csv = False
remove_duplicates = True

def scrape_http():
    with open('output-http.txt', 'a') as file:
        collected_socks = []
        idx = 1
        TheSpeedX = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt')
        for key, value in enumerate(TheSpeedX.iter_lines()):
            collected_socks.insert(idx, value)
            idx += 1
        
        jetkai = requests.get('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt')
        for key, value in enumerate(jetkai.iter_lines()):
            collected_socks.insert(idx, value)
            idx += 1
        
        MuRongPIG = requests.get('https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt')
        for key, value in enumerate(MuRongPIG.iter_lines()):
            collected_socks.insert(idx, value)
            idx += 1
        
        prxchk = requests.get('https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt')
        for key, value in enumerate(prxchk.iter_lines()):
            collected_socks.insert(idx, value)
            idx += 1
        
        KangProxy = requests.get('https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt')
        for key, value in enumerate(KangProxy.iter_lines()):
            collected_socks.insert(idx, value)
            idx += 1
        
        HyperBeats = requests.get('https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt')
        for key, value in enumerate(HyperBeats.iter_lines()):
            collected_socks.insert(idx, value)
            idx += 1

        global remove_duplicates
        if remove_duplicates:
            collected_socks = list(dict.fromkeys(collected_socks))
        
        for key, value in enumerate(collected_socks):
            file.write(value.decode() + "\n")

        global total_scrapped
        total_scrapped += idx
        print(f"Scraped {idx} Socks4 proxies!\nSaved to file!")
        main()
    return

def scrape_socks4():
    with open('output-socks4.txt', 'a') as file:
        collected_socks = []
        idx = 1
        TheSpeedX = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt')
        for key, value in enumerate(TheSpeedX.iter_lines()):
            collected_socks.insert(idx, value)
            idx += 1
        
        jetkai = requests.get('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt')
        for key, value in enumerate(jetkai.iter_lines()):
            collected_socks.insert(idx, value)
            idx += 1
        
        MuRongPIG = requests.get('https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks4.txt')
        for key, value in enumerate(MuRongPIG.iter_lines()):
            collected_socks.insert(idx, value)
            idx += 1
        
        prxchk = requests.get('https://raw.githubusercontent.com/prxchk/proxy-list/main/socks4.txt')
        for key, value in enumerate(prxchk.iter_lines()):
            collected_socks.insert(idx, value)
            idx += 1
        
        KangProxy = requests.get('https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks4/socks4.txt')
        for key, value in enumerate(KangProxy.iter_lines()):
            collected_socks.insert(idx, value)
            idx += 1
        
        HyperBeats = requests.get('https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt')
        for key, value in enumerate(HyperBeats.iter_lines()):
            collected_socks.insert(idx, value)
            idx += 1

        global remove_duplicates
        if remove_duplicates:
            collected_socks = list(dict.fromkeys(collected_socks))
        
        for key, value in enumerate(collected_socks):
            file.write(value.decode() + "\n")

        global total_scrapped
        total_scrapped += idx
        print(f"Scraped {idx} Socks4 proxies!\nSaved to file!")
        main()
    return

def scrape_socks5():
    with open('output-socks5.txt', 'a') as file:
        collected_socks = []
        idx = 1
        TheSpeedX = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt')
        for key, value in enumerate(TheSpeedX.iter_lines()):
            collected_socks.insert(idx, value)
            idx += 1
        
        jetkai = requests.get('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt')
        for key, value in enumerate(jetkai.iter_lines()):
            collected_socks.insert(idx, value)
            idx += 1
        
        MuRongPIG = requests.get('https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt')
        for key, value in enumerate(MuRongPIG.iter_lines()):
            collected_socks.insert(idx, value)
            idx += 1
        
        prxchk = requests.get('https://raw.githubusercontent.com/prxchk/proxy-list/main/socks5.txt')
        for key, value in enumerate(prxchk.iter_lines()):
            collected_socks.insert(idx, value)
            idx += 1
        
        KangProxy = requests.get('https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks5/socks5.txt')
        for key, value in enumerate(KangProxy.iter_lines()):
            collected_socks.insert(idx, value)
            idx += 1
        
        HyperBeats = requests.get('https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt')
        for key, value in enumerate(HyperBeats.iter_lines()):
            collected_socks.insert(idx, value)
            idx += 1

        global remove_duplicates
        if remove_duplicates:
            collected_socks = list(dict.fromkeys(collected_socks))
        
        for key, value in enumerate(collected_socks):
            file.write(value.decode() + "\n")

        global total_scrapped
        total_scrapped += idx
        print(f"Scraped {idx} Socks4 proxies!\nSaved to file!")
        main()
    return

def display_info():
    print(Fore.YELLOW + "███████████████████████████████████████████")
    print(Fore.YELLOW + "█─▄▄▄▄█─▄▄▄─█▄─▄▄▀██▀▄─██▄─▄▄─█▄─▄▄─█▄─▄▄▀█")
    print(Fore.YELLOW + "█▄▄▄▄─█─███▀██─▄─▄██─▀─███─▄▄▄██─▄█▀██─▄─▄█")
    print(Fore.YELLOW + "▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀")
    print(Style.RESET_ALL + "All proxies are taken from public sources available on the internet.")
    print(Fore.LIGHTBLUE_EX + "Made by Nertigel\ngithub.com/nertigel")

    global total_scrapped
    print(Fore.LIGHTGREEN_EX + f"Scraped: {total_scrapped}")

    print(Style.RESET_ALL)
    return

def display_options():
    system("cls")
    display_info()

    print(Fore.LIGHTRED_EX + "[1] " + Style.RESET_ALL + "Scrape HTTP")
    print(Fore.LIGHTRED_EX + "[2] " + Style.RESET_ALL + "Scrape Socks4")
    print(Fore.LIGHTRED_EX + "[3] " + Style.RESET_ALL + "Scrape Socks5")
    print(Fore.LIGHTRED_EX + "[4] " + Style.RESET_ALL + "Scrape Socks5")
    print(Fore.LIGHTRED_EX + "[4] " + Style.RESET_ALL + "Settings")
    print(Fore.LIGHTRED_EX + "[5] " + Style.RESET_ALL + "Exit")

    return

def display_settings():
    system("cls")
    display_info()

    print(Fore.LIGHTRED_EX + "[1] " + Style.RESET_ALL + "Remove duplicates: " + str(remove_duplicates))
    print(Fore.LIGHTRED_EX + "[2] " + Style.RESET_ALL + "Export to .csv: " + str(export_to_csv))
    print(Fore.LIGHTRED_EX + "[3] " + Style.RESET_ALL + "Back")

    return

def main(skip=NULL):
    display_options()

    option = skip or int(input())
    if option == 1:
        scrape_http()
    elif option == 2:
        scrape_socks4()
    elif option == 3:
        scrape_socks5()
    elif option == 4:
        display_settings()

        setting_option = int(input())
        if setting_option == 1:
            global remove_duplicates
            yeet = remove_duplicates
            remove_duplicates = not yeet
            main(4)
        elif setting_option == 2:
            global export_to_csv
            yeet = export_to_csv
            export_to_csv = not yeet
            main(4)
        elif setting_option == 3:
            main()

    elif option == 5:
        exit()
    return

if __name__ == "__main__":
    main()