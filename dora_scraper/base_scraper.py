import os
import json
import time

from tqdm import tqdm
from bs4 import BeautifulSoup
from typing import Dict, List

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from dora_scraper.structures import Paths
from dora_scraper.utils.download import download_image

class Scraper:
    def __init__(self, delay=1):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=webdriver.ChromeOptions(),
        )
        self.delay = delay

    #
    def get(self, url: str):
        self.driver.get(url)
        time.sleep(self.delay)
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        return soup

    #
    def price(self, currency: str, price_orgin: float, price_disc: float = None):
        price_dict = {"original": price_orgin, "discounted": price_disc, "currency" : currency}
        return price_dict

    #
    def thumb_image(self, path: str, platform_url: str):
        image_dict = {
            "path": path,
            "platform_url": platform_url,
        }
        return image_dict

    #
    def product_dict(
        self,
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


    #
    def save_product(self, product: Dict):
        if os.path.exists(Paths.DATA_ROOT):
            data = json.load(open(Paths.DATA_ROOT))
        else:
            data = list()
        
        if [row for row in data if row.get("id") == product.get("id")]:
            return
        
        data.append(product)
        with open(Paths.DATA_ROOT, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


    #
    def product_from_category_page(self, product_soup: BeautifulSoup):
        pass

    #
    def scrape_category_page(self, product_list: List[BeautifulSoup]):

        for product_data in product_list:
            product = self.product_from_category_page(product_data)
            
            # Image Process
            image_path = product['thumb_image']['path']
            full_image_path = os.path.join(Paths.IMAGES_ROOT, image_path)
            image_url = product['thumb_image']['platform_url']
            response = download_image(image_url, full_image_path)

            if response is False:
                product['thumb_image']['path'] = None

            self.save_product(product)

    #
    def scrape_category_pages(self, category_dict: Dict, url_format: str, page_number: int):
        
        category_name = category_dict["name"]
        category_url = category_dict["url"]

        urls = [url_format.format(category_url, i + 1) for i in range(0, page_number)]

        for url in tqdm(urls, desc=category_name, ncols=100, colour="green"):
            soup = self.get(url)
            self.scrape_category_page(soup)

    #
    def scrape_category_links(self, json_path, url_format, page_number):
        category_list = json.load(open(json_path))
        for category_dict in category_list:
            self.scrape_category_pages(category_dict, url_format, page_number)

