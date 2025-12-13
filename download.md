# Linux ⤵️

sudo apt update
sudo apt install git python3 python3-venv python3-pip -y

cd ~
git clone https://github.com/FSOCIETYTTKil1l/Deadpool-Tool.git

cd ~/Deadpool-Tool
python3 -m venv deadpool-venv

source deadpool-venv/bin/activate
cd "Deadpool Tool"

pip install pystyle requests

python main.py
deactivate

# Or just enter it once ⤵️

python3 -m venv ~/deadpool-temp-venv
source ~/deadpool-temp-venv/bin/activate && \
cd ~/Deadpool-Tool/"Deadpool Tool" && \
pip install pystyle requests && \
python main.py && \
deactivate
