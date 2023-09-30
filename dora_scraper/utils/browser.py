from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configure ChromeOptions for the WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--incognito")
options.add_argument("--ignore-ssl-errors=yes")
options.add_argument("--ignore-certificate-errors")
# Initialize the WebDriver
DRIVER = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

# Delay constant for sleep
DELAY = 2


def get_soup(url: str):
    """
    Get a BeautifulSoup object by fetching the HTML content of a URL.

    Args:
        url (str): The URL to fetch the HTML content from.

    Returns:
        BeautifulSoup or None: A BeautifulSoup object representing the parsed HTML content,
        or None if an exception occurs during the page retrieval.
    """
    try:
        # Attempt to navigate to the specified URL
        DRIVER.get(url)
    except:
        # If an exception occurs during page retrieval, return None
        return None

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(DRIVER.page_source, "html.parser")

    # Introduce a delay to ensure the page is fully loaded before parsing
    sleep(DELAY)

    return soup
