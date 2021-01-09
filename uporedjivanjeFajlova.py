#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'uporedjivanjeFajlova.py'
__version__ = '0.2'
__site__ = 'pythonbytes.rs'

import sys
from subprocess import call
from difflib import SequenceMatcher

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

prviFajl = input('\nUnesite ime prvog fajla: ')
drugiFajl = input('Unesite ime drugog fajla: ')

with open(prviFajl) as prviF, open(drugiFajl) as drugiF:
    slicnostTeksta = SequenceMatcher(None, prviF.read(), drugiF.read()).ratio() * 100
    print(f'\nSlicnost izmedju ova dva fajla je {slicnostTeksta:.2f} %')

