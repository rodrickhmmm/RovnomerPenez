# Varování! Barvy se nezobrazujou ve starem cmd (od windows 10 a níž). Pro správné fungování se musí nainstalovat Microsoft Terminal z Microsoft Storu.

# importuješ moduly

import os
import gettext
import json
import sys
import time
from colorama import ansi
import pyautogui

# KONFIGURACE
try:
    with open("settings.json", 'r', encoding='utf-8') as file:
        settings = json.load(file)
    config = settings
except json.JSONDecodeError as e:
    print(f"Chyba při načítání JSON: {e}")
    config = {}

nazevvokna = config.get("nazevvokna", "Minecraft") # název okna, které má skript otevřít - v mém případě Feather Client, normálně by mělo být Minecraft <dopln si verzi>
player2BezKoncovky = config.get("player2BezKoncovky", "default_value") # jméno hráče 2 bez koncovky (pro lepší skloňování protože čeština lmao)
player2ek = config.get("player2ek", "default_value") # jméno hráče 2
player2nick = config.get("player2nick", "default_value") # nick hráče
symbol = config.get("symbol", "coin") # symbol měny
jazyk = config.get("jazyk", "cz") # jazyk/dialekt (cz, mo - moravština, br - brněnština, ba - brainrot dialekt)

# KONFIGURACE BAREV 
cervena = "\033[31;49;1m"
zluta = "\033[33;49;1m"
modra = '\033[34;49;1m'
zelena = "\033[32;49;1m"
bila = "\033[0m"


# FUNKCE ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# importace jazyka/dialektu
def importjazyka():
    with open("jazyky/"+ jazyk + ".json", 'r', encoding='utf-8') as file:
        translations = json.load(file)
    locals().update(translations)

    global nadpis, zpet, jazy, kalkulacka, p1penize, p2penizeovi, a, mocchudy, ty, matestejne, musisdat, ovi, timusidat, ckjmc, poslimechat, mcprikaz, chcescmddochatu, neumispsat, nenalezenookno, oknoaktivovano, nastaveni, vybrat, nenitu, zpatky, zmenajazyka

    nadpis = translations.get("nadpis", "Nadpis menu")
    kalkulacka = translations.get("kalkulacka", "Kalkulačka")
    p1penize = translations.get("p1penize", "Tvoje peníze: ")
    p2penizeovi = translations.get("p2penizeovi", "ovi peníze: ")
    a = translations.get("a", "a")
    mocchudy = translations.get("mocchudy", " jste moc chudý!!!!!!!")
    ty = translations.get("ty", "ty")
    matestejne = translations.get("matestejne", " seš piča? už máte stejně!!!!!!!")
    musisdat = translations.get("musisdat", "Musíš dát")
    ovi = translations.get("ovi", "ovi")
    timusidat = translations.get("timusidat", "ti musí dát")
    ckjmc = translations.get("ckjmc", "Počkej než se otevře minecraft...")
    poslimechat = translations.get("poslimechat", " posli mne ")
    mcprikaz = translations.get("mcprikaz", "Napiš do Minecraftu tento příkaz:")
    chcescmddochatu = translations.get("chcescmddochatu", "Chceš, abych to za tebe napsal do chatu?")
    neumispsat = translations.get("neumispsat", "Neumíš psát???? Zadej prosím 'y' nebo 'n'.")
    nenalezenookno = translations.get("nenalezenookno", "Okno s názvem '{nazevvokna}' nebylo nalezeno.")
    oknoaktivovano = translations.get("oknoaktivovano", "Okno '{nazevvokna}' bylo úspěšně aktivováno.")
    nastaveni = translations.get("nastaveni", "Nastavení")
    vybrat = translations.get("vybrat", "Vyber si: ")
    nenitu = translations.get("nenitu", "Neimplementováno")
    zpatky = translations.get("zpatky", "Zpět")
    zmenajazyka = translations.get("zmenajazyka", "Jazyk byl změněn na Češtinu.")
    jazy = translations.get("jazy", "Jazyky")
    zpet = translations.get("zpet", "Zpět")


importjazyka()

# deklarace var automatickynapsat

