import requests
import shutil
import pyshorteners
import time
import itertools
import threading
import sys



COLORS = {
    "black": "\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33;1m",
    "blue": "\u001b[34;1m",
    "Bright Yellow": "\u001b[33;1m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "yellow-background": "\u001b[43m",
    "black-background": "\u001b[40m",
    "cyan-background": "\u001b[46;1m",
}

def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text


code = "[[blue]]Your[[red]] QrCode[[white]]"
qr = colorText(code)

su = "[[blue]]The Shortened[[red]] URL[[white]] is: "
shorturltxt = colorText(su)

re = "[[green]] (Recommended)"
Recommended = colorText(re)

baner = """"
  ____                                 ___       
 |  _ \ ___ _ __ ___  ___ _   _ ___ [[Bright Yellow]]  / _ \ _ __ 
 | |_) / _ | '__/ __|/ _ | | | / __|[[Bright Yellow]] | | | | '__|
 |  __|  __| |  \__ |  __| |_| \__ \[[Bright Yellow]] | |_| | |   
 |_|   \___|_|  |___/\___|\__,_|___/[[Bright Yellow]]  \__\_|_|   
                                                 
"""
banner = colorText(baner)

print(banner)

x = input("Url: ")


normalurl = "https://api.qrserver.com/v1/create-qr-code/?size450x450&data="+str(x)
shorturl = "https://api.qrserver.com/v1/create-qr-code/?size450x450&data="+str(x)
print(f"{qr} https://api.qrserver.com/v1/create-qr-code/?size450x450&data="+str(x))

urlshort = shorturl

long_url = urlshort

type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)
print(shorturltxt + short_url + Recommended)


url = normalurl
file_name = "qrocde.png"
res = requests.get(url, stream = True)

if res.status_code == 200:
    with open(file_name,'wb') as f:
        shutil.copyfileobj(res.raw, f)
else:
    print('Image Couldn\'t be retrieved')


url1 = shorturl
file_name = "qrocde(shorturl).png"
res = requests.get(url, stream = True)

if res.status_code == 200:
    with open(file_name,'wb') as f:
        shutil.copyfileobj(res.raw, f)
else:
    print('Image Couldn\'t be retrieved')
