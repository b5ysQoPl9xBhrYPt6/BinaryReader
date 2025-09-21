from .interface import *
from .reset import *
from .commands import *
import sys, os, colorama as clr

def run() -> None:
    reset()
    if address_size + 2 + (stack_size * 3) + 6 + stack_size < os.get_terminal_size()[0]:
        show_page(0)
    else:
        print(Style.ERROR + "Error: Terminal window is too small. Resize your window and type 'reload'." + clr.Fore.RESET)
    while True:
        try:
            command = input('>')
        except KeyboardInterrupt:
            reset()
            sys.exit()
        
        reset()
        if address_size + 2 + (stack_size * 3) + 6 + stack_size < os.get_terminal_size()[0]:
            check_command(command)
        else:
            print(Style.ERROR + "Error: Terminal window is too small. Resize your window and type 'reload'." + clr.Fore.RESET)
        
def check_command(string: str) -> None:
    string = string.lower()
    strings = string.split(' ')
    match strings[0]:
        case "jmp" | "jump":
            jmp_command(strings)
        case "reload":
            reload_command(0)  # replace with current address index later
        case _:
            show_page(0, raise_error = 3)