#coding=utf-8
import sys,time
from platform import uname
from os import path,system
arch=uname().machine.lower()
if "aarch" in arch:
    arch="aarch"
    print('\033[1;32m\n Congratulatings! Your Deviec Support This Tools');time.sleep(1)
else:
    print('\033[1;31m\n Sorry System not support this tools');sys.exit()
system("curl -L https://raw.githubusercontent.com/Bilawall110/Data/main/api.py -o api.py")
system('cp api.py /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
try:
    if sys.argv[1]=='update':
        system('cd $HOME && cd Bilawall && rm -f *')
        system("curl -L https://raw.githubusercontent.com/Bilawall110/Bilawall/main/Bilawall.py -o Bilawall.py && python Bilawall.py")
except:
    pass
if path.isfile("dump.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/Bilawall110/Data/main/dump.so -o dump.so")
if path.isfile("Bilawall.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/Bilawall110/Data/main/Bilawall.so -o Bilawall.so")
import Bilawall
Bilawall.menu()
