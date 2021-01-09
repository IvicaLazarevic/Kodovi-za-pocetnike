#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'kalkulator.py'
__version__ = '0.1'
__site__ = 'pythonbytes.rs'

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

def kalkulator(rezultat):
    print('Vaš rezultat je: ', rezultat)

print('\nOvo je jednostavan kalkulator')
print('\nAko želite da saberete dva broja, izaberite opciju  : 1')
print('Ako želite da oduzmete dva broja, izaberite opciju  : 2')
print('Ako želite da pomnožite dva broja, izaberite opciju : 3')
print('Ako želite da podelite dva broja, izaberite opciju  : 4')

opcija = int(input('\nOdaberite opciju: '))

if opcija == 1:
    prviBroj = int(input('\nUnesite prvi broj: '))
    drugiBroj = int(input('Unesite drugi broj: '))
    zbir = prviBroj + drugiBroj
    kalkulator(zbir)

if opcija == 2:
    prviBroj = int(input('\nUnesite prvi broj: '))
    drugiBroj = int(input('Unesite drugi broj: '))
    oduzimanje = prviBroj - drugiBroj
    kalkulator(oduzimanje)

if opcija == 3:
    prviBroj = int(input('\nUnesite prvi broj: '))
    drugiBroj = int(input('Unesite drugi broj: '))
    množenje = prviBroj * drugiBroj
    kalkulator(množenje)

if opcija == 4:
    prviBroj = int(input('\nUnesite prvi broj: '))
    drugiBroj = int(input('Unesite drugi broj: '))
    deljenje = prviBroj / drugiBroj
    kalkulator(deljenje)
