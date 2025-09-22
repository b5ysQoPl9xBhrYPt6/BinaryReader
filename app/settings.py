import colorama as clr

clr.init()


file:                str = r"C:\Windows\System32\cmd.exe"
address_size:        int = 8
stack_size:          int = 32
page_padding:        int = 4

title:               str = 'BinaryReader'
version:             str = 'V1.0 : commit 7 : master'

class Style:
    TITLE:               str = clr.Back.WHITE         + clr.Fore.BLACK
    ADDRESS_BLANK:       str = clr.Back.LIGHTBLACK_EX #
    STACK_BYTE_NUM:      str = clr.Back.BLUE          + clr.Fore.BLACK
    FILE_NAME:           str = clr.Back.LIGHTWHITE_EX + clr.Fore.BLACK
    ADDRESS:             str = clr.Back.BLUE          + clr.Fore.WHITE
    ERROR:               str = clr.Fore.RED           #
    BYTE_OUT_OF_BOUNDS:  str = clr.Fore.LIGHTRED_EX   #
    MESSAGE:             str = clr.Fore.LIGHTBLACK_EX #
    INPUT:               str = clr.Fore.WHITE         #
    SELECTED_BYTE:       str = clr.Fore.YELLOW         #
