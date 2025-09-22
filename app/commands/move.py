from ..settings import *
from ..interface import *
from .jmp import *

def move_command(strings: list[str], current_address_point: int, displace: int | str, selected_address: int = -1) -> int | None:
    if len(strings) == 2:
        try:
            address = current_address_point + int(displace)
            show_page(address, selected_address = selected_address if selected_address != -1 else None)
            return address
        except ValueError:
            try:
                address = current_address_point + int(str(displace), 16)
                show_page(address, selected_address = selected_address if selected_address != -1 else None)
                return address
            except ValueError:
                show_page(current_address_point, raise_error = 4)
    else:
        show_page(current_address_point, raise_error = 4)