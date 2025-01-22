# importuješ klundu

import pyautogui
import time
from colorama import ansi, Fore

# KONFIGURACE
automatickynapsat = False
nazevvokna = "Feather Client 1.21.4"
player2BezKoncovky = "Ocasníčk"
player2ek = "Ocasníček"
player2nick = "Ocasnik"

#uvodni zprava a zadani promennych uzivatelem
print("\033[31;49;1m" + "===", "\033[33;49;1m" + "Výpočet stejné hodnoty měny (socialismus simulátor)", "\033[31;49;1m" + "===")
p1 = int(input('\033[34;49;1m' + "Tvoje peníze:" + "\033[0m"))
p2 = int(input("\033[33;49;1m" + player2BezKoncovky + "ovi peníze: " + "\033[0m"))
print("")
    
if ((p1 <= 0) and (p2 <= 0)):
    print("\033[31;49;1m" + player1,"a", player2ek + " jsou moc chudý!!!!!!!")
    exit(1)
    
if (p1 == p2):
    print("\033[31;49;1m" + " seš piča? už máte stejně!!!!!!!")   
    exit(1)

#vypocet
mezivysledek = p1 - ((p1 + p2) / 2)
vysledek = abs(mezivysledek)

# napíše zprávu kolik musíš dát
if (p1 > p2):   
    print("\033[32;49;1m" + "Musíš dát", vysledek,"€", player2BezKoncovky + "ovi")
    print("")
    time.sleep(0.5)

if (p1 < p2):
    print("\033[32;49;1m" + player2ek, "ti musí dát", vysledek,"€",)
    print("")
    time.sleep(0.5)


if automatickynapsat == True and (p1 > p2):
    # timeout
    print("\033[32;49;1m" + "Počkej než se otevře minecraft...")
    time.sleep(0.5)
    print("")
    print("\033[31;49;1m" + "===", "\033[33;49;1m" + "Výpočet stejné hodnoty měny (socialismus simulátor)", "\033[31;49;1m" + "===")
    time.sleep(0.3)

    # otevre mc
    Mc = pyautogui.getWindowsWithTitle(nazevvokna)[0]
    Mc.activate()

    #automaticke napsani prikazu do chatu
    time.sleep(0.4)
    pyautogui.press("esc")
    pyautogui.press("t")
    pyautogui.write("/pay " + str(player2nick), str(vysledek))
    pyautogui.press("enter")
    exit

if automatickynapsat == True and (p1 < p2):
    exit

if automatickynapsat == False and (p1 > p2):
    print("Napiš do Minecraftu tento příkaz")
    print("/pay " + str(player2nick), str(vysledek))
    exit

if automatickynapsat == False and (p1 < p2):
    exit
    

