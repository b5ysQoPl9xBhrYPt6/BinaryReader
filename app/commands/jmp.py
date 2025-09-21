from ..settings import *
from ..interface import *
import os

def jmp_command(strings: list[str]) -> int | None:
    if len(strings) == 2:
        if not strings[1] == "end":
            try:
                address = int(strings[1]) // stack_size
                show_page(address)
                return address
            except ValueError:
                try:
                    address = int(strings[1], 16) // stack_size
                    show_page(address)
                    return address
                except ValueError:
                    show_page(0, raise_error = 4)
        else:
            address = os.path.getsize(file) // stack_size - (os.get_terminal_size()[1] - page_padding) + 1
            show_page(address)
            return address
    else:
        show_page(0, raise_error = 4)