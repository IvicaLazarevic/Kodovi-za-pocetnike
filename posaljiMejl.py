#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'posaljiMejl.py'
__version__ = '0.1'
__site__ = 'pythonbytes.rs'

import sys
import ssl
import smtplib
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

VAS_MEJL = 'OVDE UPISATI MEJL' # Ovde upisati MEJL u koji se logujete
VASA_LOZINKA = 'OVDE UPISATI LOZINKU'          # Ovde upisati LOZINKU od mejla u koji se logujete

SMTP_SERVER = 'OVDE UPISATI SMTP SERVER'     # Ovde upisati vas SMTP server. Na primer smtp.gmail.com
SMTP_PORT = 465                         # Ovde upisati port od SMTP servera. Na primer 465
NASLOV_PORUKE = 'Slanje mejla pomocu Python jezika'  # Ovde upisati ono sto ide pod SUBJECT kada kreirate mejl
TEKST_PORUKE = 'Poruka je uspesno poslata!!!' # Ovde upisati sadrzaj poruke koji zelite da posaljete
MEJL_PRIMAOCA = 'OVDE UPISATI MEJL PRIMAOCA'   # Ovde upisati mejl na koji zelite da posaljete poruku

CEO_MEJL = f'''\
From: {VAS_MEJL}
To: {MEJL_PRIMAOCA}
Subject: {NASLOV_PORUKE}

{TEKST_PORUKE}'''

provera = input(f'''\n[+]  Proverite da li su ispravni sledeci podaci:

SMTP Server = {SMTP_SERVER}
SMTP Port ={SMTP_PORT}
Vas Mejl = {VAS_MEJL}
Vasa Lozinka = {VASA_LOZINKA}
Mejl Primaoca = {MEJL_PRIMAOCA}
Naslov Poruke = {NASLOV_PORUKE}
Tekst Poruke = {TEKST_PORUKE}

[!] Da li zelite da posaljete mejl sa sledecim podacima? (y/n): ''')

if provera not in ['y', 'n']:
    exit('[-] Molimo vas ukucajte y za potvrdu slanja ili n za otkazivanje slanja mejla.')

if provera == 'n':
    exit('[-] Otkazali ste slanje mejla!')


with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=ssl.create_default_context()) as smtpServer:
    try:
        smtpServer.login(VAS_MEJL, VASA_LOZINKA)
        smtpServer.sendmail(VAS_MEJL, MEJL_PRIMAOCA, CEO_MEJL)
    except smtplib.SMTPAuthenticationError:
        print('\n[-] Doslo je do greske. Molimo vas proverite vas mejl i vasu lozinku!')
        exit()

print('\n[+] Mejl uspesno poslat!')