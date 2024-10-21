import time
import os
from datetime import datetime

try:
    import keyboard
except ImportError:
    print("The 'keyboard' module is not installed. Please install it using 'pip install keyboard'.")

os.system('cls')
print("Welcome to ")
print("MecisDOS 14")
print("Build 1251")
time.sleep(2)
now = datetime.now()

current_time = now.strftime("%H:%M")
print("Time is " + current_time)
time.sleep(2)
os.system('cls')
print("Welcome to MecisDOS 14! This is an OS emulator written in Python.")
while True:
    com1 = input("root@mecisdos:>/ ")
    if com1 == "test":
        print("Test command")
    elif com1 == "ver":
        print("MecisDOS 14")
        print("Build 1251")
        print("©MECIS.")
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
        print("commands:")
        print("help - this command            dir - view files on this category")
        print("reset - restart the dos    clear - clear all messages on the dos")
        print("test - test command         exit - exit the dos")
        print("ver - version              license - tells about the license")
        print("info - DOS Information      authors - DOS Authors")
        print("echo - repeats words   time - shows the time")
        print("github - shows the link to the project's github repository")
        print("note - note app        mkdir - create a folder")
        print("rmdir - remove a folder     cd - change directory")
        print("rename - rename a file      del - delete a file")
        print("copy - copy a file          move - move a file")
        print("touch - create a file      custom - executes commands from real OS")
    elif com1 == "authors":
        print("Nikita Rojdestvin - Versions until 8.0.1")
        print("Artem Litvinsev - Versions from 8.1. MECIS Dev Owner")
        print("Seva Tretyakov - Former Coder. XDAFAD Software Owner")
    elif com1 == "info":
        print("MecisDOS is a DOS without installing By MECIS Dev. you must write in cmd or terminal python dos.py and it starts.")
    elif com1 == "echo":
        word = input("what word do you need?: ")
        os.system("echo " + word)
    elif com1 == "cmd":
        com = input("what command do you need?: ")
        os.system(com)
    elif com1 == "time":
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        print("Current Time: ", current_time)
    elif com1 == "license":
        print("The Project Used GNU GPL 3 License. It means you can fork it and modify it and then release it. But the limitation is that you can't publish it as proprietary code, Only Open Source.")
        print("To publish it you should mention who did the program. You can use the authors command.")
        print("Read more information at LICENSE document at project's repository. Thank You!")
    elif com1 == "note":
        def save_file():
            name = input("Name for the file: ")
            with open(name + ".txt", "w") as f:
                f.write(text)

        print("press enter then ctrl+s to save. press ctrl+x to exit.")
        text = input()
        if 'keyboard' in globals():
            keyboard.add_hotkey('ctrl+s', save_file)
            keyboard.wait('ctrl+x')
        else:
            print("The 'keyboard' module is not available.")
    elif com1 == "github":
        print("https://github.com/MecisDev/MecisDOS/")
    elif com1 == "mkdir":
        directory = input("Directory and name for the folder: ")
        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
            print("The Directory already exists!")
    elif com1 == "rmdir":
        directory = input("Directory and name for the folder: ")
        if os.path.exists(directory):
            os.rmdir(directory)
        else:
            print("The Directory does not exist!")
    elif com1 == "cd":
        directory = input("Directory and name for the folder: ")
        if os.path.exists(directory):
            os.chdir(directory)
        else:
            print("The Directory does not exist!")
    elif com1 == "rename":
        file = input("File to rename: ")
        newname = input("New name for the file: ")
        os.rename(file, newname)
    elif com1 == "del":
        file = input("File to delete: ")
        if os.path.exists(file):
            os.remove(file)
        else:
            print("The File does not exist!")
    elif com1 == "copy":
        file = input("File to copy: ")
        newfile = input("New name for the file: ")
        if os.path.exists(file):
            with open(file, "r") as f:
                with open(newfile, "w") as f1:
                    for line in f:
                        f1.write(line)
        else:
            print("The File does not exist!")
    elif com1 == "move":
        file = input("File to move: ")
        newfile = input("New name for the file: ")
        if os.path.exists(file):
            with open(file, "r") as f:
                with open(newfile, "w") as f1:
                    for line in f:
                        f1.write(line)
            os.remove(file)
        else:
            print("The File does not exist!")
    elif com1 == "touch":
        file = input("File to create: ")
        if not os.path.exists(file):
            with open(file, "w") as f:
                pass
        else:
            print("The File already exists!")

    elif com1 == "custom":
        com2 = input("Enter your command that you want to execute from the OS: ")
        os.system(com2)
        
    else:
        print("The command does not exist!")
