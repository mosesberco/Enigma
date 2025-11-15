from .translator import Translator
from .substitutor import ALPHABET

class Reflector(Translator):
    """
    SYMMETRIC TRANSLATOR
    """
    def __init__(self, name: str, wiring: str):
        super().__init__(name, wiring)
        for a, b in zip(ALPHABET, wiring):
            if a == b:
                raise ValueError(f"Reflector cannot map {a} to itself")
        self.log.info(f"{name} reflector ready")
