
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
cyan = "\x1b[36m"

# FUNKCE ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Výchozí nastavení
default_settings = {
    "automatickynapsat": False,
    "jazyk": "cz",
    "player2BezKoncovky": "default_value",
    "player2ek": "default_value",
    "player2nick": "default_value",
    "symbol": "coin",
    "nazevvokna": "Minecraft",
    "tema": "Default"
    
}

# Převedení čísel z textu
def extract_number_and_format(text):
    if text.isdigit():
        return int(text)

    match = re.search(r'(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)', text)
    if match:
        extracted_number = match.group(1).replace(",", "")
        return float(extracted_number) if '.' in extracted_number else int(extracted_number)
    else:
        return None


# Funkce pro uložení nastavení do JSON souboru
def ulozit_nastaveni():
    nastaveni = {
        "automatickynapsat": automatickynapsat,
        "jazyk": jazyk,
        "player2BezKoncovky": player2BezKoncovky,
        "player2ek": player2ek,
        "player2nick": player2nick,
        "symbol": symbol,
        "nazevvokna": nazevvokna,
        "tema": tema
    }
    with open("settings.json", "w", encoding="utf-8") as file:
        json.dump(nastaveni, file, ensure_ascii=False, indent=4)

# Funkce pro načtení nastavení z JSON souboru
def nacist_nastaveni():
    global automatickynapsat, jazyk, nazevvokna, player2BezKoncovky, player2ek, player2nick, symbol, tema
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
            tema = nastaveni.get("tema", "default_value")
    else:
        input(cervena + "Nastavení nebylo nalezeno, vytvářím výchozí nastavení. Press enter to continue..." + bila)
        with open("settings.json", "w", encoding="utf-8") as file:
            json.dump(default_settings, file, ensure_ascii=False, indent=4)
        nacist_nastaveni()

# Zavolá funkci nacist_nastaveni při spuštění
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


# importace themes

import json

def importtheme():
    global nadpisbarva, errorbarva, nadpiscarky, settingstextvar, zpatkybarva, zmenajazykabarva, zmenathemebarva, player2barva
    global chcesmcbarva, creditsbarva, p1penizebarva, settingsnadpis, settingsotazka
    global cislovmenu, creditlink, oznamenibarva, cmdbarva

    # Inicializace výchozí hodnoty
    nadpisbarva = "default_color"
    nadpiscarky = "default_color"
    errorbarva = "default_color"
    settingstextvar = "default_color"
    zpatkybarva = "default_color"
    zmenajazykabarva = "default_color"
    zmenathemebarva = "default_color"
    player2barva = "default_color"
    chcesmcbarva = "default_color"
    creditsbarva = "default_color"
    p1penizebarva = "default_color"
    settingsnadpis = "default_color"
    settingsotazka = "default_color"
    cislovmenu = "default_color"
    creditlink = "default_color"
    oznamenibarva = "default_color"
    cmdbarva = "default_color"

    with open("themes/" + tema + ".json", 'r', encoding='utf-8') as file:
        temata = json.load(file)

    # Použití výchozí hodnoty, pokud není klíč nalezen
    nadpisbarva = temata.get("nadpisbarva", nadpisbarva)
    errorbarva = temata.get("errorbarva", errorbarva)
    nadpiscarky = temata.get("nadpiscarky", nadpiscarky)
    settingstextvar = temata.get("settingstextvar", settingstextvar)
    zpatkybarva = temata.get("zpatkybarva", zpatkybarva)
    zmenajazykabarva = temata.get("zmenajazykabarva", zmenajazykabarva)
    zmenathemebarva = temata.get("zmenajazykabarva", zmenajazykabarva)
    player2barva = temata.get("zmenajazykabarva", zmenajazykabarva)
    chcesmcbarva = temata.get("chcesmcbarva", chcesmcbarva)
    creditsbarva = temata.get("creditsbarva", creditsbarva)
    p1penizebarva = temata.get("p1penizebarva", p1penizebarva)
    settingsnadpis = temata.get("settingsnadpis", settingsnadpis)
    settingsotazka = temata.get("settingsotazka", settingsotazka)
    cislovmenu = temata.get("cislovmenu", cislovmenu)
    creditlink = temata.get("creditlink", creditlink)
    oznamenibarva = temata.get("oznamenibarva", oznamenibarva)
    cmdbarva = temata.get("cmdbarva", cmdbarva)

    # Pokud je hodnota v JSONu jako string, pokusíme se ji najít v globálních proměnných
    nadpisbarva = globals().get(nadpisbarva, nadpisbarva)
    errorbarva = globals().get(errorbarva, errorbarva)
    nadpiscarky = globals().get(nadpiscarky, nadpiscarky)
    settingstextvar = globals().get(settingstextvar, settingstextvar)
    zpatkybarva = globals().get(zpatkybarva, zpatkybarva)
    zmenajazykabarva = globals().get(zmenajazykabarva, zmenajazykabarva)
    zmenathemebarva = globals().get(zmenajazykabarva, zmenajazykabarva)
    player2barva = globals().get(zmenajazykabarva, zmenajazykabarva)
    chcesmcbarva = globals().get(chcesmcbarva, chcesmcbarva)
    creditsbarva = globals().get(creditsbarva, creditsbarva)
    p1penizebarva = globals().get(p1penizebarva, p1penizebarva)
    settingsnadpis = globals().get(settingsnadpis, settingsnadpis)
    settingsotazka = globals().get(settingsotazka, settingsotazka)
    cislovmenu = globals().get(cislovmenu, cislovmenu)
    creditlink = globals().get(creditlink, creditlink)
    oznamenibarva = globals().get(oznamenibarva, oznamenibarva)
    cmdbarva = globals().get(cmdbarva, cmdbarva)

