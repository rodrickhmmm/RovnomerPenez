
# importuješ moduly
import os
import gettext
import json
import sys
import time
from colorama import ansi
import pyautogui
import re

# KONFIGURACE BAREV 
cervena = "\033[31;49;1m"
zluta = "\033[33;49;1m"
modra = '\033[34;49;1m'
zelena = "\033[32;49;1m"
bila = "\033[0m"

# FUNKCE ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Výchozí nastavení
default_settings = {
    "automatickynapsat": False,
    "jazyk": "cz",
    "player2BezKoncovky": "default_value",
    "player2ek": "default_value",
    "player2nick": "default_value",
    "symbol": "coin",
    "nazevvokna": "Minecraft"
}

def extract_number(text):
    # Use regex to extract the number, ignoring commas and decimals
    match = re.search(r'(\d{1,3}(?:,\d{3})*)', text)
    if match:
        # Remove commas and convert to integer
        return int(match.group(1).replace(",", ""))
    else:
        return None  # Return None if no number is found

# Funkce pro uložení nastavení do JSON souboru
def ulozit_nastaveni():
    nastaveni = {
        "automatickynapsat": automatickynapsat,
        "jazyk": jazyk,
        "player2BezKoncovky": player2BezKoncovky,
        "player2ek": player2ek,
        "player2nick": player2nick,
        "symbol": symbol,
        "nazevvokna": nazevvokna
    }
    with open("settings.json", "w", encoding="utf-8") as file:
        json.dump(nastaveni, file, ensure_ascii=False, indent=4)

# Funkce pro načtení nastavení z JSON souboru
def nacist_nastaveni():
    global automatickynapsat, jazyk, nazevvokna, player2BezKoncovky, player2ek, player2nick, symbol
    if os.path.exists("settings.json"):
        with open("settings.json", "r", encoding="utf-8") as file:
            nastaveni = json.load(file)
            automatickynapsat = nastaveni.get("automatickynapsat", False)
            jazyk = nastaveni.get("jazyk", "cz")
            nazevvokna = nastaveni.get("nazevvokna", "Minecraft")
            player2BezKoncovky = nastaveni.get("player2BezKoncovky", "default_value")
            player2ek = nastaveni.get("player2ek", "default_value")
            player2nick = nastaveni.get("player2nick", "default_value")
            symbol = nastaveni.get("symbol", "coin")
    else:
        input(cervena + "Nastavení nebylo nalezeno, vytvářím výchozí nastavení. Press enter to continue..." + bila)
        with open("settings.json", "w", encoding="utf-8") as file:
            json.dump(default_settings, file, ensure_ascii=False, indent=4)
        nacist_nastaveni()

# Zavolejte funkci nacist_nastaveni při spuštění programu
nacist_nastaveni()

# clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# importace jazyka/dialektu
def importjazyka():
    global nadpis, zadejsymbol, nick2, minecraft, jmeno2, jmeno2bez, autonapsat, automatickynapsat, zpet, jazy, kalkulacka, p1penize, p2penizeovi, a, mocchudy, ty, matestejne, musisdat, ovi, timusidat, ckjmc, poslimechat, mcprikaz, chcescmddochatu, neumispsat, nenalezenookno, oknoaktivovano, nastaveni, vybrat, nenitu, zpatky, zmenajazyka

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
    autonapsat = "Automatické napsání do chatu"
    jmeno2bez = "Zadej jméno hráče 2 bez koncovky: "
    jmeno2 = "Zadej jméno hráče 2: "
    minecraft = "Název okna Minecraftu: "
    nick2 = "Zadej nick hráče 2: "
    zadejsymbol = "Zadej symbol měny: "

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
    autonapsat = translations.get ("autonapsat", autonapsat)
    jmeno2bez = translations.get("jmeno2bez", jmeno2bez)
    jmeno2 = translations.get("jmeno2", jmeno2)
    minecraft = translations.get("minecraft", minecraft)
    nick2 = translations.get("nick2", "Zadej nick hráče 2: ")
    zadejsymbol = translations.get("zadejsymbol", "Zadej symbol měny: ")

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

# Menu nastavení -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def settings_menu():
    clear()
    print(modra + nastaveni + bila)
    print(zelena + "[1]" + bila, autonapsat + ":", cervena + str(automatickynapsat) + bila)
    print(zelena + "[2]" + bila, "Player 2 Nick" + ":", cervena + player2nick + bila)
    print(zelena + "[3]" + bila, "Player 2 Name" + ":", cervena + player2BezKoncovky + " / " + player2ek + bila)
    print(zelena + "[4]" + bila, minecraft + ":", cervena + nazevvokna + bila)
    print(zelena + "[5]" + bila, "Symbol" + ":", cervena + symbol + bila)
    print(zelena + "[6]" + cervena, zpatky, bila)
    vyber = input(vybrat)
    if vyber == "1":
        clear()
        otazka1()
        ulozit_nastaveni()
    elif vyber == "2":
        clear()
        otazka2()
        ulozit_nastaveni()
    elif vyber == "3":
        clear()
        otazka3()
        ulozit_nastaveni()
    elif vyber == "4":
        clear()
        otazka4()
        ulozit_nastaveni()
        return main_menu()
    elif vyber == "5":
        clear()
        otazka5()
        ulozit_nastaveni()
    elif vyber == "6":
        clear()
        return main_menu()
    else:
        print(neumispsat)
        clear()
        return settings_menu()

