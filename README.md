# Dora Scraper
Dora Scraper is a Python-based web scraper tool that can be used to extract data from various e-commerce websites. Currently, it supports Trendyol, a popular e-commerce website based in Turkey.

## Requirements

- Python 3.x
- Requirements (pip install -r requirements.txt)


## Usage

Dora Scraper currently supports the following command-line arguments:

- -p or --path: Path to a JSON file containing a list of product links to scrape (required)
- -n or --page_number: Number of products to scrape (default: all products in the JSON file)
- -d or --delay: Delay between each request in seconds (default: 2 second)
- -i or --image_download: Download images for each product (default: False)

Example usage:

```bash
python3 dora_scraper/trendyol_scraper.py -p links/trendyol_dress.json -n 5 -d 3 -i
```

This will scrape the first 5 page from every link in the json file.

## Contributing
Feel free to contribute to this project by creating pull requests or reporting any issues you encounter.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Note
This README file was written by ChatGPT-2. I didn't even have to make any changes. It's amazing :)

docker pull selenium/standalone-chrome

docker run -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome
