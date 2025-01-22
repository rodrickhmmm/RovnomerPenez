# importuješ klundu

import pyautogui
import time
from colorama import ansi, Fore

#chápeš uhhh nazev okna idk
mc = "Feather Client 1.21.4"
player1 = "Freakrick"
player2 = "Prdelníč"
player2ek = "Prdelníček"

#uvodni zprava a zadani promennych uzivatelem
print("\033[31;49;1m" + "===", "\033[33;49;1m" + "Výpočet stejné hodnoty měny (socialismus simulátor)", "\033[31;49;1m" + "===")
p1 = int(input('\033[34;49;1m' + "Částka " + player1 + "a: " + "\033[0m"))
p2 = int(input("\033[33;49;1m" + "Částka " + player2 + "a: " + "\033[0m"))
print("")

if p1 < p2:
    print("\033[31;49;1m" + player2ek,"nemůže mít víc peněz jak", player1 + "!!!!!!!")
    exit(1)
    
if ((p1 <= 0) and (p2 <= 0)):
    print("\033[31;49;1m" + player1,"a", player2ek + " nemůžou mít 0€!!!!!!!")
    exit(1)
    
if (p1 == p2):
    print("\033[31;49;1m" + player1,"a", player2ek + " nemůžou mít stejně peněz!!!!!!!")   
    exit(1)

#vypocet
vysledek = p1 - ((p1 + p2) / 2)

# napíše zprávu kolik musíš dát a že musíš počkat
print("\033[32;49;1m" + "Musíš dát", vysledek,"€", player2 + "ovi")
time.sleep(0.5)
print("\033[32;49;1m" + "Počkej než se otevře minecraft...")
time.sleep(0.5)
print("")
print("\033[31;49;1m" + "===", "\033[33;49;1m" + "Výpočet stejné hodnoty měny (socialismus simulátor)", "\033[31;49;1m" + "===")
time.sleep(0.3)

# otevre mc
Mc = pyautogui.getWindowsWithTitle(mc)[0]
Mc.activate()

#automaticke napsani prikazu do chatu
time.sleep(0.4)
pyautogui.press("esc")
pyautogui.press("t")
pyautogui.write("/pay Ocasnik " + str(vysledek))
pyautogui.press("enter")