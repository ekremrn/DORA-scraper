import os

from dotenv import load_dotenv
from dataclasses import dataclass


@dataclass
class Paths:
    load_dotenv()
    ROOT = str(os.getenv("DORA_DATA_ROOT"))

    IMAGES_ROOT = os.path.join(ROOT, "images/")
    DATA_PATH = os.path.join(ROOT, "data.json")


@dataclass
class Currencies:
    LIRA = "TRY"
    DOLLAR = "USD"
    EURO = "EUR"
