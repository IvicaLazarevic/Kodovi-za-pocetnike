#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'jednostavniPrimeri.py'
__version__ = '0.1'
__site__ = 'pythonbytes.rs'

import sys
import calendar
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

def prestupnaGodina(godina):
    prestupnagodina = calendar.isleap(godina)
    if prestupnagodina:
        print(f'[+] Godina {godina} je prestupna godina!')
    else:
        print(f'[-] Godina {godina} nije prestupna godina!')

if __name__ == '__main__':
    print('\n[+] Dobrodosli u skriptu koja vam kao rezultat daje da li je godina prestupna ili ne')
    godina = int(input('\n[+] Molimo vas unesiti godinu koju zelite da proverite: '))

    prestupnaGodina(godina)