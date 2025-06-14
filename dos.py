import os
import time
import shutil
from datetime import datetime

# --- Core Functions ---

def clear_screen():
    """Clears the terminal screen."""
    # Works on Windows, macOS, and Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def print_welcome():
    """Prints the initial welcome message and startup sequence."""
    clear_screen()
    print("Welcome to")
    print("MecisDOS Devoloper Preview")
    print("Build 1258")
    time.sleep(2)
    
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print(f"Time is {current_time}")
    time.sleep(2)
    
    clear_screen()
    print("Welcome to MecisDOS 14! This is an OS emulator written in Python.")
    print("Type 'help' for a list of commands.")

# --- Command Functions ---

def do_ver(*args):
    """Prints the OS version and build information."""
    print("MecisDOS Devoloper Preview")
    print("Build 1258")
    print("©MECIS.")

def do_help(*args):
    """Displays a list of available commands."""
    print("Available commands:")
    print("  help      - Shows this help message.")
    print("  ver       - Displays the version information.")
    print("  info      - Shows information about MecisDOS.")
    print("  authors   - Lists the authors of the project.")
    print("  license   - Displays the project's license information.")
    print("  github    - Shows the link to the project's GitHub repository.")
    print("  time      - Shows the current time.")
    print("  echo      - Repeats the words you type after it (e.g., echo hello world).")
    print("  clear     - Clears the screen.")
    print("  exit      - Exits the MecisDOS emulator.")
    print("\nFile & Directory Commands:")
    print("  dir       - Lists files and directories in the current location.")
    print("  cd        - Changes the current directory (e.g., cd my_folder).")
    print("  mkdir     - Creates a new directory (e.g., mkdir new_folder).")
    print("  rmdir     - Removes an empty directory (e.g., rmdir old_folder).")
    print("  touch     - Creates a new empty file (e.g., touch new_file.txt).")
    print("  del       - Deletes a file (e.g., del old_file.txt).")
    print("  rename    - Renames a file (e.g., rename old.txt new.txt).")
    print("  copy      - Copies a file (e.g., copy source.txt destination.txt).")
    print("  move      - Moves a file (e.g., move source.txt destination_folder/).")
    print("  note      - A simple text editor (e.g., note my_document.txt).")


def do_info(*args):
    """Prints information about the OS."""
    print("MecisDOS is a DOS emulator by MECIS Dev. Use the 'help' command to see all commands. Enjoy!")

def do_authors(*args):
    """Prints the authors' names."""
    print("Nikita Rojdestvin - Versions until 8.0.1")
    print("Artem Litvinsev - Versions from 8.1. MECIS Dev Owner")
    print("Seva Tretyakov - Former Coder. XDAFAD Software Owner")

def do_license(*args):
    """Prints license information."""
    print("The Project uses the GNU GPL 3 License. This means you can fork, modify, and release it.")
    print("However, you must publish it as Open Source, not as proprietary code.")
    print("You should also credit the original authors (use the 'authors' command).")

def do_github(*args):
    """Prints the GitHub repository link."""
    print("https://github.com/MecisDev/MecisDOS/")

def do_time(*args):
    """Displays the current time."""
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Current Time: {current_time}")

def do_echo(*args):
    """Prints the arguments back to the console."""
    if not args:
        print("Usage: echo <text to repeat>")
    else:
        # Join all arguments into a single string
        print(" ".join(args))
        
def do_dir(*args):
    """Lists the contents of the current directory."""
    print(f"Directory of {os.getcwd()}:\n")
    try:
        for item in os.listdir("."):
            if os.path.isdir(item):
                print(f"<DIR>  {item}")
            else:
                print(f"       {item}")
    except OSError as e:
        print(f"Error: {e}")


