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

progress = tqdm(category_links, desc = opt.platform_name, ncols=100, colour="green")
for category_link in progress:
    links = get_category_pages(category_link)
    for link in links:
        soup = get_soup(link)
        products = get_category_products(soup)
        SAVER.product_list(products)

DRIVER.quit()
