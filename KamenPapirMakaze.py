#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'KamenPapirMakaze.py'
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

def pobednik(prviIgrac, drugiIgrac):
    if prviIgrac == drugiIgrac:
        print('Nereseno!')

    elif prviIgrac == 'kamen':
        if drugiIgrac == 'makaze':
            print('Prvi igrac je pobedio!')
        else:
            print('Drugi igrac je pobedio!')

    elif prviIgrac == 'makaze':
        if drugiIgrac == 'papir':
            print('Prvi igrac je pobedio!')
        else:
            print('Drugi igrac je pobedio')

    elif prviIgrac == 'papir':
        if drugiIgrac == 'kamen':
            print('Prvi igrac je pobedio!')
        else:
            print('Drugi igrac je pobedio!')

    else:
        print('Molimo vas unesite sledece: kamen, makaze ili papir!')



print('\nUkucajte recima nesto od ponudjenih opcija:')
print('\n\tkamen ')
print('\tpapir')
print('\tmakaze')

prviIgrac = input('\nPrvi igrac: ')
drugiIgrac = input('Drugi igrac: ')
print(pobednik(prviIgrac, drugiIgrac))