theme = "default"  # Nastav výchozí theme
importtheme()

# deklarace var automatickynapsat

def automat():
    clear()
    global automatickynapsat
    automatickynapsat = None  # Inicializace jako None
    otazka = input(chcesmcbarva + chcescmddochatu + " [y/n] " + bila).strip().lower()
    
    if otazka == "y":
        automatickynapsat = True
    elif otazka == "n":
        automatickynapsat = False
    else:
        print(errorbarva + neumispsat + bila)
        automatickynapsat = None
        return automat()
        
# funkce na otevření Minecraftu
def otevritmc():
    try:
        windows = pyautogui.getWindowsWithTitle(nazevvokna)
        if not windows:
            raise ValueError(errorbarva + nenalezenookno)  # Vlastní chyba, pokud je seznam prázdný

        Mc = windows[0]
        Mc.activate()
        print(oknoaktivovano)

    except ValueError as e:
        print(e)  # Zobrazí vlastní zprávu při prázdném seznamu
    except IndexError:
        print(errorbarva + "Chyba: Pokus o přístup k neexistujícímu oknu.")
    except Exception as e:
        print(f"Neočekávaná chyba: {e}")

# Menu nastavení -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def settings_menu():
    clear()
    print(settingsnadpis + nastaveni + bila)
    print(cislovmenu + "[1]" + bila, autonapsat + ":", settingstextvar + str(automatickynapsat) + bila)
    print(cislovmenu + "[2]" + bila, "Player 2 Nick" + ":", settingstextvar + player2nick + bila)
    print(cislovmenu + "[3]" + bila, "Player 2 Name" + ":", settingstextvar + player2BezKoncovky + " / " + player2ek + bila)
    print(cislovmenu + "[4]" + bila, minecraft + ":", settingstextvar + nazevvokna + bila)
    print(cislovmenu + "[5]" + bila, "Symbol" + ":", settingstextvar + symbol + bila)
    print(cislovmenu + "[6]" + zpatkybarva, zpatky, bila)
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

