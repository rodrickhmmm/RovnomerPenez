sudo true
echo "Instalace Rovnoměru peněz..."
cd ~
git clone https://github.com/rodrickhmmm/RovnomerPenez
cd RovnomerPenez
echo "Instalování modulů..."
python -m pip install --upgrade pip
pip install pyautogui
sudo chmod +x ./Main.py
sudo chmod +x ./run.sh
./run.sh
cd ~
rm -rf install.sh