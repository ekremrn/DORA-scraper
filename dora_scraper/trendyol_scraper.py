import os
import json


from typing import Dict
from bs4 import BeautifulSoup

from dora_scraper.base_scraper import Scraper
from dora_scraper.structures import Currencies, Paths


class TrendyolScraper(Scraper):

    #
    def product_from_category_page(self, product_soup : BeautifulSoup):
        super().product_from_category_page(product_soup)
        id = product_soup.get("data-id")
        name = product_soup.select("span.prdct-desc-cntnr-name")[0].get_text()
        brand = product_soup.select("span.prdct-desc-cntnr-ttl")[0].get_text()
        url = "https://www.trendyol.com" + product_soup.select(
            " div.p-card-chldrn-cntnr.card-border > a"
        )[0].get("href").split("?")[0]

        price1 = product_soup.select("div.prc-box-orgnl")
        price1 = price1[0].get_text() if price1 else None
        price2 = product_soup.select("div.prc-box-dscntd")[0].get_text()

        price1 = (
            price1.split(" ")[0].replace(".", "").replace(",", ".") if price1 else None
        )
        price2 = price2.split(" ")[0].replace(".", "").replace(",", ".")
        price_dict = (
            self.price(
                Currencies.LIRA, price_orgin=float(price1), price_disc=float(price2)
            )
            if price1
            else self.price(Currencies.LIRA, price_orgin=float(price2))
        )

        image_path = os.path.join("trendyol", id, "thumb_0.jpg")
        image_url = product_soup.select("img.p-card-img")[0].get("src")

        thumb_image = self.thumb_image(path=image_path, platform_url=image_url)

        product = self.product_dict(
            id=id,
            platform="trendyol",
            brand=brand,
            name=name,
            url=url,
            price=price_dict,
            thumb_image=thumb_image,
        )

        return product

    #
    def scrape_category_page(self, soup: BeautifulSoup):
        product_list = soup.find_all("div", {"class": "p-card-wrppr"})
        super().scrape_category_page(product_list)
        

    #
    def scrape_category_links(self, page_number:int=1):
        json_path = os.path.join(Paths.LINKS_ROOT, "trendyol_categories.json")
        url_format = "{}?pi={}"
        super().scrape_category_links(json_path, url_format, page_number)
