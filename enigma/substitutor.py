from abc import ABC, abstractmethod
from .logger import get_logger

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
A_ORD = ord('A')
MOD = 26

class Substitutor(ABC):
    def __init__(self, name: str):
        self.log = get_logger(name)

    @staticmethod
    def ch2i(ch: str) -> int:
        return ord(ch) - A_ORD

    @staticmethod
    def i2ch(i: int) -> str:
        return chr((i % MOD) + A_ORD)

    @staticmethod
    def rot(i: int, shift: int) -> int:
        return (i + shift) % MOD

    @abstractmethod
    def forward(self, i: int) -> int:
        """המרה קדימה (ימין→שמאל) באינדקסים 0–25."""
        raise NotImplementedError

    def reverse(self, i: int) -> int:
        """ברירת מחדל סימטרית (מתאים לרפלקטור/לוח-חיבורים)."""
        # למחלקות לא-סימטריות (כמו Rotor) נדרוס.
        return self.forward(i)
