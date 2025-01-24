
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
automatickynapsat = config.get("automatickynapsat", False) # automatické napsání do chatu

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
    global nadpis, automatickynapsat, zpet, jazy, kalkulacka, p1penize, p2penizeovi, a, mocchudy, ty, matestejne, musisdat, ovi, timusidat, ckjmc, poslimechat, mcprikaz, chcescmddochatu, neumispsat, nenalezenookno, oknoaktivovano, nastaveni, vybrat, nenitu, zpatky, zmenajazyka

    # Inicializace proměnných
    nadpis = "Nadpis menu"
    kalkulacka = "Kalkulačka"
    p1penize = "Tvoje peníze: "
    p2penizeovi = "ovi peníze: "
    a = "a"
    mocchudy = " jste moc chudý!!!!!!!"
    ty = "ty"
    matestejne = " seš piča? už máte stejně!!!!!!!"
    musisdat = "Musíš dát"
    ovi = "ovi"
    timusidat = "ti musí dát"
    ckjmc = "Počkej než se otevře minecraft..."
    poslimechat = " posli mne "
    mcprikaz = "Napiš do Minecraftu tento příkaz:"
    chcescmddochatu = "Chceš, abych to za tebe napsal do chatu?"
    neumispsat = "Neumíš psát???? Zadej prosím 'y' nebo 'n'."
    nenalezenookno = "Okno s názvem '{nazevvokna}' nebylo nalezeno."
    oknoaktivovano = "Okno '{nazevvokna}' bylo úspěšně aktivováno."
    nastaveni = "Nastavení"
    vybrat = "Vyber si: "
    nenitu = "Neimplementováno"
    zpatky = "Zpět"
    zmenajazyka = "Jazyk byl změněn na Češtinu."
    jazy = "Jazyky"
    zpet = "Zpět"

    with open("jazyky/"+ jazyk + ".json", 'r', encoding='utf-8') as file:
        translations = json.load(file)
    locals().update(translations)

    nadpis = translations.get("nadpis", nadpis)
    kalkulacka = translations.get("kalkulacka", kalkulacka)
    p1penize = translations.get("p1penize", p1penize)
    p2penizeovi = translations.get("p2penizeovi", p2penizeovi)
    a = translations.get("a", a)
    mocchudy = translations.get("mocchudy", mocchudy)
    ty = translations.get("ty", ty)
    matestejne = translations.get("matestejne", matestejne)
    musisdat = translations.get("musisdat", musisdat)
    ovi = translations.get("ovi", ovi)
    timusidat = translations.get("timusidat", timusidat)
    ckjmc = translations.get("ckjmc", ckjmc)
    poslimechat = translations.get("poslimechat", poslimechat)
    mcprikaz = translations.get("mcprikaz", mcprikaz)
    chcescmddochatu = translations.get("chcescmddochatu", chcescmddochatu)
    neumispsat = translations.get("neumispsat", neumispsat)
    nenalezenookno = translations.get("nenalezenookno", nenalezenookno)
    oknoaktivovano = translations.get("oknoaktivovano", oknoaktivovano)
    nastaveni = translations.get("nastaveni", nastaveni)
    vybrat = translations.get("vybrat", vybrat)
    nenitu = translations.get("nenitu", nenitu)
    zpatky = translations.get("zpatky", zpatky)
    zmenajazyka = translations.get("zmenajazyka", zmenajazyka)
    jazy = translations.get("jazy", jazy)
    zpet = translations.get("zpet", zpet)

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
    print(zelena + "[5]" + bila, "English")
    print(zelena + "[6]" + bila, "Skinhead English")
    print(zelena + "[7]" + cervena, zpet + bila) #type: ignore
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
        jazyk = "en"
        importjazyka()
        print(cervena + zmenajazyka + bila)
        time.sleep(1)
        return main_menu()
    if vyber == "6":
        jazyk = "sh"
        importjazyka()
        print(cervena + zmenajazyka + bila)
        time.sleep(1)
        return main_menu()    
    if vyber == "7":
        return main_menu()
    else:
        print(neumispsat)
        return jazyky()

