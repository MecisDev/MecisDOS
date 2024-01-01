import time
import os
import psutil
from datetime import datetime

os.system('cls')
print("Welcome to ")
print("FatCisDos Dev")
print("Build 1211")
time.sleep(2)
now = datetime.now()

current_time = now.strftime("%H:%M")
print("Time is " +current_time)
print("Loading...")
time.sleep(0.2)
print("One little bit...")
time.sleep(1)
os.system('cls')
print("Welcome to FatCisDOS Dev! This project use GNU GPL 3")
while True:
    com1 = input("root@fatcisdos:>/ ")
    if com1 == "test":
        print("Test command")
    if com1 == "ver":
        print("FatCisDOS Dev")
        print("Build 1210")
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
        print ("ver - version            vk - FatCisDev VK Group")
        print ("info - DOS Information      authors - DOS Authors")
        print ("color green,blue or gray - making DOS green, blue and gray!")
        print ("echo - repeats words        time - shows the time "   )
    if com1 == "authors":
        print ("Nikita Rojdestvin - Versions until 8.0.1")
        print ("Artem Litvinsev - Versions from 8.1. FatCisDev Owner")
        print ("Seva Tretyakov - Former Coder. XDAFAD Software Owner")
    if com1 == "info":
        print("FatCisDOS is a DOS without installing By FatCisDev (Former MECIS Software). you must be write in cmd or terminal python dos.py and it starts.")

    if com1 == "kakish":
        print("ugh. ugh. ugh.")
    if com1 == "echo":
        word=input("Write your words:")
        print(echo)
    if com1 == "command":
        com = input("Which command are you need? ")
        os.system(com)
    if com1 == "time":
        now = datetime.now()

        current_time = now.strftime("%H:%M")
        print("Current Time: ", current_time)
    if com1 == "fatcis":
        print("https://vk.com/fatcisdev")


        