# Menu jazyků
def jazyky():
    clear()
    print(settingsnadpis + jazy + bila)
    print(cislovmenu + "[1]" + bila, "Čeština")
    print(cislovmenu + "[2]" + bila, "Moravština")
    print(cislovmenu + "[3]" + bila, "Hantec")
    print(cislovmenu + "[4]" + bila, "Brainrot spachtoš")
    print(cislovmenu + "[5]" + bila, "Skinhead English")
    print(cislovmenu + "[6]" + bila, "English")
    print(cislovmenu + "[7]" + bila, "Français")
    print(cislovmenu + "[8]" + bila, "YN/Hood language")     
    print(cislovmenu + "[9]" + bila, "Cajzlovština (přeloženo z Hantecu - Pražáčtina)") 
    print(cislovmenu + "[10]" + zpatkybarva, zpatky + bila) #type: ignore
    vyber = input(vybrat)
    global jazyk
    if vyber == "1":
        jazyk = "cz"
        importjazyka()
        print(zmenajazykabarva + zmenajazyka + bila)
        time.sleep(1)
        clear()
        ulozit_nastaveni()  # Uložení nastavení po změně jazyka
        return main_menu()
    elif vyber == "2":
        jazyk = "mo"
        importjazyka()
        print(zmenajazykabarva + zmenajazyka + bila)
        time.sleep(1)
        clear()
        ulozit_nastaveni()  # Uložení nastavení po změně jazyka
        return main_menu()
    elif vyber == "3":
        jazyk = "br"
        importjazyka()
        print(zmenajazykabarva + zmenajazyka + bila)
        time.sleep(1)
        clear()
        ulozit_nastaveni()  # Uložení nastavení po změně jazyka
        return main_menu()
    elif vyber == "4":
        jazyk = "ba"
        importjazyka()
        print(zmenajazykabarva + zmenajazyka + bila)
        time.sleep(1)
        clear()
        ulozit_nastaveni()  # Uložení nastavení po změně jazyka
        return main_menu()
    elif vyber == "5":
        jazyk = "sh"
        importjazyka()
        print(zmenajazykabarva + zmenajazyka + bila)
        time.sleep(1)
        clear()
        ulozit_nastaveni()  # Uložení nastavení po změně jazyka
        return main_menu()
    elif vyber == "6":
        jazyk = "en"
        importjazyka()
        print(zmenajazykabarva + zmenajazyka + bila)
        time.sleep(1)
        clear()
        ulozit_nastaveni()  # Uložení nastavení po změně jazyka
        return main_menu()
    elif vyber == "7":
        jazyk = "fr"
        importjazyka()
        print(zmenajazykabarva + zmenajazyka + bila)
        time.sleep(1)
        clear()
        ulozit_nastaveni()  # Uložení nastavení po změně jazyka
        return main_menu()
    elif vyber == "8":
        jazyk = "ho"
        importjazyka()
        print(zmenajazykabarva + zmenajazyka + bila)
        time.sleep(1)
        clear()
        ulozit_nastaveni()  # Uložení nastavení po změně jazyka
        return main_menu()
    elif vyber == "9":
        jazyk = "pr"
        importjazyka()
        print(zmenajazykabarva + zmenajazyka + bila)
        time.sleep(1)
        clear()
        ulozit_nastaveni()  # Uložení nastavení po změně jazyka
        return main_menu()    
    elif vyber == "10":
        return main_menu()
    else:
        print(neumispsat)
        clear()
        return jazyky()

# Themes menu
def themes():
    clear()
    print(settingsnadpis + "Vybrat Theme" + bila)
    print(cislovmenu + "[1]" + bila, "Default")
    print(cislovmenu + "[2]" + bila, "Frutiger Aero")
    print(cislovmenu + "[3]" + zpatkybarva, zpatky + bila) #type: ignore
    vyber = input(vybrat)
    global tema
    if vyber == "1":
        tema = "default"
        importtheme()
        print(zmenathemebarva + "Zmenil si theme na default" + bila)
        time.sleep(1)
        clear()
        ulozit_nastaveni()  # Uložení nastavení po změně jazyka
        return main_menu()
    if vyber == "2":
        tema = "frutigeraero"
        importtheme()
        print(zmenathemebarva + "Zmenil si theme na frutigeraero" + bila)
        time.sleep(1)
        clear()
        ulozit_nastaveni()  # Uložení nastavení po změně jazyka
        return main_menu()  
    elif vyber == "3":
        return main_menu()
    else:
        print(neumispsat)
        clear()
        return themes()

#MAIN MENU ------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main_menu():
    clear()
    while True:
        print(nadpiscarky + "===", nadpisbarva + nadpis, nadpiscarky + "===")
        print(cislovmenu + "[1]" + bila, kalkulacka)
        print(cislovmenu + "[2]" + bila, jazy)
        print(cislovmenu + "[3]" + bila, "Themes")
        print(cislovmenu + "[4]" + bila, nastaveni)
        print(cislovmenu + "[5]" + bila, "Credits")
        print(cislovmenu + "[6]" + zpatkybarva, zpatky + bila)

        choice = input(vybrat)

        if choice == "1":
            print(kalkulacka)
            calc()
        elif choice == "2":
            print(jazy)
            jazyky()
        elif choice == "3":
            print("Themes")
            themes()
            
            # themes
        elif choice == "4":
            print(nastaveni)
            settings_menu()
        elif choice == "5":
            clear()
            print(creditsbarva + "Credits" + bila)
            print("Vytvořil: Rodrick - rodrickhmmm (Ten Ajťák) a Ocasníček - xtomasnemec (Ten Elektrikář)")
            print(creditlink + "https://github.com/rodrickhmmm/RovnomerPenez" + bila)
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
# Tj. kalkulačka

