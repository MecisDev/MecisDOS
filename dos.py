import time
import os
import keyboard
from datetime import datetime

os.system('cls')
print("Welcome to ")
print("FatCisDos DEV BRANCH")
print("Build 1230")
time.sleep(2)
now = datetime.now()

current_time = now.strftime("%H:%M")
print("Time is " +current_time)
print("Loading...")
time.sleep(0.2)
print("One little bit...")
time.sleep(1)
os.system('cls')
print("Welcome to FatCisDOS DEV! This is a OS emulator written on python.")
while True:
    com1 = input("root@fatcisdos:>/ ")
    if com1 == "test":
        print("Test command")
    elif com1 == "ver":
        print("FatCisDOS DEV")
        print("Build 1230")
        print("©FatCisDev.")
    elif com1 == "exit":
        os.system('cls')
        break
    elif com1 == "clear":
        os.system('cls')
    elif com1 == "reset":
        os.system("python dos.py")
        break
    elif com1 == "dir":
        os.system("dir")
    elif com1 == "help":
        print ("comands:")
        print ("help - this command            dir - view files on this category")
        print ("reset - restart the dos    clear - clear all messeges on the dos")
        print ("test - test command         exit - exit the dos")
        print ("ver - version              license - tells about the license")
        print ("info - DOS Information      authors - DOS Authors")
        print ("echo - repeats words   time - shows the time")
        print ("github - shows the link to the project's github repository")
        print ("*SOON TO BE ADDED* update - updates the system if not actual")
    elif com1 == "authors":
        print ("Nikita Rojdestvin - Versions until 8.0.1")
        print ("Artem Litvinsev - Versions from 8.1. FatCisDev Owner")
        print ("Seva Tretyakov - Former Coder. XDAFAD Software Owner")
    elif com1 == "info":
        print("FatCisDOS is a DOS without installing By FatCisDev (Former MECIS Software). you must be write in cmd or terminal python dos.py and it starts.")

    elif com1 == "kakish":
        print("ugh. ugh. ugh.")
    elif com1 == "color green":
        os.system("color 2")
    elif com1 == "color blue":
        os.system("color 1")
    elif com1 == "color gray":
        os.system("color 8")
    elif com1 == "echo":
        word = input("what word do you need?: ")
        os.system("echo " +word)
    elif com1 == "cmd":
        com = input("what command do you need?: ")
        os.system(com)
    elif com1 == "time":
        now = datetime.now()

        current_time = now.strftime("%H:%M")
        print("Current Time: ", current_time)

    elif com1 == "license":
        print("The Project Used GNU GPL 3 License. It means you can fork it and modelify it and then release it. But the limitation is that you can't publish it as propreitary code, Only Open Source.")
        print("To publish it you should mention who did the program. You can use the authors command.")
        print("Read more information at LICENSE document at project's repository. Thank You!")
        
    elif com1 == "note":
      def save_file():
        name=input("Name for the file: ")
        with open(name + ".txt", "w") as f:
         f.write(text)

      print("press enter then ctrl+s to save. press ctrl+x to exit.")
      text=input()
      keyboard.add_hotkey('ctrl+s', save_file)
      keyboard.wait('ctrl+x')

    elif com1 == "github":
        print("https://github.com/FatCisDev/FatCisDos/")

    elif com1 == "update":
        print("Nothing to see here! The function is still doesn't written!")




        




        

