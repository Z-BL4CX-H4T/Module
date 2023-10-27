# MODULE #
# Install Modules or Materials for Termux and Linux
# FOR TERMUX #

pkg update -y

pkg upgrade -y

pkg install python2 -y

pkg install python -y

pkg install git

git clone https://github.com/ZeThAlOnE/Module.git

cd Module

chmod +x *

pip install -r requirements.txt

python Module-Termux.py

# FOR LINUX #

apt update -y

apt upgrade -y

apt install python2 -y

apt install git

git clone https://github.com/ZeThAlOnE/Module.git

cd Module

chmod +x *

pip2 install -r requiremenst.txt

python3 Module-Linux.py
