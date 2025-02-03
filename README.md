# **Plně automatický Rovnoměr peněz**
toto byl pouze test toho, jestli rovnoměr peněz může být zcela automatický a číst z logu rovnou čísla. Tahle verze je docelá stará a není aktualizovaná, možná v budoucnu se to přidá jako funkce but.. who knows

# **Rovnoměr peněz**

Hrajete na Minecraft serveru s kamarádem, kde si chcete udržet stejný zůstatek peněz, ale nechce se vám pokaždé manuálně počítat rozdíl? 
Tento jednoduchý Python program vám s tím pomůže! 🚀


# Jak program funguje

Tento program umožňuje zadat aktuální zůstatky peněz dvou hráčů a automaticky spočítá, kolik peněz by měl jeden z hráčů převést druhému, aby měli oba stejný zůstatek.

Dále se vás program zeptá, zda chcete:

Vygenerovat příkaz a zobrazit ho v terminálu, nebo

Na základě toho, kdo má větší zůstatek automaticky otevřít Minecraft a příkaz do něj rovnou napsat, nebo se zeptat druhého hráče, aby mu poslal daný počet peněz.


Ačkoli je program primárně určen pro použití na Minecraft serverech, jeho funkčnost lze snadno přizpůsobit i pro jiné aplikace, kde je třeba vyrovnávat zůstatky nebo generovat specifické příkazy.

Program obsahuje také soubor Open.bat, který usnadňuje spuštění. Jednoduše dvakrát kliknete na tento soubor, a program se automaticky spustí bez nutnosti otevírat terminál.


# Funkce

Automatický výpočet rozdílu: Zadejte zůstatky obou hráčů a program provede všechny výpočty za vás.

Generování příkazu pro Minecraft: Vygeneruje přesný příkaz /pay, který lze okamžitě použít ve hře.

Automatické zadání příkazu: Možnost příkaz automaticky zadat přímo do Minecraftu.

Jednoduché spuštění: Pomocí souboru Open.bat spustíte program jedním kliknutím.

# Jak to spustit

## Windows

- Stáhněte si celé repo
- Spusťte soubour ```nainstalovat moduly.bat```
- Pro otevírání programu použijte soubor ```Open.bat```

## Linux, macOS a další UNIX-like OS

```git clone https://github.com/rodrickhmmm/RovnomerPenez```

```cd RovnomerPenez-main```

```sudo chmod +x ./install.sh```

```./install.sh```

- Pro spouštění používejte: ```/RovnomerPenez-main/run.sh```, ```python /RovnomerPenez-main/Main.py``` nebo otevřte soubor ```Main.py```

# Požadavky


**Python 3** nebo **novější**

Modul **pyautogui** - stačí otevřít soubor nainsttalovat moduly.bat, který automaticky daný modul nainstaluje

**Terminál** (příkazový řádek)

# Credits

Vytvořeno Ajťákem a Elektrikářem
