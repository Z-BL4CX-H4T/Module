# MODULE #
# Install Modules or Materials for Termux and Linux
# FOR TERMUX#

pkg update

pkg upgrade

pkg install python2

pkg install git

git clone https://github.com/ZeThAlOnE/Module.git

cd Module

chmod +x *

pip install -r requirements.txt

python Module-Termux.py
