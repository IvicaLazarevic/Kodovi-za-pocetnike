#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'lotoigra.py'
__version__ = '0.1'
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


if sys.platform == 'linux' or sys.platform == 'linux2':
    call('clear', shell=True)
    logo()
elif sys.platform == 'darwin':
    call('clear', shell=True)
    logo()
else:
    call('cls', shell=True)
    logo()


def loto(sedmica):
    print(f'\nRandom generisana sedmica: {sedmica}')

    brojListica = 0
    brojTrojki = 0
    brojCetvorki = 0
    brojPetica = 0
    brojSestica = 0
    brojSedmica = 0
    randomListici = random.randint(450000, 500000)

    while brojListica < randomListici:

        listic = random.sample(range(1, 40), 7)
        listic.sort()
        #print(f'Random odigrani loto listic: {listic}')
        brojListica += 1

        for i in sedmica:
            hits = 0
            brojevi = []
            for a in listic:
                if a in sedmica:
                    hits += 1
                    brojevi.append(a)

            if hits == 3:
                #print(f'Pogodjeno {hits} broja. Kupljeni listic broj {brojListica}. Pogodjeni brojevi su: {brojevi}')
                brojTrojki += 1
                break

            if hits == 4:
                #print(f'Pogodjeno {hits} broja. Kupljeni listic broj {brojListica}. Pogodjeni brojevi su: {brojevi}')
                brojCetvorki += 1
                break

            if hits == 5:
                #print(f'Pogodjeno {hits} brojeva. Kupljeni listic broj {brojListica}. Pogodjeni brojevi su: {brojevi}')
                brojPetica += 1
                break

            if hits == 6:
                #print(f'Pogodjeno {hits} brojeva. Kupljeni listic broj {brojListica}. Pogodjeni brojevi su: {brojevi}')
                brojSestica += 1
                break
            if hits == 7:
                #print(f'Pogodjeno {hits} brojeva. Kupljeni listic broj {brojListica}. Pogodjeni brojevi su: {brojevi}')
                brojSedmica += 1
                break


    ukupnaUplata = brojListica * 80
    ukupnoTrojke = brojTrojki * 80
    ukupnoCetvorke = brojCetvorki * 80 * 10
    nakonTrojkiCetvorki = ukupnaUplata - ukupnoTrojke - ukupnoCetvorke
    ukupnoPetice = nakonTrojkiCetvorki / 4
    ukupnoSestice = nakonTrojkiCetvorki / 4
    ukupnoSedmica = nakonTrojkiCetvorki / 2
    ukupnoIsplaceno = ukupnoTrojke + ukupnoCetvorke + ukupnoPetice + ukupnoSestice + ukupnoSedmica

    #logo()
    #print(f'\nRandom generisana sedmica: {sedmica}')
    print(f'\nUkupan broj odigranih listica: {brojListica}')
    print(f'Ukupno uplaceno: {ukupnaUplata} dinara.')
    print(f'\nBroj pogodjenih trojki: {brojTrojki}')
    print(f'Ukupan dobitak na pogodjene trojke: {ukupnoTrojke} dinara.')
    print(f'Dobitak po listicu: {ukupnoTrojke / brojTrojki:.2f} dinara.')
    print(f'\nBroj pogodjenih cetvorki: {brojCetvorki}')
    print(f'Ukupan dobitak na pogodjene cetvorke: {ukupnoCetvorke} dinara.')
    print(f'Dobitak po listicu: {ukupnoCetvorke / brojCetvorki:.2f} dinara.')
    print(f'\nFond koji je ostao nakon isplata trojki i cetvorki: {nakonTrojkiCetvorki} dinara.')
    print(f'\nBroj pogodjenih petica: {brojPetica}')
    print(f'Ukupan dobitak na pogodjene petice: {ukupnoPetice}')
    print(f'Dobitak po listicu: {ukupnoPetice / brojPetica:.2f} dinara.')
    print(f'\nBroj pogodjenih sestica: {brojSestica}')
    print(f'Ukupan dobitak na pogodjene sestice: {ukupnoSestice:.2f}')
    print(f'Dobitak po listicu: {ukupnoSestice / brojSestica:.2f} dinara.')
    print(f'\nBroj pogodjenih sedmica: {brojSedmica}')
    print(f'Ukupan dobitat na pogodjene sedmice: {ukupnoSedmica:.2f}')
    if brojSedmica > 0:
        print(f'Dobitak po listicu: {ukupnoSedmica / brojSedmica:.2f} dinara.')
        print(f'\nUkupno isplaceno: {ukupnoIsplaceno} dinara.')
    else:
        print('Zao mi je, sedmica nije izvucena!!')
        print(f'\nUkupno isplaceno: {ukupnoIsplaceno - ukupnoSedmica:.2f} dinara.')

    print('\n\nNapomena: ovo je samo za zabavu, ne pokusavati u realnom zivotu. Nismo odgovorni za upotrebu skripte!')






if __name__ == "__main__":
    randomSedmica = random.sample(range(1, 40), 7)
    randomSedmica.sort()
    loto(randomSedmica)