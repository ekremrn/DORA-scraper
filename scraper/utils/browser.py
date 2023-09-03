from time import sleep

from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--ignore-ssl-errors=yes")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--headless")
DRIVER = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub", options=options
)

DELAY = 2


def get_soup(url: str):
    try:
        DRIVER.get(url)
    except:
        return None
    soup = BeautifulSoup(DRIVER.page_source, "html.parser")
    sleep(DELAY)
    return soup