def calc():
    clear()
    global p1, p2
    print(nadpiscarky + "===", nadpisbarva + nadpis, nadpiscarky + "===")
    p1 = input(p1penizebarva + p1penize + bila)
    p2 = input(player2barva + player2BezKoncovky + p2penizeovi + bila)
    print("")

    # Vyfiltruje z textu čísla 
    n1 = extract_number_and_format(p1)
    n2 = extract_number_and_format(p2)

    if n1 is None or n2 is None:
        print(errorbarva + "Error: Unable to extract valid numbers from inputs." + bila)
        input("Press Enter to continue...")
        return main_menu()

    if n1 <= 0 and n2 <= 0:
        print(errorbarva + mocchudy + bila)
        input("Press Enter to continue...")
        return main_menu()
    elif n1 == n2:
        print(errorbarva + matestejne + bila)
        input("Press Enter to continue...")
        return main_menu()

    # Provedení výpočtu
    global mezivysledek, mezivysledek2, vysledek
    mezivysledek = float(n1 - ((n1 + n2) / 2))
    mezivysledek2 = abs(mezivysledek)
    vysledek = int(mezivysledek2) if mezivysledek2.is_integer() else mezivysledek2

    # Finální zpráva, která zobrazí jestli ty nebo druhý hráč dává peníze
    if n1 > n2:
        print(oznamenibarva + musisdat, vysledek, symbol, player2BezKoncovky + ovi + bila)
        input("Press Enter to continue...")
        clear()
    elif n1 < n2:
        print(oznamenibarva + player2ek, timusidat, vysledek, symbol + bila)
        input("Press Enter to continue...")
        clear()
    

    # Proces, který napíše do chatu příkaz nebo request budto jo nebo nn
    if automatickynapsat == True and (p1 > p2):
        # timeout
        clear()
        print(oznamenibarva + ckjmc)
        otevritmc()
        time.sleep(0.5)
        clear()
        print(nadpiscarky + "===", nadpisbarva + nadpis, nadpiscarky + "===")
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
        print(oznamenibarva + ckjmc)
        otevritmc()
        time.sleep(0.5)
        clear()
        print(nadpiscarky + "===", nadpisbarva + nadpis, nadpiscarky + "===")
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
        print(cmdbarva + "/pay " + str(player2nick), str(vysledek) + bila)
        input("Press Enter to continue...") 
        clear()
        main_menu()

    elif automatickynapsat == False and (p1 < p2):
        clear()
        main_menu()
        
# KONEC HLAVNÍ FUNKCE ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Nastavení otazky 
# Otazka automaticky napsat
def otazka1():
    clear()
    global automatickynapsat
    automatickynapsat = None  # Inicializace jako None
    otazka = input(chcesmcbarva + chcescmddochatu + "[y/n]" + bila).strip().lower()
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
        print(errorbarva + neumispsat + bila)
        automatickynapsat = None
        input("Press Enter to continue...") 
        clear()
        return otazka1()

# změnit nick hráče 2
def otazka2():
    clear()
    global player2nick
    player2nick = input(settingsotazka + nick2 + bila)
    ulozit_nastaveni()
    clear()
    settings_menu()

# změnit jméno hráče 2
def otazka3():
    clear()
    nacist_nastaveni()
    global player2BezKoncovky, player2ek
    player2BezKoncovky = input(settingsotazka + jmeno2bez + bila)

    if jazyk not in ["en", "sh", "ho"]:
        player2ek = input(settingsotazka + jmeno2 + bila)
    else:
        player2ek = player2BezKoncovky

    ulozit_nastaveni()
    clear()
    settings_menu()
    
#změnit symbol
def otazka4():
    clear()
    global nazevvokna
    nazevvokna = input(settingsotazka + minecraft + bila)
    ulozit_nastaveni()
    clear()
    settings_menu()    

#změnit symbol
def otazka5():
    clear()
    global symbol
    symbol = input(settingsotazka + zadejsymbol + bila)
    ulozit_nastaveni()
    clear()
    settings_menu()

# spuštění
main_menu()