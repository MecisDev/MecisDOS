import time
import os
import psutil
from datetime import datetime

os.system('cls')
print("Welcome to ")
print("FatCisDos Dev")
print("Build 1212")
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
        print("Build 1212")
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
        print ("ver - version               time - shows the time")
        print ("info - DOS Information      authors - DOS Authors")
        print ("echo - repeats words         gui - Starts the GUI Variant (PRE-DEV)")
        print ("guireq - GUI Requirments      pip - Installs python libraries in your choice")
    if com1 == "authors":
        print ("Nikita Rojdestvin - Versions until 8.0.1")
        print ("Artem Litvinsev - Versions from 8.1. FatCisDev Owner")
        print ("Seva Tretyakov - Former Coder. XDAFAD Software Owner")
    if com1 == "info":
        print("FatCisDOS is a DOS without installing By FatCisDev (Former MECIS Software).")

    if com1 == "echo":
        word=input("Write your words:")
        print(word)
    if com1 == "command":
        com = input("Which command are you need? ")
        os.system(com)
    if com1 == "time":
        now = datetime.now()

        current_time = now.strftime("%H:%M")
        print("Current Time: ", current_time)

    if com1 == "gui":
        os.system("python3 gui.py")

    if com1 == "guireq":
        os.system("pip install pyqt6")
    
    if com1 == "pip":
        libname = input("Enter library name: ")
        os.system("pip install " + libname)


        

