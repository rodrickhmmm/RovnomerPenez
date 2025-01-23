# Varování! Barvy se nezobrazujou ve starem cmd (od windows 10 a níž). Pro správné fungování se musí nainstalovat Microsoft Terminal z Microsoft Storu.

# importuješ moduly

import json
import time
from colorama import ansi
import pyautogui

# KONFIGURACE
nazevvokna = "Feather Client 1.21.4" # název okna, které má skript otevřít - v mém případě Feather Client, normálně by mělo být Minecraft <dopln si verzi>
player2BezKoncovky = "Ocasníčk" # jméno hráče 2 bez koncovky (pro lepší skloňování protože čeština lmao)
player2ek = "Ocasníček" # jméno hráče 2
player2nick = "Ocasnik" # nick hráče
symbol = "€" # symbol měny
jazyk = "data.json"


# KONFIGURACE BAREV 
cervena = "\033[31;49;1m"
zluta = "\033[33;49;1m"
modra = '\033[34;49;1m'
zelena = "\033[32;49;1m"
bila = "\033[0m"

# Importace jazyka/dialektu do python souboru
with open(jazyk, 'r', encoding='utf-8') as file:
    translations = json.load(file)

# Vytvoření lokálních proměnných dynamicky
locals().update(translations)

# deklarace var automatickynapsat

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
        
# funkce na otevření mc
def otevritmc():
    try:
        windows = pyautogui.getWindowsWithTitle(nazevvokna)
        if not windows:
            raise ValueError(f"Okno s názvem '{nazevvokna}' nebylo nalezeno.")  # Vlastní chyba, pokud je seznam prázdný
    
        Mc = windows[0]
        Mc.activate()
        print(f"Okno '{nazevvokna}' bylo úspěšně aktivováno.")

    except ValueError as e:
        print(e)  # Zobrazí vlastní zprávu při prázdném seznamu
    except IndexError:
        print("Chyba: Pokus o přístup k neexistujícímu oknu.")
    except Exception as e:
        print(f"Neočekávaná chyba: {e}")
    
# Uvodni zprava a zadani promennych uzivatelem
print(cervena + "===", zluta + nadpis, cervena + "===")
p1 = float(input(modra + p1penize + bila))
p2 = float(input(zluta + player2BezKoncovky + p2penizeovi + bila))
print("")
    
# podmínky pro kokoty    
if ((p1 <= 0) and (p2 <= 0)):
    print(cervena + ty, a , player2ek + mocchudy)
    exit(1)
    
if (p1 == p2):
    print(cervena + matestejne)   
    exit(1)

# výpočet
mezivysledek = float(p1 - ((p1 + p2) / 2))
mezivysledek2 = float(abs(mezivysledek))
if mezivysledek2.is_integer() == True:
    vysledek = int(mezivysledek2)
else:
    vysledek = mezivysledek2

# napíše zprávu kolik musíš dát
if (p1 > p2):   
    print(bila + musisdat, vysledek, symbol, player2BezKoncovky + ovi)
    print("")
    time.sleep(0.5)

if (p1 < p2):
    print("\033[32;49;1m" + player2ek, timusidat, vysledek, symbol)
    print("")
    time.sleep(0.5)

otazka1()

if automatickynapsat == True and (p1 > p2):
    # timeout
    print("\033[32;49;1m" + ckjmc)
    time.sleep(0.5)
    print("")
    print(cervena + "===", zluta + "Výpočet stejné hodnoty měny (socialismus simulátor)", cervena + "===")
    time.sleep(0.3)
    otevritmc()
    time.sleep(0.4)
    pyautogui.press("esc")
    pyautogui.press("t")
    pyautogui.write("/pay " + str(player2nick) + " " + str(vysledek))
    pyautogui.press("enter")
    exit

if automatickynapsat == True and (p1 < p2):
    print("\033[32;49;1m" + "Počkej než se otevře minecraft...")
    time.sleep(0.5)
    print("")
    print(cervena + "===", zluta + "Výpočet stejné hodnoty měny (socialismus simulátor)", cervena + "===")
    time.sleep(0.3)
    otevritmc()
    time.sleep(0.4)
    pyautogui.press("esc")
    pyautogui.press("t")
    pyautogui.write(str(player2nick) + " posli mne " + str(vysledek) + str(symbol) + "€")
    pyautogui.press("enter")

if automatickynapsat == False and (p1 > p2):
    print("Napiš do Minecraftu tento příkaz:")
    print(zelena + "/pay " + str(player2nick), str(vysledek) + bila)
    exit

if automatickynapsat == False and (p1 < p2):
    exit
    


