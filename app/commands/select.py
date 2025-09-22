from ..settings import *
from ..interface import *

def select_command(strings: list[str], current_address_point: int) -> bool:
    if len(strings) == 2:
        try:
            show_page(current_address_point, selected_address = int(strings[1]) // stack_size)
            return True
        except ValueError:
            try:
                show_page(current_address_point, selected_address = int(strings[1], 16) // stack_size)
                return True
            except ValueError:
                show_page(current_address_point, raise_error = 4)
                return False
    else:
        show_page(current_address_point, raise_error = 4)
        return False