# menu jazyků
def jazyky():
    clear()
    print(modra + jazy + bila)
    print(zelena + "[1]" + bila, "Čeština")
    print(zelena + "[2]" + bila, "Moravština")
    print(zelena + "[3]" + bila, "Hantec")
    print(zelena + "[4]" + bila, "Brainrot spachtoš")
    print(zelena + "[5]" + bila, "Skinhead English")
    print(zelena + "[6]" + bila, "English")
    print(zelena + "[7]" + cervena, zpet + bila) #type: ignore
    vyber = input(vybrat)
    global jazyk
    if vyber == "1":
        jazyk = "cz"
        importjazyka()
        print(cervena + zmenajazyka + bila)
        time.sleep(1)
        clear()
        ulozit_nastaveni()  # Uložení nastavení po změně jazyka
        return main_menu()
    elif vyber == "2":
        jazyk = "mo"
        importjazyka()
        print(cervena + zmenajazyka + bila)
        time.sleep(1)
        clear()
        ulozit_nastaveni()  # Uložení nastavení po změně jazyka
        return main_menu()
    elif vyber == "3":
        jazyk = "br"
        importjazyka()
        print(cervena + zmenajazyka + bila)
        time.sleep(1)
        clear()
        ulozit_nastaveni()  # Uložení nastavení po změně jazyka
        return main_menu()
    elif vyber == "4":
        jazyk = "ba"
        importjazyka()
        print(cervena + zmenajazyka + bila)
        time.sleep(1)
        clear()
        ulozit_nastaveni()  # Uložení nastavení po změně jazyka
        return main_menu()
    elif vyber == "5":
        jazyk = "sh"
        importjazyka()
        print(cervena + zmenajazyka + bila)
        time.sleep(1)
        clear()
        ulozit_nastaveni()  # Uložení nastavení po změně jazyka
        return main_menu()
    elif vyber == "6":
        jazyk = "en"
        importjazyka()
        print(cervena + zmenajazyka + bila)
        time.sleep(1)
        clear()
        ulozit_nastaveni()  # Uložení nastavení po změně jazyka
        return main_menu()
    elif vyber == "7":
        return main_menu()
    else:
        print(neumispsat)
        clear()
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
            settings_menu()
        elif choice == "5":
            clear()
            print(modra + "Credits" + bila)
            print("Vytvořil: Rodrick - rodrickhmmm (Ten Ajťák) a Ocasníček - xtomasnemec (Ten Elektrikář)")
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
    p1 = input(modra + p1penize + bila)
    p2 = input(zluta + player2BezKoncovky + p2penizeovi + bila)
    print("")

    n1 = extract_number(p1)
    n2 = extract_number(p2)

    # podmínky pro kokoty    
    if ((n1 <= 0) and (n2 <= 0)):
        print(cervena + mocchudy + bila)        
    elif n1 == n2:
        print(cervena + matestejne + bila)

    # výpočet
    global mezivysledek, mezivysledek2, vysledek
    mezivysledek = float(n1 - ((n1 + n2) / 2))
    mezivysledek2 = float(abs(mezivysledek))
    if mezivysledek2.is_integer() == True:
        vysledek = int(mezivysledek2)
    else:
        vysledek = mezivysledek2

    if (p1 > p2):   
        print(zelena + musisdat, vysledek, symbol, player2BezKoncovky + "ovi" + bila)
        input("Press Enter to continue...") 
        clear()

    if (p1 < p2):
        print(zelena + player2ek, timusidat, vysledek, symbol + bila)
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

#automaticky napsat
def otazka1():
    clear()
    global automatickynapsat
    automatickynapsat = None  # Inicializace jako None
    otazka = input(modra + chcescmddochatu + "[y/n]" + bila).strip().lower()
    clear()
    
    if otazka == "y":
        automatickynapsat = True
        ulozit_nastaveni()
        settings_menu()
    elif otazka == "n":
        automatickynapsat = False
        ulozit_nastaveni()
        settings_menu()
    else:
        clear()
        print(cervena + neumispsat + bila)
        automatickynapsat = None
        input("Press Enter to continue...") 
        clear()
        return otazka1()

# změnit nick hráče 2
def otazka2():
    clear()
    global player2nick
    player2nick = input(modra + nick2 + bila)
    ulozit_nastaveni()
    clear()
    settings_menu()

# změnit jméno hráče 2
def otazka3():
    clear()
    global player2BezKoncovky, player2ek
    player2BezKoncovky = input(modra + jmeno2bez + bila)
    if not jazyk == "en" or "sh":
        player2ek = input(modra + jmeno2 + bila)
    if jazyk == "en" or "sh":
        player2ek = player2BezKoncovky
    ulozit_nastaveni()
    clear()
    settings_menu()
    
#změnit symbol
def otazka4():
    clear()
    global nazevvokna
    nazevvokna = input(modra + minecraft + bila)
    ulozit_nastaveni()
    clear()
    settings_menu()    

#změnit symbol
def otazka5():
    clear()
    global symbol
    symbol = input(modra + zadejsymbol + bila)
    ulozit_nastaveni()
    clear()
    settings_menu()

# spuštění
main_menu()