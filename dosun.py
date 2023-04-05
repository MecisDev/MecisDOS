import time
import os
from datetime import datetime

os.system('cls')
print("Welcome to ")
print("FatCisDOS Unix-Based Edition")
print("Build 1210")
time.sleep(2)
now = datetime.now()

current_time = now.strftime("%H:%M")
print("Time is " +current_time)
print("Loading...")
time.sleep(0.2)
print("One little bit...")
time.sleep(1)
os.system('clear')
print("Welcome to MecisDOS 12 Unix-Based Edition, this is dos adapted to run on modern os's. This project use GNU GPL 3")
while True:
    com1 = input("/")
    if com1 == "test":
        print("Test command")
    if com1 == "ver":
        print("FatCisDos 12 Unix-Based Edition")
        print("Build 1210")
        print("©FatCisDev.")
    if com1 == "exit":
        os.system('exit')
        break
    if com1 == "clear":
        os.system('clear')
    if com1 == "reset":
        os.system("python dos.py")
        break
    if com1 == "dir":
        os.system("dir")
    if com1 == "help":
        print ("comands:")
        print ("help - comands             dir - view files on this dir")
        print ("reset - restart the dos    clear - clear all messege on the dos")
        print ("test - test comand         exit - exit the dos")
        print ("ver - version             time - shows the time")
        print ("info - DOS Information      authors - DOS Authors")
        print ("echo - repeats words    vk - FatCisDev VK Group")
    if com1 == "authors":
        print ("Nikita Rojdestvin - Versions until 8.0.1")
        print ("Artem Litvinsev - Versions from 8.1. FatCisDev Owner")
        print ("Seva Tretyakov - Former Coder. XDAFAD Software Owner")
    if com1 == "info":
        print("MecisDOS is a DOS without installing By Mecis Software. you must be write in cmd or terminal python dos.py and it starts.")

    if com1 == "kakish":
        print("ugh. ugh. ugh.")
    if com1 == "color green":
        os.system("color 2")
    if com1 == "color blue":
        os.system("color 1")
    if com1 == "color gray":
        os.system("color 8")
    if com1 == "term":
        com = input("what command do you need?: ")
        os.system(com)
    if com1 == "echo":
        word = input("what word do you need?: ")
        os.system("echo " +word)
    if com1 == "time":
        now = datetime.now()

        current_time = now.strftime("%H:%M")
        print("Current Time: ", current_time)
    if com1 == "mecis":
        print("https://vk.com/fatcisdev")


        
