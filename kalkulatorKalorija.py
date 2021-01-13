#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'kalkulatorKalorija.py'
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

def BMI(kilaza, visina):
    return float(kilaza / ((visina/100)**2))

def BMR(godine, kilaza, visina, pol):
    if pol in ['M', 'm']:
        ritamBM = ((10 * kilaza) + (6.25 * visina) - (5 * godine) + 5)
    else:
        ritamBM = ((10 * kilaza) + (6.25 * visina) - (5 * godine) - 161)

    return ritamBM

def TDEE(koeficijent_aktivnosti):
    return round(BMR(godine, kilaza, visina, pol) * koeficijent_aktivnosti)

def GUBLJENJE_KILAZE(koeficijent_aktivnosti, procenat = 0.2):
    return round(TDEE(koeficijent_aktivnosti) * (1 - procenat))

def DOBIJANJE_KILAZE(koeficijent_aktivnosti, procenat = 0.2):
    return round(TDEE(koeficijent_aktivnosti) * (1 + procenat))

def UNOS_PROTEINA(kilaza, grama_po_kg=2.2):
    return round(kilaza * grama_po_kg)

def INDEX_TM(indexTM):
    if float(indexTM) < 19:
        return ('[-] Prema Indeksu telesne mase(BMI) imate manjak kilograma!')

    if float(indexTM) > 19 and float(indexTM) < 25:
        return ('[+] Prema Indeksu telesne mase(BMI) imate normalnu tezinu!')

    if float(indexTM) > 25 and float(indexTM) < 30:
        return ('[-] Prema Indeksu telesne mase(BMI) imate visak kilograma!\n[+] Medjutim to ne vazi ako ste atleta i ako imate nizak procenat masti!')

    if float(indexTM) > 30 and float(indexTM) < 39:
        return ('[!] Prema Indeksu telesne mase(BMI) vi ste GOJAZNI!\n[+] Medjutim to ne vazi ako ste atleta i ako imate nizak procenat masti!')

    if float(indexTM) > 39:
        return ('[!] Prema Indeksu telesne mase(BMI) vi ste JAKO GOJAZNI!')




