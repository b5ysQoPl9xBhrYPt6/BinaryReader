from .interface import *
from .reset import *
from .commands import *
import sys, os, colorama as clr

current_address: int = 0

def run() -> None:
    reset()
    if address_size + 2 + (stack_size * 3) + 6 + stack_size < os.get_terminal_size()[0]:
        show_page(0)
    else:
        print(Style.ERROR + "Error: Terminal window is too small. Resize your window and type 'reload'." + clr.Fore.RESET)
    while True:
        try:
            command = input(Style.INPUT + file + '>')
        except KeyboardInterrupt:
            reset()
            sys.exit()
        
        reset()
        if address_size + 2 + (stack_size * 3) + 6 + stack_size < os.get_terminal_size()[0]:
            check_command(command)
        else:
            print(Style.ERROR + "Error: Terminal window is too small. Resize your window and type 'reload'." + clr.Fore.RESET)
        
def check_command(string: str) -> None:
    global current_address
    string = string.lower()
    strings = string.split(' ')
    match strings[0]:
        case "jmp" | "jump":
            address = jmp_command(strings)
            if address is not None:
                current_address = address
        case "reload":
            reload_command(current_address)
        case _:
            show_page(current_address, raise_error = 3)