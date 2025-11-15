from .substitutor import Substitutor
from .plugboard import Plugboard
from .reflector import Reflector
from .rotor import Rotor
from .logger import get_logger

class EnigmaMachine:
    def __init__(self, left: Rotor, middle: Rotor, right: Rotor, reflector: Reflector, plugboard: Plugboard):
        self.left = left
        self.middle = middle
        self.right = right
        self.reflector = reflector
        self.plugboard = plugboard
        self.log = get_logger("ENIGMA")
        self.log.info("Enigma machine ready")

    def step_rotors(self):
        """מימוש הדריכה הכפולה"""
        if self.middle.at_notch():
            self.middle.step()
            self.left.step()
            self.log.debug("Double step triggered (middle at notch)")
        elif self.right.at_notch():
            self.middle.step()
            self.log.debug("Middle stepped because right at notch")
        self.right.step()

    def encode_char(self, ch: str) -> str:
        if not ch.isalpha():
            return ch
        ch = ch.upper()

        self.step_rotors()
        i = Substitutor.ch2i(ch)
        self.log.debug(f"Input {ch} -> {i}")

        # זרימה: plugboard → rotors → reflector → rotors ← plugboard
        i = self.plugboard.forward(i)
        i = self.right.forward(i)
        i = self.middle.forward(i)
        i = self.left.forward(i)
        i = self.reflector.forward(i)
        i = self.left.reverse(i)
        i = self.middle.reverse(i)
        i = self.right.reverse(i)
        i = self.plugboard.reverse(i)

        out_ch = Substitutor.i2ch(i)
        self.log.info(f"{ch} → {out_ch}")
        return out_ch

    def encode_message(self, msg: str) -> str:
        result = []
        for ch in msg:
            result.append(self.encode_char(ch))
        return "".join(result)
