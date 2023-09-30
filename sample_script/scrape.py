import os

from tqdm import tqdm
from argparse import ArgumentParser

from dora_scraper.utils.saver import ProductSaver
from dora_scraper.utils.browser import get_soup, DRIVER
from dora_scraper.platforms.trendyol import (
    extract_category_links,
    generate_pagination_urls,
    extract_products_from_category_page,
)

parser = ArgumentParser()
parser.add_argument("-p", "--path", type=str, default="DATA/")
parser.add_argument("-n", "--platform_name", type=str, required=True)
parser.add_argument("-u", "--platform_url", type=str, required=True)
parser.add_argument("-c", "--categories", nargs="+", required=True)
opt = parser.parse_args()

JSONPATH = os.path.join(opt.path, "{}.json".format(opt.platform_name))
SAVER = ProductSaver(opt.path, opt.platform_name)

soup = get_soup(opt.platform_url)
category_links = extract_category_links(soup, opt.categories)

progress = tqdm(category_links, desc=opt.platform_name, ncols=100, colour="green")
for category_link in progress:
    links = generate_pagination_urls(category_link)
    for link in links:
        soup = get_soup(link)
        products = extract_products_from_category_page(soup)
        SAVER.product_list(products)

DRIVER.quit()
