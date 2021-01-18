#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'citanjePDF.py'
__version__ = '0.1'
__site__ = 'pythonbytes.rs'

import sys
from subprocess import call

try:
    from tqdm import trange
    import pyttsx3
    from PyPDF2 import PdfFileReader
    from colorama import Fore
except:
    call('pip3 install colorama PyPDF2 pyttsx3 tqdm', shell=True)
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

print('\n[+] Dobrodosli u skriptu koja otvara pdf fajl i cita ga!')

PDF_FAJL = input('[+] Unesite ime fajla u pdf formatu: ')

if PDF_FAJL[-4:] != '.pdf':
    exit('[-] Unesite pravilno naziv fajla koji se zavrsava sa .pdf!')

GLAS = input('[+] Molimo vas unesite M ako zelite muski glas ili unesite Z ako zelite zenski glas: ')
if GLAS not in ['Z', 'z', 'm', 'M']:
    exit('[-] Molimo vas pravilno unesite odabir za glas!')

if GLAS == 'M' or GLAS == 'm':
    GLAS = 0
else:
    GLAS = 1

BRZINA = input('[+] Molimo vas unesiti brzinu citanja [100 je sporo a 300 brzo]: ')

with open(PDF_FAJL, 'r+b') as fajl:
    print(f'[+] Ovaj pdf fajl ima {PdfFileReader(fajl).getNumPages()} stranica.')
    print('[+] Ucitavamo tekst i krecemo sa citanjem ...')
    zvucnik = pyttsx3.init()
    print(f'[+] Podesavamo novu vrednost za brzinu citanja ...')
    zvucnik.setProperty('rate', int(BRZINA))
    print(f'[+] Podesavamo glas ...\n')
    zvucnik.setProperty('voice', zvucnik.getProperty('voices')[GLAS].id)
    strana = 1
    for stranica in PdfFileReader(fajl).pages:
        for i in trange(PdfFileReader(fajl).getNumPages(), desc=f'[+] Citamo stranu broj: {strana}'):
            zvucnik.say(stranica.extractText())
            zvucnik.runAndWait()
            strana += 1
