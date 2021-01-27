#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'ipInformacije.py'
__version__ = '0.1'
__site__ = 'pythonbytes.rs'

import sys
import re
import json
from urllib import request
from subprocess import call

try:
    from colorama import Fore
except:
    call('pip3 install colorama', shell=True)
    exit()


def logo():
    print(Fore.RED+"\n       __           __        ____      __        ")
    print(Fore.RED+"  ____/ /___ ______/ /_______/ __ \____/ /__  _____ ")
    print(Fore.RED+" / __  / __ `/ ___/ //_/ ___/ / / / __  / _ \/ ___/ ")
    print(Fore.RED+"/ /_/ / /_/ / /  / ,< / /__/ /_/ / /_/ /  __/ /     ")
    print(Fore.RED+"\__,_/\__,_/_/  /_/|_|\___/\____/\__,_/\___/_/      ")
    print(Fore.RED+"                                                \n")
    print(Fore.RED+'                               Naziv: '+ __scriptName__)
    print(Fore.RED+'                               Verzija: '+ __version__)
    print(Fore.RED+'                               Koder: '+ __coder__)
    print(Fore.RED+ '                               Sajt: ' + __site__+Fore.WHITE)

if sys.platform == 'linux' or sys.platform == 'linux2' or sys.platform == 'darwin':
    call('clear', shell=True)
    logo()
else:
    call('cls', shell=True)
    logo()


CHECK_IP = 'http://checkip.dyndns.com/'
CHECK_IP_LOCATION = 'http://ipinfo.io/'

VAS_IP = re.search(r'(\d+.\d+.\d+.\d+)', str(request.urlopen(CHECK_IP).read())).group()

ODGOVOR = request.urlopen(url=CHECK_IP_LOCATION+VAS_IP+'/json')
PODACI = json.load(ODGOVOR)


print(f'\n[+] Vasa IP adresa je: {VAS_IP} ')
print(f'[+] Vas hostname: {PODACI["hostname"]}')
print(f'[+] Zemlja kojoj pripada IP adresa: {PODACI["country"]}')
print(f'[+] Lokacija IP adrese: {PODACI["city"]}')
print(f'[+] Region: {PODACI["region"]}')
print(f'[+] Vas provajder: {PODACI["org"]}')
print(f'[+] Geografska sirina i duzina: {PODACI["loc"]}')