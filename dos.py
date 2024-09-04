import time
import os
import keyboard
from datetime import datetime

os.system('cls')
print("Welcome to ")
print("FatCisDos 12")
print("Build 1225")
time.sleep(2)
now = datetime.now()

current_time = now.strftime("%H:%M")
print("Time is " +current_time)
print("Loading...")
time.sleep(0.2)
print("One little bit...")
time.sleep(1)
os.system('cls')
print("Welcome to FatCisDOS 12.1! this is dos adapted to run on modern os's.")
while True:
    com1 = input("root@fatcisdos:>/ ")
    if com1 == "test":
        print("Test command")
    if com1 == "ver":
        print("FatCisDOS 12.1")
        print("Build 1225")
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
        print ("ver - version              license - tells about the license")
        print ("info - DOS Information      authors - DOS Authors")
        print ("echo - repeats words   time - shows the time")
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
    if com1 == "echo":
        word = input("what word do you need?: ")
        os.system("echo " +word)
    if com1 == "cmd":
        com = input("what command do you need?: ")
        os.system(com)
    if com1 == "time":
        now = datetime.now()

        current_time = now.strftime("%H:%M")
        print("Current Time: ", current_time)
    if com1 == "note":
      def save_file():
        name=input("Name for the file: ")
        with open(name + ".txt", "w") as f:
         f.write(text)

    if com1 == "license":
        print("The Project Used GNU GPL 3 License. It means you can fork it and modify it and then release it. But the limitation is that you can't publish it as propreitary code, Only Open Source.")
        print("To publish it you should mention who did the program. You can use the "authors" command. Thank you!")

      print("press enter then ctrl+s to save. press ctrl+x to exit.")
      text=input()
      keyboard.add_hotkey('ctrl+s', save_file)
      keyboard.wait('ctrl+x')


        



        

