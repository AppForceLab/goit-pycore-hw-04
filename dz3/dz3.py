import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True) 

def print_directory_contents(path, prefix=''):
    try:
        base_path = Path(path)
        if not base_path.exists():
            print("The specified path does not exist.")
            return
        if not base_path.is_dir():
            print("The specified path is not a directory.")
            return
        
        for item in base_path.iterdir():
            new_prefix = prefix + "┣ " if prefix else ""
            if item.is_dir():
                print(f"{prefix}{Fore.BLUE}{item.name}")
                print_directory_contents(item, prefix + "┃ ")
            else:
                print(f"{prefix}{Fore.GREEN}{item.name}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dz3.py /path/to/directory")
    else:
        directory_path = sys.argv[1]
        print_directory_contents(directory_path)
