# module
from os import system
from time import sleep

# program
def logo():
   print("""

\33[5;32m __________ _____ _   _ __  __  ___  ____  _   _ _     _____\33[5;32m
\33[5;32m|__  / ____|_   _| | | |  \/  |/ _ \|  _ \| | | | |   | ____|\33[5;32m
  \33[5;32m/ /|  _|   | | | |_| | |\/| | | | | | | | | | | |   |  _|\33[5;32m
 \33[5;32m/ /_| |___  | | |  _  | |  | | |_| | |_| | |_| | |___| |___ \33[5;32m
\33[5;32m/____|_____| |_| |_| |_|_|  |_|\___/|____/ \___/|_____|_____|\33[5;32m  
""")

logo()
def menu():
   system("""\33[5;31mapt update\33[5;31m
apt upgrade
apt install python
apt install python2
apt install curl
apt install tar
apt install zip
apt install unzip
apt install tor
apt install wget
apt install wcalc
apt install bmon
apt install golang
apt install perl
apt install openssl
apt install openssh
apt install zsh
apt install fortune
apt install htop
apt install dnsutils
apt install cmatrix
apt install ranger
apt install libcaca
apt install git
apt install toilet
apt install neofetch
apt install php
apt install pv
apt install w3m 
apt install sl
\33[5;31m""")
   print("""

\33[0;35m ____  _____ _     _____ ____    _    ___\33[0;35m 
\33[0;35m/ ___|| ____| |   | ____/ ___|  / \  |_ _|\33[0;35m
\33[0;35m\___ \|  _| | |   |  _| \___ \ / _ \  | |\33[0;35m
\33[0;35m ___) | |___| |___| |___ ___) / ___ \ | |\33[0;35m
\33[0;35m|____/|_____|_____|_____|____/_/   \_\___|\33[0;35m
""")
   sleep(1)

menu()