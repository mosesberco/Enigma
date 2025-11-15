from .translator import Translator
from .substitutor import ALPHABET

class Plugboard(Translator):

    def __init__(self, pairs=None):
        if pairs is None:
            pairs = []

        wiring = list(ALPHABET)
        used = set()
        for a, b in pairs:
            a, b = a.upper(), b.upper()
            if a in used or b in used:
                raise ValueError("letter already connected")
            ai, bi = ALPHABET.index(a), ALPHABET.index(b)
            wiring[ai], wiring[bi] = b, a
            used |= {a, b}
        super().__init__("PLUGBOARD", "".join(wiring))
        self.log.info(f"Plugboard initialized with {pairs}")
