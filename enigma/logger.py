# enigma/logger.py
import logging
from logging import Formatter, StreamHandler, FileHandler
import os

CURRENT_LOG_LEVEL = logging.ERROR

def set_log_level(level_name: str):
    """עדכון רמת לוג גלובלית (לקריאה מ-main)"""
    global CURRENT_LOG_LEVEL
    level = getattr(logging, level_name.upper(), logging.INFO)
    CURRENT_LOG_LEVEL = level

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(CURRENT_LOG_LEVEL)
    fmt = Formatter("%(asctime)s | %(levelname)-7s | %(name)s | %(message)s")



    # SCREEN
    console = StreamHandler()
    console.setLevel(CURRENT_LOG_LEVEL)
    console.setFormatter(fmt)


    # FILE

    # os.makedirs("logs", exist_ok=True)
    # file = FileHandler("logs/enigma.log", mode="w", encoding="utf-8")
    # file.setLevel(CURRENT_LOG_LEVEL)
    # file.setFormatter(fmt)
    #
    logger.addHandler(console)
    # logger.addHandler(file)
    return logger
