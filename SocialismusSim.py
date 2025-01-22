# Varování! Barvy se nezobrazujou ve starem cmd (od windows 10 a níž). Pro správné fungování se musí nainstalovat Microsoft Terminal z Microsoft Storu.

# importuješ moduly

import pyautogui
import time
from colorama import ansi


# KONFIGURACE
automatickynapsat = True # automaticky zapsat do minecraftu příkaz, true = ano, zapiš, false = ne, nezapisuj
nazevvokna = "Feather Client 1.21.4" # název okna, které má skript otevřít - v mém případě Feather Client, normálně by mělo být Minecraft <dopln si verzi>
player2BezKoncovky = "Ocasníčk" # jméno hráče 2 bez koncovky (pro lepší skloňování protože čeština lmao)
player2ek = "Ocasníček" # jméno hráče 2
player2nick = "Ocasnik" # nick hráče

# KONFIGURACE BAREV 
cervena = "\033[31;49;1m"
zluta = "\033[33;49;1m"
modra = '\033[34;49;1m'
zelena = "\033[32;49;1m"
bila = "\033[0m"

# Uvodni zprava a zadani promennych uzivatelem
print(cervena + "===", zluta + "Výpočet stejné hodnoty měny (socialismus simulátor)", cervena + "===")
p1 = float(input(modra + "Tvoje peníze:" + bila))
p2 = float(input(zluta + player2BezKoncovky + "ovi peníze: " + bila))
print("")
    
# podmínky pro kokoty    
if ((p1 <= 0) and (p2 <= 0)):
    print(cervena + player1,"a", player2ek + " jsou moc chudý!!!!!!!")
    exit(1)
    
if (p1 == p2):
    print(cervena + " seš piča? už máte stejně!!!!!!!")   
    exit(1)

# výpočet
mezivysledek = float(p1 - ((p1 + p2) / 2))
vysledek = float(abs(mezivysledek))

# napíše zprávu kolik musíš dát
if (p1 > p2):   
    print(bila + "Musíš dát", vysledek,"€", player2BezKoncovky + "ovi")
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
    print(cervena + "===", zluta + "Výpočet stejné hodnoty měny (socialismus simulátor)", cervena + "===")
    time.sleep(0.3)

    # otevre mc
    Mc = pyautogui.getWindowsWithTitle(nazevvokna)[0]
    Mc.activate()

    #automaticke napsani prikazu do chatu
    time.sleep(0.4)
    pyautogui.press("esc")
    pyautogui.press("t")
    pyautogui.write("/pay " + str(player2nick) + " " + str(vysledek))
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
    