#MAIN MENU ------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main_menu():
    clear()
    while True:
        print(cervena + "===", zluta + nadpis, cervena + "===")
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
            #dočasné řešení
            otazka1()
            return main_menu()
        elif choice == "5":
            clear()
            print(modra + "Credits" + bila)
            print("Vytvořil: Rodrick (Ten Ajťák) a Ocasníček (Ten Elektrikář)")
            print(zelena + "https://github.com/rodrickhmmm/RovnomerPenez" + bila)
            time.sleep(5)
            main_menu()
        elif choice == "6":
            print("Exit")
            sys.exit()
        else:
            clear()
            print(neumispsat)
            main_menu()

# KONEC MAIN MENU ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# HLAVNÍ FUNKCE ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Uvodni zprava a zadani promennych uzivatelem
def calc():
    clear()
    global p1, p2
    print(cervena + "===", zluta + nadpis, cervena + "===")
    p1 = float(input(modra + p1penize + bila))
    p2 = float(input(zluta + player2BezKoncovky + p2penizeovi + bila))
    print("")

    # podmínky pro kokoty    
    if ((p1 <= 0) and (p2 <= 0)):
        print(cervena + mocchudy + bila)        
    elif p1 == p2:
        print(cervena + matestejne + bila)

    # výpočet
    global mezivysledek, mezivysledek2, vysledek
    mezivysledek = float(p1 - ((p1 + p2) / 2))
    mezivysledek2 = float(abs(mezivysledek))
    if mezivysledek2.is_integer() == True:
        vysledek = int(mezivysledek2)
    else:
        vysledek = mezivysledek2

    if (p1 > p2):   
        print(zelena + "Musíš dát", vysledek, symbol, player2BezKoncovky + "ovi" + bila)
        input("Press Enter to continue...")
        clear()

    if (p1 < p2):
        print(zelena + player2ek, "ti musí dát", vysledek, symbol + bila)
        input("Press Enter to continue...")
        clear()

    # final
    if automatickynapsat == True and (p1 > p2):
        # timeout
        clear()
        print(zelena + ckjmc)
        otevritmc()
        time.sleep(0.5)
        clear()
        print(cervena + "===", zluta + nadpis, cervena + "===")
        time.sleep(0.3)
        otevritmc()
        time.sleep(0.4)
        pyautogui.press("esc")
        pyautogui.press("t")
        pyautogui.write("/pay " + str(player2nick) + " " + str(vysledek))
        pyautogui.press("enter")
        main_menu()

    elif automatickynapsat == True and (p1 < p2):
        clear()
        print(zelena + ckjmc)
        otevritmc()
        time.sleep(0.5)
        clear()
        print(cervena + "===", zluta + nadpis, cervena + "===")
        time.sleep(0.3)
        time.sleep(0.4)
        pyautogui.press("esc")
        pyautogui.press("t")
        pyautogui.write(str(player2nick) + " posli mne " + str(vysledek) + str(symbol))
        pyautogui.press("enter")
        clear()

    elif automatickynapsat == False and (p1 > p2):
        clear()
        print(mcprikaz)
        print(zelena + "/pay " + str(player2nick), str(vysledek) + bila)
        input("Press Enter to continue...")
        clear()
        main_menu()

    elif automatickynapsat == False and (p1 < p2):
        clear()
        main_menu()

#automaticky napsat - dočasné řešení
def otazka1():
    global automatickynapsat
    automatickynapsat = None  # Inicializace jako None
    otazka = input(modra + "Chceš, abych to za tebe napsal do chatu? [y/n] " + bila).strip().lower()
    
    if otazka == "y":
        automatickynapsat = True
    elif otazka == "n":
        automatickynapsat = False
    else:
        print(cervena + "Neumíš psát???? Zadej prosím 'y' nebo 'n'." + bila)
        automatickynapsat = None
        return otazka1()

# spuštění
main_menu()