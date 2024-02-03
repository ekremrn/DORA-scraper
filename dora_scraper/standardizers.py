from typing import Dict


def price_dict(currency: str, price_orgin: float, price_disc: float = None):
    """
    Create a dictionary representing the price information.

    Args:
        currency (str): The currency in which the price is expressed.
        price_orgin (float): The original price.
        price_disc (float, optional): The discounted price (default is None if there's no discount).

    Returns:
        dict: A dictionary containing the price information.
    """
    price_dict = {
        "original": price_orgin,
        "discounted": price_disc,
        "currency": currency,
    }
    return price_dict


def thumb_image_dict(path: str, platform_url: str):
    """
    Create a dictionary representing thumbnail image information.

    Args:
        path (str): The file path to the thumbnail image.
        platform_url (str): The URL of the platform where the image is hosted.

    Returns:
        dict: A dictionary containing the thumbnail image information.
    """
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
    """
    Create a dictionary representing product information.

    Args:
        id (str): The unique identifier of the product.
        platform (str): The platform or marketplace where the product is listed.
        brand (str): The brand or manufacturer of the product.
        name (str): The name or title of the product.
        url (str): The URL of the product listing.
        price (Dict): A dictionary representing the price information (created using price_dict).
        thumb_image (Dict): A dictionary representing the thumbnail image information (created using thumb_image_dict).

    Returns:
        dict: A dictionary containing the product information.
    """
    product_dict = {
        "_id": int(id),
        "platform": platform,
        "brand": brand,
        "name": name,
        "url": url,
        "price": price,
        "thumb_image": thumb_image,
    }
    return product_dict
