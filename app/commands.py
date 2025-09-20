from .interface import *
from .reset import *
import sys, colorama as clr

def run() -> None:
    reset()
    show_page(0)
    print("Type a command. Ctrl + C to exit.")
    while True:
        try:
            command = input('>')
        except KeyboardInterrupt:
            reset()
            sys.exit()
        
        reset()
        check_command(command)
        
def check_command(string: str) -> None:
    strings = string.split(' ')
    match strings[0]:
        case "jmp" | "jump":
            if len(strings) == 2:
                try:
                    errid = show_page(int(strings[1]) // stack_size)
                    if errid == 0:
                        print("Type a command. Ctrl + C to exit.")
                except ValueError:
                    try:
                        errid = show_page(int(strings[1], 16) // stack_size)
                        if errid == 0:
                            print("Type a command. Ctrl + C to exit.")
                    except ValueError:
                        show_page(0, raise_error = 4)
            else:
                show_page(0, raise_error = 4)
        case _:
            show_page(0, raise_error = 3)