# module
from os import system
from time import sleep

# program
def logo():
   print("""
 
\33[5;32m _____    _   _\33[5;32m     
\33[5;32m|__  /___| |_| |__\33[5;32m  
  \33[5;32m/ // _ \ __| '_ \ \33[5;32m
 \33[5;32m/ /|  __/ |_| | | |\33[5;32m
\33[5;32m/____\___|\__|_| |_|\33[5;32m
""")

logo()
def menu():
   system("""\33[5;31mpkg update\33[5;31m
pkg upgrade -y
pkg install perl -y
pkg install python -y
pkg install python2 -y
pkg install curl -y
pkg install tar -y
pkg install zip -y
pkg install unzip -y
pkg install tor -y
pkg install wcalc -y
pkg install bmon -y
pkg install golang -y
pkg install openssl -y
pkg install openssh -y
pkg install vim -y
pkg install vim-python -y
pkg install zsh -y
pkg install fortune -y
pkg install htop -y
pkg install dnsutils -y 
pkg install cmatrix -y
pkg install libcaca -y
pkg install sl -y
pkg install ranger -y 
pkg install git -y
pkg install neofetch -y
pkg install toilet -y
pkg install php -y
pkg install lolcat -y
pkg install pv -y
pkg install w3m -y
\33[5;31m""")
   print("""

          \33[0;33m_                 _\33[0;33m 
 \33[0;33m___  ___| | ___  ___  __ _(_)\33[0;33m
\33[0;33m/ __|/ _ \ |/ _ \/ __|/ _` | |\33[0;33m
\33[0;33m\__ \  __/ |  __/\__ \ (_| | |\33[0;33m
\33[0;33m|___/\___|_|\___||___/\__,_|_|\33[0;33m
""")
   sleep(1)

menu()
