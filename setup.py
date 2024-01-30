from setuptools import find_packages, setup

setup(
    name="dora_scraper",
    version="0.1.2",
    description="Scraper of Dora Platform",
    url="https://github.com/ekremrn/DORA-scraper",
    long_description_content_type="text/markdown",
    author="ekremrn",
    packages=find_packages(),
    install_requires=["pandas", "beautifulsoup4", "selenium", "tqdm"],
)
