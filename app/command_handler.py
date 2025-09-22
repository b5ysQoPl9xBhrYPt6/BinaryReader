from .interface import *
from .reset import *
from .commands import *
import sys, os, colorama as clr

current_address:  int = 0
selected_address: int = -1

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
    global current_address, selected_address
    string = string.lower()
    strings = string.split(' ')
    match strings[0]:
        case "jmp" | "jump":
            address = jmp_command(strings, selected_address = selected_address)
            if address is not None:
                current_address = address
        case "reload":
            reload_command(current_address, selected_address = selected_address)
        case "move" | "mv":
            result = move_command(strings, current_address, strings[1], selected_address = selected_address)
            if result is not None:
                current_address = result
        case "select" | "sel":
            success = select_command(strings, current_address)
            if success:
                try:
                    selected_address = int(strings[1])
                    show_page(current_address, selected_address = selected_address)
                except ValueError:
                    selected_address = int(strings[1], 16)
                    show_page(current_address, selected_address = selected_address)
        case "done":
            selected_address = -1
            show_page(current_address)
        case _:
            show_page(current_address, raise_error = 3)