def do_cd(*args):
    """Changes the current working directory."""
    if not args:
        print("Usage: cd <directory_path>")
        return
    directory = args[0]
    try:
        os.chdir(directory)
        print(f"Current directory: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
    except NotADirectoryError:
        print(f"Error: '{directory}' is not a directory.")
    except OSError as e:
        print(f"Error changing directory: {e}")

def do_mkdir(*args):
    """Creates a new directory."""
    if not args:
        print("Usage: mkdir <directory_name>")
        return
    directory = args[0]
    try:
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")
    except FileExistsError:
        print(f"Error: The directory '{directory}' already exists.")
    except OSError as e:
        print(f"Error creating directory: {e}")

def do_rmdir(*args):
    """Removes an empty directory."""
    if not args:
        print("Usage: rmdir <directory_name>")
        return
    directory = args[0]
    try:
        os.rmdir(directory)
        print(f"Directory '{directory}' removed.")
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
    except OSError:
        # This error often means the directory is not empty
        print(f"Error: Could not remove '{directory}'. It may not be empty.")

def do_touch(*args):
    """Creates an empty file."""
    if not args:
        print("Usage: touch <filename>")
        return
    file_path = args[0]
    if os.path.exists(file_path):
        print(f"Error: File '{file_path}' already exists.")
    else:
        try:
            with open(file_path, 'w') as f:
                pass  # Create the file
            print(f"File '{file_path}' created.")
        except OSError as e:
            print(f"Error creating file: {e}")

def do_del(*args):
    """Deletes a file."""
    if not args:
        print("Usage: del <filename>")
        return
    file_path = args[0]
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
    elif os.path.isdir(file_path):
         print(f"Error: '{file_path}' is a directory. Use 'rmdir' to remove directories.")
    else:
        try:
            os.remove(file_path)
            print(f"File '{file_path}' deleted.")
        except OSError as e:
            print(f"Error deleting file: {e}")

def do_rename(*args):
    """Renames a file."""
    if len(args) != 2:
        print("Usage: rename <old_name> <new_name>")
        return
    old_name, new_name = args
    try:
        os.rename(old_name, new_name)
        print(f"Renamed '{old_name}' to '{new_name}'.")
    except FileNotFoundError:
        print(f"Error: The file '{old_name}' does not exist.")
    except OSError as e:
        print(f"Error renaming file: {e}")

def do_copy(*args):
    """Copies a file."""
    if len(args) != 2:
        print("Usage: copy <source_file> <destination_file_or_dir>")
        return
    source, dest = args
    try:
        shutil.copy2(source, dest) # copy2 preserves metadata
        print(f"Copied '{source}' to '{dest}'.")
    except FileNotFoundError:
        print(f"Error: The source file '{source}' was not found.")
    except shutil.SameFileError:
        print("Error: Source and destination are the same file.")
    except OSError as e:
        print(f"Error copying file: {e}")

def do_move(*args):
    """Moves a file."""
    if len(args) != 2:
        print("Usage: move <source_file> <destination_file_or_dir>")
        return
    source, dest = args
    try:
        shutil.move(source, dest)
        print(f"Moved '{source}' to '{dest}'.")
    except FileNotFoundError:
        print(f"Error: The source file '{source}' was not found.")
    except OSError as e:
        print(f"Error moving file: {e}")

def do_note(*args):
    """A simple text editor."""
    if not args:
        print("Usage: note <filename>")
        return
    
    filename = args[0]
    print(f"--- MecisDOS Note: {filename} ---")
    print("Enter your text. Type SAVE on a new line to save and exit.")
    print("-----------------------------------")
    
    lines = []
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                lines = f.read().splitlines()
                for line in lines:
                    print(line)
        except OSError as e:
            print(f"Error reading existing file: {e}")
            return
    
    # Reset lines for new input
    lines = []
    while True:
        try:
            line = input()
            if line.strip().upper() == "SAVE":
                break
            lines.append(line)
        except EOFError: # Ctrl+D
            break
            
    try:
        with open(filename, 'w') as f:
            f.write('\n'.join(lines))
        print(f"File '{filename}' saved successfully.")
    except OSError as e:
        print(f"Error saving file: {e}")

# --- Main Application Logic ---

def main():
    """The main function and command loop."""
    
    # A dictionary mapping command strings to functions.
    # This makes it easy to add new commands.
    commands = {
        "ver": do_ver,
        "help": do_help,
        "info": do_info,
        "authors": do_authors,
        "license": do_license,
        "github": do_github,
        "time": do_time,
        "clear": lambda *args: clear_screen(),
        "cls": lambda *args: clear_screen(), # Alias for clear
        "echo": do_echo,
        "dir": do_dir,
        "ls": do_dir, # Alias for dir
        "cd": do_cd,
        "mkdir": do_mkdir,
        "rmdir": do_rmdir,
        "touch": do_touch,
        "del": do_del,
        "rm": do_del, # Alias for del
        "rename": do_rename,
        "mv": do_move, # Alias for move
        "move": do_move,
        "copy": do_copy,
        "cp": do_copy, # Alias for copy
        "note": do_note,
    }

    print_welcome()
    
    while True:
        # Get the current working directory to show in the prompt
        cwd = os.path.basename(os.getcwd())
        prompt = f"root@mecisdos:{cwd}> "
        
        full_command = input(prompt).strip()
        
        if not full_command:
            continue

        # Split the input into the command and its arguments
        parts = full_command.split()
        command = parts[0].lower()
        args = parts[1:]

        if command == "exit":
            clear_screen()
            break
        
        # Find the function to execute from the dictionary
        func_to_run = commands.get(command)
        
        if func_to_run:
            try:
                # Call the function, passing the arguments
                func_to_run(*args)
            except Exception as e:
                # Catch-all for any unexpected errors in command functions
                print(f"An unexpected error occurred: {e}")
        else:
            print(f"Error: Command '{command}' not found. Type 'help' for a list of commands.")

# --- Script Entry Point ---
if __name__ == "__main__":
    main()
