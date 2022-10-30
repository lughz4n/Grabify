#!/bin/python3
#By: ZanderC0de

import os
import sys
import time
import platform
import requests
from bs4 import BeautifulSoup
from colorama import Fore, init, Back

init()


##########USE############
'''
EXAMPLE:
    link: https://grabify.link/PTRYUB
    "PTRYUB" IS THE CODE, THEN USE THE NEXT...
    ./Evade.py PTRYUB
'''

########FUNCTIONS########


def banner():

    text = """
  ▄████  ██▀███   ▄▄▄       ▄▄▄▄    ██▓  █████▒▓██   ██▓
 ██▒ ▀█▒▓██ ▒ ██▒▒████▄    ▓█████▄ ▓██▒▓██   ▒  ▒██  ██▒
▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄  ▒██▒ ▄██▒██▒▒████ ░   ▒██ ██░
░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██ ▒██░█▀  ░██░░▓█▒  ░   ░ ▐██▓░
░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒░▓█  ▀█▓░██░░▒█░      ░ ██▒▓░
 ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▒▓███▀▒░▓   ▒ ░       ██▒▒▒ 
  ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░▒░▒   ░  ▒ ░ ░       ▓██ ░▒░ 
░ ░   ░   ░░   ░   ░   ▒    ░    ░  ▒ ░ ░ ░     ▒ ▒ ░░  
      ░    ░           ░  ░ ░       ░           ░ ░     
                                 ░              ░ ░     
    """
    print(Fore.LIGHTRED_EX+text+"\n")


def clearD():

    os.system('clear')

def warn():

    os.system('curl ip-api.com -o .ipcur 2>/dev/null')

    print(Fore.GREEN+'The datas of your current IP is:')
    print(Fore.BLACK+'')
    os.system('cat .ipcur | grep "query"')
    os.system('cat .ipcur | grep "country"')
    os.system('cat .ipcur | grep "city"')
    os.remove('.ipcur')

    opc = input(Back.BLACK+Fore.LIGHTGREEN_EX+'\nDo you want continue? (y/n): ').lower()

    if 'y' in opc:
        pass
    else:
        exit(1)


def checkArg():

    global code

    try:

        code = sys.argv[1]
        code = code.upper()
        print(Fore.GREEN+'[+]Code typed')

    except:

        print(Fore.RED+'[-]Code not typed\n')
        print(Fore.YELLOW+'Use: ./Evade.py <<CODE>>')
        exit(1)

    if len(code) == 6:
        pass

    else:
        print(Fore.RED+'The code is bad, check again')
        exit(1)

    headers = {
        'User-Agent': 'VLC/3.0.18 LibVLC/3.0.18',
        'Referer': 'https://pornhub.com',
        'Forwarded': 'for=192.0.2.60; proto=http; by=203.0.113.43'
    }

    x = requests.get('https://grabify.link/'+code, headers=headers)

    if x.status_code != 200:
        print(Fore.LIGHTRED_EX+'Check again the code, there a error')
        exit(1)


def checkConnection():

    try:
        request = requests.get('https://google.com', timeout=4)
    except (requests.ConnectionError, requests.Timeout):
        print(Fore.RED+'[-]Not there connection to internet')
        exit(1)
    else:
        print(Fore.GREEN+'[+]There connection to internet')

def getFile():

    time.sleep(1)

    print(Fore.GREEN+'[+]Hiding the User Agent (Device,OS,ETC)')

    time.sleep(2)

    os.system('curl --header "Referer: https://xvideos.com" -A "Fsociety | Hello im Steve Jobs, ok?" https://grabify.link/'+code+' -o structure  2>/dev/null')

    response = os.popen('cat structure').read()

    os.remove('structure')

    soup = BeautifulSoup(response, 'html.parser')

    box = soup.find('head')

    link = box.find('title')

    link = str(link)

    link = link.replace('<title>Redirecting to', '')

    link = link.replace('</title>', '')


    if '<title>Just' in link:

        print(Fore.YELLOW+'[?]Oh! Maybe the link have Smart Logger')

        time.sleep(3)

        link2 = box.find('meta', {'name':'url'})

        link2 = str(link2)

        link2 = link2.replace('" name="url"/>', '')

        link2 = link2.replace('<meta content="', '')
	
        if 'http' in link2:
            print(Fore.GREEN+'[+]The Link has been evaded')
            print(Fore.LIGHTRED_EX+'\n--------------------------------------------')
            print(Fore.LIGHTGREEN_EX+'LINK ORIGIN: '+Fore.LIGHTMAGENTA_EX+link2)
            print(Fore.LIGHTRED_EX+'---------------------------------------------\n')
            exit(0)

        else:
            print(Fore.RED+"\nError, maybe you be using a VPN not compatible")
            print('The vpns that you can use is:')
            print(Fore.GREEN+'+VPNHUB\n+HOLAVPN\n?NordVPN')
            exit(1)

    else:
        print(Fore.GREEN+'[+]The Link has been evaded')
        print(Fore.LIGHTRED_EX+'\n---------------------------------------------')
        print(Fore.LIGHTGREEN_EX+'LINK ORIGIN: '+Fore.LIGHTMAGENTA_EX+link)
        print(Fore.LIGHTRED_EX+'---------------------------------------------\n')
        exit(0)

def main():

    #Check OS
    if platform.system() == "Windows":
        print(Fore.LIGHTRED_EX+'This programa is not for Windows')
        exit(1)

    clearD()

    #Print the banner
    banner()

    #Warning about VPN
    warn()

    #Clear display
    clearD()

    #Print banner
    banner()

    #Check if the code has been typed
    checkArg()

    #Check if there connection to internet
    checkConnection()

    #Start the extraction of link
    getFile()

if __name__ == '__main__':
    main()
