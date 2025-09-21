from ..settings import *
from ..reset import *
from ..interface import *
import os

def reload_command(address_point: int) -> None:
    reset()
    show_page(address_point)