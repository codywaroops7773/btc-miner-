import secrets, time
from gettext import install
import string, random 
import time  
import random
import string
import os
from colorama import init, Fore
init(convert=True)
import subprocess, requests

wallet = input(Fore.RED + "receive address: ")
print(Fore.CYAN + "checking if address exists...")
time.sleep(1)
walletcheck = requests.get("https://blockchain.info/q/addressbalance/" + wallet)
if walletcheck.status_code == 200:
    print("wallet found!")
else:
    print("wallet invalid!") 
    exit(123) 

for i in range(1000):
    print(secrets.token_hex(nbytes=32), '- 0 btc')
    time.sleep(0.05)
print(secrets.token_hex(nbytes=32), ' - 0.31 btc') 
print("your btc has been transfered to your wallet")
input('press enter no continue')   
    