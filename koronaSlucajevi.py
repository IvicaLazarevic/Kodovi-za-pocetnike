#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'koronaSlucajevi.py'
__version__ = '0.1'
__site__ = 'pythonbytes.rs'

import sys
from subprocess import call

try:
    import requests
    from colorama import Fore
except:
    call('pip3 install colorama requests', shell=True)
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

COVID_STATISTIKA = requests.get('https://api.covid19api.com/summary').json()


def globalno():
    print('\n[+] Statiskika na globalnom nivou:')
    print(f'\n[+] Prijavljeni novi slucajevi na globalnom nivou: {COVID_STATISTIKA["Global"]["NewConfirmed"]}')
    print(f'[+] Ukupno prijavljeno na globalnom nivou: {COVID_STATISTIKA["Global"]["TotalConfirmed"]}')
    print(f'[+] Prijavljeni novi slucajevi sa smrtnim ishodom: {COVID_STATISTIKA["Global"]["NewDeaths"]}')
    print(f'[+] Ukupno prijavljeno smrtnih slucajeva na globalnom nivou: {COVID_STATISTIKA["Global"]["TotalDeaths"]}')
    print(f'[+] Prijavljen broj novih pacijenata koji su se oporavili: {COVID_STATISTIKA["Global"]["NewRecovered"]}')
    print(f'[+] Ukupno prijavljeno pacijenata koji su se oporavili na globalnom nivou: {COVID_STATISTIKA["Global"]["TotalRecovered"]}')

def srbija():
    SRBIJA = COVID_STATISTIKA['Countries']
    SRB = SRBIJA[151]['Country']
    print(f'\n[+] Statistika za drzavu {SRB} na datum {SRBIJA[151]["Date"]}')
    print(f'\n[+] Prijavljeni novi slucajevi: {SRBIJA[151]["NewConfirmed"]}')
    print(f'[+] Ukupno prijavljeno slucajeva: {SRBIJA[151]["TotalConfirmed"]}')
    print(f'[+] Prijavljeni novi slucajevi sa smrtnim ishodom: {SRBIJA[151]["NewDeaths"]}')
    print(f'[+] Ukupno prijavljeno smrtnih slucajeva: {SRBIJA[151]["TotalDeaths"]}')
    print(f'[+] Prijavljen broj novih pacijenata koji su se oporavili: {SRBIJA[151]["NewRecovered"]}')
    print(f'[+] Ukupno prijavljeno pacijenata koji su se oporavili: {SRBIJA[151]["TotalRecovered"]}')

def BiH():
    BiH = COVID_STATISTIKA['Countries']
    BIH = BiH[21]['Country']
    print(f'\n[+] Statistika za drzavu {BIH} na datum {BiH[21]["Date"]}')
    print(f'\n[+] Prijavljeni novi slucajevi: {BiH[21]["NewConfirmed"]}')
    print(f'[+] Ukupno prijavljeno slucajeva: {BiH[21]["TotalConfirmed"]}')
    print(f'[+] Prijavljeni novi slucajevi sa smrtnim ishodom: {BiH[21]["NewDeaths"]}')
    print(f'[+] Ukupno prijavljeno smrtnih slucajeva: {BiH[21]["TotalDeaths"]}')
    print(f'[+] Prijavljen broj novih pacijenata koji su se oporavili: {BiH[21]["NewRecovered"]}')
    print(f'[+] Ukupno prijavljeno pacijenata koji su se oporavili: {BiH[21]["TotalRecovered"]}')

def hrvatska():
    HRVATSKA = COVID_STATISTIKA['Countries']
    CRO = HRVATSKA[41]['Country']
    print(f'\n[+] Statistika za drzavu {CRO} na datum {HRVATSKA[41]["Date"]}')
    print(f'\n[+] Prijavljeni novi slucajevi: {HRVATSKA[41]["NewConfirmed"]}')
    print(f'[+] Ukupno prijavljeno slucajeva: {HRVATSKA[41]["TotalConfirmed"]}')
    print(f'[+] Prijavljeni novi slucajevi sa smrtnim ishodom: {HRVATSKA[41]["NewDeaths"]}')
    print(f'[+] Ukupno prijavljeno smrtnih slucajeva: {HRVATSKA[41]["TotalDeaths"]}')
    print(f'[+] Prijavljen broj novih pacijenata koji su se oporavili: {HRVATSKA[41]["NewRecovered"]}')
    print(f'[+] Ukupno prijavljeno pacijenata koji su se oporavili: {HRVATSKA[41]["TotalRecovered"]}')

def crnagora():
    CRNA_GORA = COVID_STATISTIKA['Countries']
    CG = CRNA_GORA[115]['Country']
    print(f'\n[+] Statistika za drzavu {CG} na datum {CRNA_GORA[115]["Date"]}')
    print(f'\n[+] Prijavljeni novi slucajevi: {CRNA_GORA[115]["NewConfirmed"]}')
    print(f'[+] Ukupno prijavljeno slucajeva: {CRNA_GORA[115]["TotalConfirmed"]}')
    print(f'[+] Prijavljeni novi slucajevi sa smrtnim ishodom: {CRNA_GORA[115]["NewDeaths"]}')
    print(f'[+] Ukupno prijavljeno smrtnih slucajeva: {CRNA_GORA[115]["TotalDeaths"]}')
    print(f'[+] Prijavljen broj novih pacijenata koji su se oporavili: {CRNA_GORA[115]["NewRecovered"]}')
    print(f'[+] Ukupno prijavljeno pacijenata koji su se oporavili: {CRNA_GORA[115]["TotalRecovered"]}')

def makedonija():
    MAKEDONIJA = COVID_STATISTIKA['Countries']
    MK = MAKEDONIJA[101]['Country']
    print(f'\n[+] Statistika za drzavu {MK} na datum {MAKEDONIJA[101]["Date"]}')
    print(f'\n[+] Prijavljeni novi slucajevi: {MAKEDONIJA[101]["NewConfirmed"]}')
    print(f'[+] Ukupno prijavljeno slucajeva: {MAKEDONIJA[101]["TotalConfirmed"]}')
    print(f'[+] Prijavljeni novi slucajevi sa smrtnim ishodom: {MAKEDONIJA[101]["NewDeaths"]}')
    print(f'[+] Ukupno prijavljeno smrtnih slucajeva: {MAKEDONIJA[101]["TotalDeaths"]}')
    print(f'[+] Prijavljen broj novih pacijenata koji su se oporavili: {MAKEDONIJA[101]["NewRecovered"]}')
    print(f'[+] Ukupno prijavljeno pacijenata koji su se oporavili: {MAKEDONIJA[101]["TotalRecovered"]}')

if __name__ == "__main__":
    globalno()
    srbija()
    BiH()
    hrvatska()
    crnagora()
    makedonija()