def automat():
    clear()
    global automatickynapsat
    automatickynapsat = None  # Inicializace jako None
    otazka = input(modra + chcescmddochatu + " [y/n] " + bila).strip().lower()
    
    if otazka == "y":
        automatickynapsat = True
    elif otazka == "n":
        automatickynapsat = False
    else:
        print(cervena + neumispsat + bila)
        automatickynapsat = None
        return automat()
        
# funkce na otevření mc
def otevritmc():
    try:
        windows = pyautogui.getWindowsWithTitle(nazevvokna)
        if not windows:
            raise ValueError(cervena + nenalezenookno)  # Vlastní chyba, pokud je seznam prázdný

        Mc = windows[0]
        Mc.activate()
        print(oknoaktivovano)

    except ValueError as e:
        print(e)  # Zobrazí vlastní zprávu při prázdném seznamu
    except IndexError:
        print(cervena + "Chyba: Pokus o přístup k neexistujícímu oknu.")
    except Exception as e:
        print(f"Neočekávaná chyba: {e}")

# menu jazyků
def jazyky():
    clear()
    print(modra + jazy + bila)
    print(zelena + "[1]" + bila, "Čeština")
    print(zelena + "[2]" + bila, "Moravština")
    print(zelena + "[3]" + bila, "Hantec")
    print(zelena + "[4]" + bila, "Brainrot spachtoš")
    print(zelena + "[5]" + cervena, zpet + bila) #type: ignore
    vyber = input(vybrat)
    global jazyk
    if vyber == "1":
        jazyk = "cz"
        importjazyka()
        print(cervena + zmenajazyka + bila)
        time.sleep(1)
        return main_menu()
    if vyber == "2":
        jazyk = "mo"
        importjazyka()
        print(cervena + zmenajazyka + bila)
        time.sleep(1)
        return main_menu()
    if vyber == "3":
        jazyk = "br"
        importjazyka()
        print(cervena + zmenajazyka + bila)
        time.sleep(1)
        return main_menu()
    if vyber == "4":
        jazyk = "ba"
        importjazyka()
        print(cervena + zmenajazyka + bila)
        time.sleep(1)
        return main_menu()
    if vyber == "5":
        return main_menu()
    else:
        print(neumispsat)
        return jazyky()

#MAIN MENU ------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main_menu():
    clear()
    while True:
        print(modra + nadpis + bila)
        print(zelena + "[1]" + bila, kalkulacka)
        print(zelena + "[2]" + bila, jazy)
        print(zelena + "[3]" + bila, "Themes")
        print(zelena + "[4]" + bila, nastaveni)
        print(zelena + "[5]" + bila, "Credits")
        print(zelena + "[6]" + cervena, "Exit" + bila)

        choice = input(vybrat)

        if choice == "1":
            print(kalkulacka)
            calc()
        elif choice == "2":
            print(jazy)
            jazyky()
        elif choice == "3":
            print("Themes")
            print(NotImplementedError)
            return main_menu()
            # themes
        elif choice == "4":
            print(nastaveni)
            print(NotImplementedError)
            return main_menu()
        elif choice == "5":
            print("Credits")
            print("Vytvořil: Rodrick (Ten Ajťák) a Ocasníček (Ten Elektrikář)")
            print(zelena + "https://github.com/rodrickhmmm/RovnomerPenez" + bila)
            time.sleep(5)
            main_menu()
        elif choice == "6":
            print("Exit")
            sys.exit()
        else:
            print(neumispsat)

# KONEC MAIN MENU ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# HLAVNÍ FUNKCE ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Uvodni zprava a zadani promennych uzivatelem
def calc():
    clear()
    print(cervena + "===", zluta + nadpis, cervena + "===")
    p1 = float(input(modra + p1penize + bila))
    p2 = float(input(zluta + player2BezKoncovky + p2penizeovi + bila))
    print("")

    # podmínky pro kokoty    
    if ((p1 <= 0) and (p2 <= 0)):
        print(mocchudy)
    elif p1 == p2:
        print(matestejne)
    elif p1 > p2:
        rozdil = p1 - p2
        print(musisdat, rozdil, symbol, ovi)
    else:
        rozdil = p2 - p1
        print(timusidat, rozdil, symbol)

main_menu()