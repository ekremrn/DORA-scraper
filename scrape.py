import os

from tqdm import tqdm
from argparse import ArgumentParser

from utils.saver import ProductSaver
from utils.browser import get_soup, DRIVER
from platforms.trendyol import (
    get_category_links,
    get_category_pages,
    get_category_products,
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
category_links = get_category_links(soup, opt.categories)

for category_link in category_links:
    links = get_category_pages(category_link)
    progress = tqdm(links, desc="{} - {}: ".format(opt.platform_name, category_link))
    for link in progress:
        soup = get_soup(link)
        products = get_category_products(soup)
        SAVER.product_list(products)

DRIVER.quit()
