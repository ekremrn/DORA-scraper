import os

from dotenv import load_dotenv
from dataclasses import dataclass


@dataclass
class Paths:
    load_dotenv()
    ROOT = str(os.getenv("DORA_SCRAPER_ROOT"))

    IMAGES_ROOT = os.path.join(ROOT, "images/")
    DATA_ROOT = os.path.join(ROOT, "data.json")

    LINKS_ROOT = os.path.join(ROOT, "links")

@dataclass
class Currencies:
    LIRA = "TRY"
    DOLLAR = "USD"
    EURO = "EUR"


"""
{
    "id": str,
    "brand": str,
    "category": str,
    "title": str,
    "category": str,
    "url": str,
    "prices": {
        "TRY" : {"original" : float, "discounted" : float},
    },
    "images": {
        "thumbnail_images" : [
            {
                "path" : str,
                "url" : str,
                "platform_url" : str,
            }
        ]
    },
}


"""
