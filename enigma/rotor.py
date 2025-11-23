from .translator import Translator
from .substitutor import MOD

class Rotor(Translator):
    def __init__(self, name: str, wiring: str, notch: str, ring_setting: int = 0, offset: int = 0):
        super().__init__(name, wiring)
        self.notch = [ord(c) - ord("A") for c in notch]
        self.ring_setting = ring_setting % MOD
        self.offset = offset % MOD
        self.log.info(f"{name} rotor ready | notch={notch}, ring={ring_setting}, offset={offset}")

    def at_notch(self) -> bool:
        return self.offset in self.notch

    def step(self):
        """סיבוב קדימה אחד (דריכה)."""
        self.offset = (self.offset + 1) % MOD
        self.log.debug(f"{self.__class__.__name__} {self.__dict__} | stepped to offset={self.offset}")

    def forward(self, i: int) -> int:
        shifted = (i + self.offset - self.ring_setting) % MOD
        j = self.forward_tbl[shifted]
        result = (j - self.offset + self.ring_setting) % MOD
        idx_to_letter = lambda x: chr(x + 65)
        self.log.debug(f"{self.__class__.__name__}.forward: {i}->{result} (letter {idx_to_letter(j)}) (shifted={shifted})")
        return result

    def reverse(self, i: int) -> int:
        shifted = (i + self.offset - self.ring_setting) % MOD
        j = self.reverse_tbl[shifted]
        result = (j - self.offset + self.ring_setting) % MOD
        idx_to_letter = lambda x: chr(x + 65)
        self.log.debug(f"{self.__class__.__name__}.reverse: {i}->{result} (letter {idx_to_letter(j)}) (shifted={shifted})")
        return result
