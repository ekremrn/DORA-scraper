import os

from bs4 import BeautifulSoup
from typing import List, Dict

from utils.structures import Currencies
from utils.standardizers import price_dict, thumb_image_dict, product_dict


def get_category_links(soup: BeautifulSoup, categories: List[str]) -> List[str]:
    main_categories = soup.find_all("li", {"class": "tab-link"})
    links = list()
    for main_category_soup in main_categories:
        main_category_name = main_category_soup.a.get_text().lower()
        if main_category_name not in categories:
            continue

        sub_categories = main_category_soup.select("div", {"class": "sub-item-list"})
        for sub_category in sub_categories:
            links_soup = sub_category.find_all("li")
            links += [
                "https://www.trendyol.com{}".format(link_soup.a.get("href"))
                for link_soup in links_soup
            ]

    return links


def get_category_pages(category_link: str, page_limit: int = 99) -> List[Dict]:
    urls = ["{}?pi={}".format(category_link, i + 1) for i in range(0, page_limit)]
    return urls


def get_category_products(soup: BeautifulSoup) -> List[Dict]:
    soup_list = soup.find_all("div", {"class": "p-card-wrppr"})
    products = list()
    for product_soup in soup_list:
        id = product_soup.get("data-id")
        name = product_soup.select("span.prdct-desc-cntnr-name")[0].get_text()
        brand = product_soup.select("span.prdct-desc-cntnr-ttl")[0].get_text()
        url = (
            "https://www.trendyol.com"
            + product_soup.select(" div.p-card-chldrn-cntnr.card-border > a")[0]
            .get("href")
            .split("?")[0]
        )

        price1 = product_soup.select("div.prc-box-orgnl")
        price1 = price1[0].get_text() if price1 else None
        price2 = product_soup.select("div.prc-box-dscntd")[0].get_text()
        price1 = (
            price1.split(" ")[0].replace(".", "").replace(",", ".") if price1 else None
        )
        price2 = price2.split(" ")[0].replace(".", "").replace(",", ".")

        price = (
            price_dict(
                Currencies.LIRA, price_orgin=float(price1), price_disc=float(price2)
            )
            if price1
            else price_dict(Currencies.LIRA, price_orgin=float(price2))
        )

        image_path = os.path.join("trendyol", id, "thumb_0.jpg")
        image_url = product_soup.select("img.p-card-img")[0].get("src")
        thumb_image = thumb_image_dict(path=image_path, platform_url=image_url)

        products.append(
            product_dict(
                id=id,
                platform="trendyol",
                brand=brand,
                name=name,
                url=url,
                price=price,
                thumb_image=thumb_image,
            )
        )

    return products
