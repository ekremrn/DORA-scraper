from typing import Dict


def price_dict(currency: str, price_orgin: float, price_disc: float = None):

    price_dict = {
        "original": price_orgin,
        "discounted": price_disc,
        "currency": currency,
    }
    return price_dict


def thumb_image_dict(path: str, platform_url: str):
    image_dict = {"path": path, "platform_url": platform_url}
    return image_dict


def product_dict(
    id: str,
    platform: str,
    brand: str,
    name: str,
    url: str,
    price: Dict,
    thumb_image: Dict,
):
    product_dict = {
        "id": id,
        "platform": platform,
        "brand": brand,
        "name": name,
        "url": url,
        "price": price,
        "thumb_image": thumb_image,
    }
    return product_dict
