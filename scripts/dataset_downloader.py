import os
import re
import json
import shutil
import socket
import requests

from tqdm import tqdm
from time import sleep
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.request import urlretrieve

from argparse import ArgumentParser

socket.setdefaulttimeout(5)

parser = ArgumentParser()
parser.add_argument("-p", "--path", type=str, required=True)
parser.add_argument("-d", "--dataset_path", type=str, required=True)
parser.add_argument("-s", "--delay", type=float, default=0.5)
opt = parser.parse_args()


data = json.load(open(opt.path))

def download_image(source, target):
    target_head, _ = os.path.split(target)
    if not os.path.exists(target_head):
        os.makedirs(target_head)
    elif os.path.exists(target):
        return True

    try:
        urlretrieve(source, target)
    except HTTPError as e:
        r = requests.get(source, stream=True)
        if r.status_code == 200:
            with open(str(target), "wb") as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
    except Exception as e:
        return False

    sleep(opt.delay)
    return True
    

def get_images_links(url):
    r = requests.get(url)
    sleep(opt.delay)

    if r.status_code != 200:
        return False
    
    soup = BeautifulSoup(r.content, "html.parser")
    script = soup.find("script", string=re.compile("__PRODUCT_DETAIL_APP_INITIAL_STATE__"))
    pattern = "\"images\":(.*)\,\"isSellable"
    match = re.search(pattern, str(script))
    urls = eval(match.group(1))
    urls = ["https://cdn.dsmcdn.com/{}".format(url) for url in urls]
    return urls



for row in tqdm(data, ncols=100, colour="green"):
    if row.get("platform") != "trendyol":
        continue

    id = row.get("id")
    url = row.get("url")

    target_path = os.path.join(opt.dataset_path, str(id))
    image_urls = get_images_links(url)

    if not image_urls:
        continue

    for index, image_url in enumerate(image_urls):
        target_image_path = os.path.join(target_path, "{}.jpg".format(index))
        download_image(source=image_url, target=target_image_path)