if __name__ == "__main__":
    print('\n[+] Dobrodosli u kalkulator kalorija!')
    print('[+] Pokusacemo da vam izracunamo potrebne kalorije na dnevnom nivou, u zavisnosti od vaseg cilja i aktivnosti!')
    print('[!] Ovaj program sluzi samo za edukativne svrhe. Koristite ga na sopstvenu odgovornost!')

    godine = int(input('\n[+] Unesite vase godine: '))
    if godine < 18:
        exit('[!] Imate manje od 18 godina.')
    pol = str(input('[+] Unesite vas pol (M ili m za muski, Z ili z za zenski): '))
    if pol not in ['M', 'm', 'Z', 'z']:
        print('[-] Molimo vas unesite slovo M ili Z !')
        exit()

    kilaza = float(input('[+] Unesite koliko imate kg: '))
    visina = float(input('[+] Unesite visinu u cm: '))

    aktivnost = float(input('''\n[+] Ispod se nalazi opis  aktivnosti i njihov koeficijent:
    
    1.2 - Sedeci: Malo ili bez fizicke aktivnosti.
    1.3 - Lakse Aktivni: Lake vezbe ili aktivnost 1-3 dana u toku nedelje. 
    1.5 - Srednje Aktivni: Srednje vezbe ili aktivnost 3-5 dana u toku nedelje.
    1.7 - Veoma Aktivni: Teske vezbe ili aktivnost 6-7 dana u toku nedelje.
    1.9 - Ekstremno Aktivni: Teske vezbe svakodnevno ili aktivnost i fizicki posao.
    
    Unesiti broj ispred opisa aktivnosti u tabli iznad(Vrednost mora biti tacno upisana): '''))

    if aktivnost not in [1.2, 1.3, 1.5, 1.7, 1.9]:
        print('\n[-] Niste pravilno upisali vrednost za aktivnost!')
        exit()

    print(f'\n[+] Vas Indeks Telesne Mase(BMI) je: {BMI(kilaza, visina):.2f}')
    print(INDEX_TM(f'{BMI(kilaza, visina):.2f}'))

    if aktivnost == 1.2:
        print('\n[!] Prema opciji koju ste izabrali, vi ste slabo aktivna osoba!!')
        print('[+] Povecana aktivnost moze da vam poboljsa zdravlje i da vam ubrza proces gubljenja masnih naslaga.')


    cilj = input('''\n[+] Ispod vam se nalaze opcije u zavisnosti od vaseg cilja:
    
    I ili i - Zelim da ostanem na istoj kilazi.
    G ili g - Zelim da izgubim kilazu.
    D ili d - Zelim da dobijem kilazu.
    
    Izaberite jednu od opcija(I, i, G, g, D, d): ''')

    if cilj not in ['I', 'i', 'G', 'g', 'D', 'd']:
        print('\n[-] Niste pravilno odabrali vas cilj!')
        exit()

    if cilj == 'I' or cilj == 'i':
        print(f'\n[+] Potrebno vam je {TDEE(aktivnost)} kalorija kako bi odrzavali trenutnu kilazu.')
        print(f'\n[+] Potrebno je da unesete {UNOS_PROTEINA(kilaza)} grama proteina po danu.')
        print(f'[+] Broj kalorija iz {UNOS_PROTEINA(kilaza)} grama proteina je: {UNOS_PROTEINA(kilaza) * 4} kcal.')
        print(f'[+] Ostalih {TDEE(aktivnost) - UNOS_PROTEINA(kilaza) * 4} kcal, mozete uneti kroz masti i ugljene hidrate.')
        print(f'\n[+] Predlog kako da raspodelite makro nutrijente:')
        print(f'[+] Proteini: {UNOS_PROTEINA(kilaza)} grama po danu.')
        print(f'[+] Masti: 45 grama po danu. ')
        print(f'[+] Ugljeni hidrati: {(TDEE(aktivnost) - UNOS_PROTEINA(kilaza) * 4 - 45 * 9) / 4} grama po danu.')

    if cilj == 'G' or cilj == 'g':
        print(f'\n[+] Potrebno vam je {GUBLJENJE_KILAZE(aktivnost)} kalorija kako bi gubili kilazu.')
        print(f'\n[+] Potrebno je da unesete {UNOS_PROTEINA(kilaza)} grama proteina po danu.')
        print(f'[+] Broj kalorija iz {UNOS_PROTEINA(kilaza)} grama proteina je: {UNOS_PROTEINA(kilaza) * 4} kcal.')
        print(f'[+] Ostalih {GUBLJENJE_KILAZE(aktivnost) - UNOS_PROTEINA(kilaza) *4} kcal, mozete uneti kroz masti i ugljene hidrate.')
        print(f'\n[+] Predlog kako da raspodelite makro nutrijente:')
        print(f'[+] Proteini: {UNOS_PROTEINA(kilaza)} grama po danu.')
        print(f'[+] Masti: 45 grama po danu. ')
        print(f'[+] Ugljeni hidrati: {(GUBLJENJE_KILAZE(aktivnost) - UNOS_PROTEINA(kilaza) * 4 - 45 * 9) / 4} grama po danu.')

    if cilj == 'D' or cilj == 'd':
        print(f'\n[+] Potrebno vam je {DOBIJANJE_KILAZE(aktivnost)} kalorija kako bi dobijali kilazu.')
        print(f'\n[+] Potrebno je da unesete {UNOS_PROTEINA(kilaza)} grama proteina po danu.')
        print(f'[+] Broj kalorija iz {UNOS_PROTEINA(kilaza)} grama proteina je: {UNOS_PROTEINA(kilaza) * 4} kcal.')
        print(f'[+] Ostalih {DOBIJANJE_KILAZE(aktivnost) - UNOS_PROTEINA(kilaza) * 4} kcal, mozete uneti kroz masti i ugljene hidrate.')
        print(f'\n[+] Predlog kako da raspodelite makro nutrijente:')
        print(f'[+] Proteini: {UNOS_PROTEINA(kilaza)} grama po danu.')
        print(f'[+] Masti: 45 grama po danu. ')
        print(f'[+] Ugljeni hidrati: {(DOBIJANJE_KILAZE(aktivnost) - UNOS_PROTEINA(kilaza) * 4 - 45 * 9) / 4} grama po danu.')







