#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = '7zKreker.py'
__version__ = '0.1'
__site__ = 'pythonbytes.rs'

import sys
from subprocess import call

try:
    from py7zr import SevenZipFile
    from colorama import Fore
except:
    call('pip3 install colorama py7zr', shell=True)
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

print('\n[+] Ovo je skripta koja pokusava da pogodi lozinku od .7z arhiviranog fajla!')
FAJL = input('\n[+] Molimo vas unesite ime fajla koji zelite da krekujete: ')
LOZINKE = input('[+] Molimo vas unesite ime fajla sa lozinkama: ')



def krekovanje7z(lozinka):
    try:
        SevenZipFile(FAJL, mode='r', password=lozinka).extractall()
        return lozinka
    except(KeyboardInterrupt):
        exit('[-] Izlazak iz skripte!')
    except:
        return


with open(LOZINKE, 'r') as lozinke:
    for lozinka in lozinke.readlines():
        lozinka = lozinka.strip('\n')
        pogodak = krekovanje7z(lozinka)
        if pogodak:
            exit(f'\n[+] Lozinka je pogodjena: {lozinka}')
        else:
            pass
    print('\n[-] Lozinka nije pogodjena. Probajte drugi recnik!')
