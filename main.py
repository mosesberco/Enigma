import json
import argparse
from enigma.machine import EnigmaMachine
from enigma.rotor import Rotor
from enigma.reflector import Reflector
from enigma.plugboard import Plugboard
from enigma.logger import get_logger, set_log_level

def load_machine_from_config(path: str) -> EnigmaMachine:
    with open(path) as f:
        cfg = json.load(f)

    rotors = [
        Rotor(r["name"], r["wiring"], notch=r["notch"], ring_setting=r["ring"], offset=r["offset"])
        for r in cfg["rotors"]
    ]
    reflector = Reflector(cfg["reflector"]["name"], cfg["reflector"]["wiring"])
    plugboard = Plugboard(cfg["plugboard"])
    return EnigmaMachine(rotors[0], rotors[1], rotors[2], reflector, plugboard)

def main():
    parser = argparse.ArgumentParser(description="Enigma M3 Simulator")
    parser.add_argument("--config", default="enigma/config.json", help="path/to/config.json")
    parser.add_argument("--level", default="INFO", help="DEBUG / INFO / WARNING / ERROR")
    parser.add_argument("--message", help="message to encode (optional)")
    args = parser.parse_args()

    set_log_level(args.level)
    log = get_logger("MAIN")
    log.info(f"Starting Enigma with log level {args.level}")

    machine = load_machine_from_config(args.config)
    msg = args.message or input("Enter message: ").upper()

    encoded = machine.encode_message(msg)
    print("Encoded:", encoded)

    # machine2 = load_machine_from_config(args.config)
    # decoded = machine2.encode_message(encoded)
    # print("Decoded:", decoded)

if __name__ == "__main__":
    main()
