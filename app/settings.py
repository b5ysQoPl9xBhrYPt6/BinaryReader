import colorama as clr

clr.init()


file:                str = r"C:\Windows\System32\cmd.exe"
address_size:        int = 8
stack_size:          int = 32
page_padding:        int = 4

title:               str = 'BinaryReader'
version:             str = 'V1.0'


def get_binary_hex_data(file: str) -> list[str]:
    with open(file, 'rb') as f:
        data = f.read()

    bytearr: list[str] = []
    for byte in data:
        bytearr.append(f'{ord(str(chr(byte))):02x}'.upper())
    return bytearr