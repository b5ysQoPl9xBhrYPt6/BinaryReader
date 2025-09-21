import os

class BufferedHexReader:
    def __init__(self, filename: str, buffer_size: int = 4096):
        self.file = open(filename, "rb")
        self.buffer_size = buffer_size
        self.buffer: list[str] = []
        self.buffer_start = 0
        self.file_size = os.path.getsize(filename)

    def _ensure(self, pos: int, size: int = 1):
        if pos < self.buffer_start or pos + size > self.buffer_start + len(self.buffer):
            self.file.seek(pos)
            raw = self.file.read(self.buffer_size)
            self.buffer = [f"{b:02X}" for b in raw]
            self.buffer_start = pos

    def get_byte(self, pos: int) -> str:
        if pos < 0 or pos >= self.file_size:
            raise IndexError
        self._ensure(pos, 1)
        return self.buffer[pos - self.buffer_start]

    def get_size(self) -> int:
        return self.file_size

