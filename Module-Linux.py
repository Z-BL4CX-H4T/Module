# Module-Linux.py
# Tools Installer Linux Version
# Author : Z-SH4DOWSPEECH

import os
import sys
import time
import itertools

__author__ = "Z-SH4DOWSPEECH"
__version__ = "1.0.0"

# === LOGO ===
def logo():
    print("""
\033[5;32m
  __  __           _       _            _     _                  
 |  \/  | ___   __| |_   _| | ___      | |   (_)_ __  _   ___  __
 | |\/| |/ _ \ / _` | | | | |/ _ \_____| |   | | '_ \| | | \ \/ /
 | |  | | (_) | (_| | |_| | |  __/_____| |___| | | | | |_| |>  < 
 |_|  |_|\___/ \__,_|\__,_|_|\___|     |_____|_|_| |_|\__,_/_/\_\
\033[0m
""")

# === ANIMASI SPINNER ===
def spinner(task, duration=3):
    spinner_cycle = itertools.cycle(['|', '/', '-', '\\'])
    start_time = time.time()
    while (time.time() - start_time) < duration:
        sys.stdout.write(f"\r\033[94m{task}... {next(spinner_cycle)}\033[0m")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\r\033[92m[SUCCESS]\033[0m\n")

# === ANIMASI PROGRESS BAR ===
def progress_bar(task, steps=30):
    for i in range(steps + 1):
        bar = "█" * i + "-" * (steps - i)
        sys.stdout.write(f"\r\033[96m{task} |{bar}| {int((i/steps)*100)}%\033[0m")
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write("\n")

# === INSTALLER ===
def install_packages():
    packages = [
        "update && sudo apt upgrade -y",
        "install perl -y",
        "install python3 -y",
        "install curl -y",
        "install tar -y",
        "install zip -y",
        "install unzip -y",
        "install tor -y",
        "install golang -y",
        "install openssl -y",
        "install openssh-client -y",
        "install vim -y",
        "install zsh -y",
        "install htop -y",
        "install dnsutils -y",
        "install cmatrix -y",
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
        print(f"\033[5;31m>> Installing: apt {pkg}\033[0m")
        spinner("Downloading")      # animasi spinner
        progress_bar("Installing")  # progress bar smooth
        os.system(f"sudo apt {pkg}")
        print()

# === MAIN RUN ===
def run():
    logo()
    install_packages()
    print("""
\033[0;33m
  _                 _ 
 ___  ___| | ___  ___  __ _(_)
 / __|/ _ \\ |/ _ \\/ __|/ _` | |
 \\__ \\  __/ |  __/\\__ \\ (_| | |
 |___/\\___|_|\\___||___/\\__,_|_|
\033[0m
""")
    print(f"\033[1;36mTools created by: {__author__}\033[0m\n")

if __name__ == "__main__":
    run()
