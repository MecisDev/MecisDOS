import time
import os
import psutil
from datetime import datetime

os.system('cls')
print("Welcome to ")
print("FatCisDos 12")
print("Build 1200")
time.sleep(2)
now = datetime.now()

current_time = now.strftime("%H:%M")
print("Time is " +current_time)
print("Loading...")
time.sleep(0.2)
print("One little bit...")
time.sleep(1)
os.system('cls')
print("Welcome to FatCisDOS 12! this is dos adapted to run on modern os's. This project use GNU GPL 3")
while True:
    com1 = input("root@fatcisdos:>/ ")
    if com1 == "test":
        print("Test command")
    if com1 == "ver":
        print("FatCisDOS 12")
        print("Build 1200")
        print("©FatCisDev.")
    if com1 == "exit":
        os.system('cls')
        break
    if com1 == "clear":
        os.system('cls')
    if com1 == "reset":
        os.system("python dos.py")
        break
    if com1 == "dir":
        os.system("dir")
    if com1 == "help":
        print ("comands:")
        print ("help - this command            dir - view files on this category")
        print ("reset - restart the dos    clear - clear all messeges on the dos")
        print ("test - test command         exit - exit the dos")
        print ("ver - version            vk - Mecis Software VK Group")
        print ("info - DOS Information      authors - DOS Authors")
        print ("color green,blue or gray - making DOS green, blue and gray!")
        print ("echo - repeats words   notepad - opening windows notepad")
        print ("time - shows the time  mspaint - starts microsoft paint")
    if com1 == "authors":
        print ("Nikita Rojdestvin - Versions until 8.0.1")
        print ("Artem Litvinsev - Versions from 8.1. FatCisDev Owner")
        print ("Seva Tretyakov - Former Coder. XDAFAD Software Owner")
    if com1 == "info":
        print("FatCisDOS is a DOS without installing By FatCisDev (Former MECIS Software). you must be write in cmd or terminal python dos.py and it starts.")

    if com1 == "kakish":
        print("ugh. ugh. ugh.")
    if com1 == "color green":
        os.system("color 2")
    if com1 == "color blue":
        os.system("color 1")
    if com1 == "color gray":
        os.system("color 8")
    if com1 == "notepad":
        os.system("notepad")
    if com1 == "echo":
        word = input("what word do you need?: ")
        os.system("echo " +word)
    if com1 == "cmd":
        com = input("what command do you need?: ")
        os.system(com)
    if com1 == "mspaint":
        os.system("mspaint")
    if com1 == "time":
        now = datetime.now()

        current_time = now.strftime("%H:%M")
        print("Current Time: ", current_time)
    if com1 == "fatcis":
        print("https://vk.com/fatcisdev")


        

