# module
import os
import sys
import time
import itertools

# program
def logo():
    print("""
\033[5;32m
  __  __           _       _          _____                              
 |  \/  | ___   __| |_   _| | ___    |_   _|__ _ __ _ __ ___  _   ___  __
 | |\/| |/ _ \ / _` | | | | |/ _ \_____| |/ _ \ '__| '_ ` _ \| | | \ \/ /
 | |  | | (_) | (_| | |_| | |  __/_____| |  __/ |  | | | | | | |_| |>  < 
 |_|  |_|\___/ \__,_|\__,_|_|\___|     |_|\___|_|  |_| |_| |_|\__,_/_/\_\
\033[0m
""")

def spinner(task, duration=3):
    spinner_cycle = itertools.cycle(['|', '/', '-', '\\'])
    start_time = time.time()
    while (time.time() - start_time) < duration:
        sys.stdout.write(f"\r\033[94m{task}... {next(spinner_cycle)}\033[0m")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\r\033[92m[SUCCESS]\033[0m\n")

def progress_bar(task, steps=30):
    for i in range(steps + 1):
        bar = "█" * i + "-" * (steps - i)
        sys.stdout.write(f"\r\033[96m{task} |{bar}| {int((i/steps)*100)}%\033[0m")
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write("\n")

def menu():
    # daftar paket yang akan diinstall
    packages = [
        "update && pkg upgrade -y",
        "install perl -y",
        "install python -y",
        "install python2 -y",
        "install curl -y",
        "install tar -y",
        "install zip -y",
        "install unzip -y",
        "install tor -y",
        "install wcalc -y",
        "install bmon -y",
        "install golang -y",
        "install openssl -y",
        "install openssh -y",
        "install vim -y",
        "install vim-python -y",
        "install zsh -y",
        "install fortune -y",
        "install htop -y",
        "install dnsutils -y",
        "install cmatrix -y",
        "install libcaca -y",
        "install sl -y",
        "install ranger -y",
        "install git -y",
        "install neofetch -y",
        "install toilet -y",
        "install php -y",
        "install lolcat -y",
        "install pv -y",
        "install w3m -y"
    ]

    for pkg in packages:
        print(f"\033[5;31m>> Installing: pkg {pkg}\033[0m")
        spinner("Downloading")          # animasi spinner
        progress_bar("Installing")      # progress bar halus
        os.system(f"pkg {pkg}")
        print()

    print("""
\033[0;33m
  _                 _ 
 ___  ___| | ___  ___  __ _(_)
 / __|/ _ \ |/ _ \/ __|/ _` | |
 \__ \  __/ |  __/\__ \ (_| | |
 |___/\___|_|\___||___/\__,_|_|
\033[0m
""")

    print("\033[1;36mTools created by: Z-SH4DOWSPEECH\033[0m\n")

# jalankan
logo()
menu()
       
