import time
from enigma.machine import EnigmaMachine
from enigma.rotor import Rotor
from enigma.reflector import Reflector
from enigma.plugboard import Plugboard
import json


def build_machine(cfg):
    rotors = [
        Rotor(r["name"], r["wiring"], notch=r["notch"], ring_setting=r["ring"], offset=r["offset"])
        for r in cfg["rotors"]
    ]
    reflector = Reflector(cfg["reflector"]["name"], cfg["reflector"]["wiring"])
    plugboard = Plugboard(cfg["plugboard"])
    return EnigmaMachine(rotors[0], rotors[1], rotors[2], reflector, plugboard)

with open("enigma/config.json") as f:
    cfg = json.load(f)

N = 10000
msg = "HELLO"

start = time.perf_counter()
for _ in range(N):
    machine = build_machine(cfg)
    machine.encode_message(msg)
end = time.perf_counter()

print(f"Encoded {N} messages in {end - start:.3f}s  →  {(N / (end - start)):.1f} msgs/sec")
