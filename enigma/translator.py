from typing import List
from .substitutor import Substitutor, ALPHABET, MOD

def _wiring_to_indexes(wiring: str) -> List[int]:
    wiring = wiring.upper()
    assert len(wiring) == 26 and set(wiring) == set(ALPHABET), "wiring must be a 26-letter permutation"
    return [Substitutor.ch2i(c) for c in wiring]

def _invert_table(tbl: List[int]) -> List[int]:
    inv = [0] * 26
    for i, j in enumerate(tbl):
        inv[j] = i
    return inv

class Translator(Substitutor):
    """
    ממיר כללי קדימה/אחורה לפי טבלת פרמוטציה.
    מתאים כבסיס ל-Reflector/Plugboard/אחר.
    """
    def __init__(self, name: str, wiring: str):
        super().__init__(name)
        self.forward_tbl = _wiring_to_indexes(wiring)   # f(i)
        self.reverse_tbl = _invert_table(self.forward_tbl)  # f^{-1}(i)
        self.log.debug(f"{name}: wiring={wiring}")

    def forward(self, i: int) -> int:
        j = self.forward_tbl[i % MOD]
        self.log.debug(f"{self.__class__.__name__}.forward: {i} -> {j}")
        return j

    def reverse(self, i: int) -> int:
        j = self.reverse_tbl[i % MOD]
        self.log.debug(f"{self.__class__.__name__}.reverse: {i} -> {j}")
        return j
