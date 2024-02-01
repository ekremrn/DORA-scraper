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
    options.add_argument("--no-sandbox")
    options.add_argument("--single-process")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ignore-ssl-errors=yes")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
        "537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    )
    return Chrome(service=Service(ChromeDriverManager().install()), options=options)


class Browser:
    def __init__(self):
        self._DRIVER = create_driver()
        self.__DELAY = 2

    def get_soup(self, url: str) -> BeautifulSoup:

        try:
            self._DRIVER.get(url)
            sleep(self.__DELAY)
            return BeautifulSoup(self._DRIVER.page_source, "html.parser")

        except NoSuchWindowException:
            logging.error("Driver: NoSuchWindowException")
            sleep(self.__DELAY)
            self._DRIVER = create_driver()
            return self.get_soup(url)

        except Exception as e:
            logging.error(e)
            sleep(self.__DELAY)
            self._DRIVER = create_driver()
            return self.get_soup(url)
