from .settings import *
import sys, os, time

print('Loading your file...')
data: list[str] = get_binary_hex_data(file)

def show_page(address_point: int = 0, raise_error: int | None = None) -> int:
    show_app_bar()
    show_stack_info_bar()
    errid = 0
    if address_point < 0:
        errid = 2
    try:
        (lambda: data[address_point * stack_size])()
    except IndexError:
        errid = 1
    if raise_error != None:
        errid = raise_error

    for ycor in range(os.get_terminal_size()[1] - page_padding):
        address = (address_point + ycor) * stack_size
        hex_address = hex(address).split("0x")[-1].upper()
        print(clr.Back.BLUE + clr.Fore.WHITE + '0x' + ''.join(['0' for _ in range(address_size - len(hex_address))]) + hex_address + clr.Back.RESET + clr.Fore.RESET, end = ' ')
        for bi in range(stack_size):
            if errid == 0:
                show_byte(address + bi)
            else:
                print('00', end = ' ')
        print(end = '\t')
        for bi in range(stack_size):
            if errid == 0:
                show_char(address + bi)
            else:
                print('.', end = '')
        print()

    match errid:
        case 1:
            print(clr.Fore.RED + "Error: Address out of bounds.", clr.Fore.RESET)
        case 2:
            print(clr.Fore.RED + "Error: Address cannot be negative.", clr.Fore.RESET)
        case 3:
            print(clr.Fore.RED + "Error: Invalid command. Type 'help' to get a command list.", clr.Fore.RESET)
        case 4:
            print(clr.Fore.RED + "Error: Invalid command arguments. Type 'help' to get a command list.", clr.Fore.RESET)
        
        case 0:
            pass
        case _:
            print(clr.Fore.RED + "Error: Unknown error.", clr.Fore.RESET)

    return errid

def show_char(char_index: int) -> None:
    char = chr(int(data[char_index], 16))
    print(char if char.isprintable() else '.', end = '')

def show_byte(byte_index: int) -> None:
    print(data[byte_index], end = ' ')

def show_stack_info_bar() -> None:
    print(clr.Back.LIGHTBLACK_EX + clr.Fore.BLACK + ''.join([' ' for _ in range(address_size + 2)]) + clr.Back.BLUE, end = ' ')
    for cell in range(stack_size):
        print(f'{cell:02x}'.upper(), end = '')
        if not cell == stack_size -1:
            print(end = ' ')
    print(clr.Back.RESET, end = '')
    print(end = '\t')

    filename = os.path.basename(file)
    blank = ''.join([' ' for _ in range(stack_size // 2 - len(filename) // 2)])
    print(clr.Back.LIGHTWHITE_EX + blank + filename + ''.join([' ' for _ in range(stack_size - len(blank + filename))]) + clr.Back.RESET, end = '')
    print()

def show_app_bar() -> None:
    active_console_width: int = address_size + 2 + (stack_size * 3) + 6 + stack_size
    blank = ''.join([' ' for _ in range(active_console_width // 2 - len(title) // 2)])
    blank_version = ''.join([' ' for _ in range(active_console_width // 2 - len(title) // 2 - len(version))])
    print(clr.Back.WHITE + clr.Fore.BLACK + version + blank_version + title + blank + clr.Back.RESET + clr.Fore.RESET)