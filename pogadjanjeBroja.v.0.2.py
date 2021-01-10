#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'pogadjanjeBroja.py'
__version__ = '0.2'
__site__ = 'pythonbytes.rs'

import random
import sys
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

print('\nDobrodosli u igru pogadjanje broja v.0.2')
print('Cilj igre je da osvojite 50 poena')
print('Kako bi izasli iz igre unesite sledeci broj: 99')
poeni = 0

while True:
    broj = random.randint(0, 10)
    pogodi = int(input('\nPogodi broj izmedju 0 i 10: '))

    if pogodi is 99:
        exit('\nHvala vam sto ste igrali ovu igru!')

    if pogodi > 10 or pogodi < 0:
        print('[!] Broj ne sme da bude manji od nule ili veci od deset')



    if pogodi is broj:
        print('[+] Svaka cast, pogodio si broj!')
        poeni += 10
        print('[+] Ukupan broj osvojenih poena: ', poeni)
        if poeni == 50:
            exit('[!] Svaka cast! Dosli ste do 50 poena! Hvala vam sto ste igrali ovu igru!')

    else:
        print('[-] Nisi pogodio broj! Broj je bio: ', broj)