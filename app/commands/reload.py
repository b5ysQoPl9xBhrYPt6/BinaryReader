from ..settings import *
from ..reset import *
from ..interface import *
import os

def reload_command(address_point: int, selected_address: int = -1) -> None:
    show_page(address_point, selected_address = selected_address if selected_address != -1 else None)