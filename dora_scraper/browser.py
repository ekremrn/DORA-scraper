import logging

from time import sleep
from bs4 import BeautifulSoup

from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchWindowException

from webdriver_manager.chrome import ChromeDriverManager


def create_driver():
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument("--ignore-ssl-errors=yes")
    options.add_argument("--ignore-certificate-errors")
    return Chrome(service=Service(ChromeDriverManager().install()), options=options)


class Browser:
    def __init__(self):
        self.__DRIVER = create_driver()
        self.__DELAY = 2

    def get_soup(self, url: str) -> BeautifulSoup:

        try:
            self.__DRIVER.get(url)
        except NoSuchWindowException:
            logging.error("Driver: NoSuchWindowException")
            del self.__DRIVER
            self.__DRIVER = create_driver()
            sleep(self.__DELAY)
            return self.get_soup(url)
        except Exception as e:
            logging.error(e)
            return None

        sleep(self.__DELAY)
        soup = BeautifulSoup(self.__DRIVER.page_source, "html.parser")
        return soup
