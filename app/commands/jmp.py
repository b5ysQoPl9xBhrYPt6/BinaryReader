from ..settings import *
from ..interface import *
import os

def jmp_command(strings: list[str]) -> None:
    if len(strings) == 2:
        if not strings[1] == "end":
            try:
                show_page(int(strings[1]) // stack_size)
            except ValueError:
                try:
                    show_page(int(strings[1], 16) // stack_size)
                except ValueError:
                    show_page(0, raise_error = 4)
        else:
            show_page(os.path.getsize(file) // stack_size - (os.get_terminal_size()[1] - page_padding) + 1)
    else:
        show_page(0, raise_error = 4)