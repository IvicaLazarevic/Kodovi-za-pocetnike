#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'baciKockice.py'
__version__ = '0.1'
__site__ = 'pythonbytes.rs'

import sys
from random import randint, choice
from time import sleep as pauza
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

IGRACI = ['Ivan', 'Marko', 'Aca', 'Milos', 'Bojan', 'Borko', 'Zeljko', 'Sasa', 'Nina', 'Viki', 'Sandra', 'Ivana', 'Sneza']

def bacanjeKockica():
    UKUPNO_POENA = 0
    for kockica in range(6):
        POENI = randint(1, 6)
        print(f'[+] Kockica broj {kockica+1} donosi poena: {POENI}')
        UKUPNO_POENA += POENI
        pauza(1)
    print(f'\n[+] Ukupan zbir svih kockica je: {UKUPNO_POENA}')


if __name__ == '__main__':
    VASE_IME = input('\n[+] Molimo vas unesite vase ime: ')
    print(f'\n[+] Igrac {VASE_IME} baca kockice ...\n')
    bacanjeKockica()
    DRUGI_IGRAC = choice(IGRACI)
    print(f'\n[+] Vas protivnik {DRUGI_IGRAC} baca kockice ...\n')
    bacanjeKockica()