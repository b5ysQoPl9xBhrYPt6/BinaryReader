from .settings import *
from .tools import *
import sys, os

print('Loading your file...')
reader = BufferedHexReader(file, buffer_size = 8192)


def show_page(address_point: int = 0, raise_error: int | None = None, selected_address: int | None = None) -> int:
    _show_app_bar()
    _show_stack_info_bar()
    errid = 0
    if address_point < 0:
        errid = 2
    try:
        reader.get_byte(address_point * stack_size)
    except IndexError:
        errid = 1
    if raise_error != None:
        errid = raise_error

    for ycor in range(os.get_terminal_size()[1] - page_padding):
        address = (address_point + ycor) * stack_size
        hex_address = hex(address).split("0x")[-1].upper()
        print(
            Style.ADDRESS
            + '0x' + ''.join(['0' for _ in range(address_size - len(hex_address))]) + hex_address
            + clr.Back.RESET + clr.Fore.RESET,
            end = ' '
        )
        for bi in range(stack_size):
            if errid == 0 or errid == 3 or errid == 4:
                if selected_address is not None and address == selected_address:
                    _show_byte(address + bi, selected = True)
                else:
                    _show_byte(address + bi)
            else:
                print(Style.BYTE_OUT_OF_BOUNDS + '00' + clr.Fore.RESET, end = ' ')
        print(end = '\t')
        for bi in range(stack_size):
            if errid == 0 or errid == 3 or errid == 4:
                if selected_address is not None and address == selected_address:
                    _show_char(address + bi, selected = True)
                else:
                    _show_char(address + bi)
            else:
                print(Style.BYTE_OUT_OF_BOUNDS + '.' + clr.Fore.RESET, end = '')
        print()

    match errid:
        case 1:
            print(Style.ERROR + "Error: Address out of bounds.", clr.Fore.RESET)
        case 2:
            print(Style.ERROR + "Error: No message available.", clr.Fore.RESET)
        case 3:
            print(Style.ERROR + "Error: Invalid command. Type 'help' to get a command list.", clr.Fore.RESET)
        case 4:
            print(Style.ERROR + "Error: Invalid command arguments. Type 'help' to get a command list.", clr.Fore.RESET)
        
        case 0:
            print(Style.MESSAGE + "Type a command. Ctrl + C to exit.")
        case _:
            print(Style.ERROR + "Error: Unknown error.", clr.Fore.RESET)

    return errid

def _show_char(char_index: int, selected: bool = False) -> None:
    try:
        char = chr(int(reader.get_byte(char_index), 16))
        if selected:
            print(Style.SELECTED_BYTE, end = '')
        print(char if char.isprintable() else '.', end = '')
        print(clr.Fore.RESET, end = '')
    except IndexError:
        print(Style.BYTE_OUT_OF_BOUNDS + '.' + clr.Fore.RESET, end = '')

def _show_byte(byte_index: int, selected: bool = False) -> None:
    try:
        if selected:
            print(Style.SELECTED_BYTE, end = '')
        print(reader.get_byte(byte_index), end = ' ')
        print(clr.Fore.RESET, end = '')
    except IndexError:
        print(Style.BYTE_OUT_OF_BOUNDS + '00' + clr.Fore.RESET, end = ' ')

def _show_stack_info_bar() -> None:
    print(
        Style.ADDRESS_BLANK
        + ''.join([' ' for _ in range(address_size + 2)])
        + Style.STACK_BYTE_NUM,
        end = ' '
    )
    for cell in range(stack_size):
        print(f'{cell:02x}', end = '')
        if not cell == stack_size -1:
            print(end = ' ')
    print(clr.Back.RESET, end = '')
    print(end = '\t')

    fileinfo = f'File size: {os.path.getsize(file) / 1024} KB'
    if len(fileinfo) > stack_size - 3:
        fileinfo = fileinfo[:stack_size-3] + '...'
    blank = ''.join([' ' for _ in range(stack_size // 2 - len(fileinfo) // 2)])
    print(
        Style.FILE_NAME
        + blank + fileinfo + ''.join([' ' for _ in range(stack_size - len(blank + fileinfo))])
        + clr.Back.RESET,
        end = ''
    )
    print()

def _show_app_bar() -> None:
    active_console_width: int = address_size + 2 + (stack_size * 3) + 6 + stack_size
    blank = ''.join([' ' for _ in range(active_console_width // 2 - len(title) // 2)])
    blank_version = ''.join([' ' for _ in range(active_console_width // 2 - len(title) // 2 - len(version))])
    print(
        Style.TITLE
        + version + blank_version + title + blank
        + clr.Back.RESET + clr.Fore.RESET
    )