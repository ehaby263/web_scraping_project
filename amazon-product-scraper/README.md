# Amazon Product Scraper

A web scraping project built with **Python and Scrapy** to extract product information from Amazon search results.

## 📌 Project Overview

This project uses **Scrapy** to collect structured product information from Amazon search pages.

The scraper searches for products based on a specified keyword and extracts relevant information from the search results.

## 🛠️ Technologies Used

* Python
* Scrapy
* CSS Selectors
* XPath
* Web Scraping
* Data Extraction

## 📊 Data Collected

For each product, the scraper extracts available information such as:

* Product Name
* Product URL
* Price
* Rating
* Number of Reviews
* Availability

## 📁 Project Structure

```text
amazon-product-scraper/
│
├── scrapy.cfg
│
└── amazon/
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── settings.py
    │
    └── spiders/
        ├── __init__.py
        └── products.py
```

## 🔍 Example Search

The scraper can be configured to search for products using a keyword such as:

```text
Python for Beginners
```

## 📋 Sample Scraped Data

| Product Name                          |  Price | Rating | Reviews |
| ------------------------------------- | -----: | -----: | ------: |
| Python Crash Course                   | $xx.xx |    4.7 | 20,000+ |
| Automate the Boring Stuff with Python | $xx.xx |    4.7 | 10,000+ |
| Python Programming for Beginners      | $xx.xx |    4.5 |  5,000+ |

> The values above are examples of the output structure. Actual results depend on the Amazon search page at the time of scraping.

## 🔍 Example Output

```text
{
    "product_name": "Python Crash Course",
    "price": "$xx.xx",
    "rating": "4.7",
    "reviews": "20,000+",
    "product_url": "https://www.amazon.com/..."
}
```

## 🚀 Running the Spider

Install the required dependencies:

```bash
pip install scrapy
```

Run the spider:

```bash
scrapy crawl products
```

Export the scraped data to CSV:

```bash
scrapy crawl products -o amazon_products.csv
```

Export the scraped data to JSON:

```bash
scrapy crawl products -o amazon_products.json
```

## 🔧 Features

* Scrapes Amazon search results
* Uses custom request headers
* Extracts structured product information
* Supports CSV and JSON export
* Built using Scrapy's spider architecture
* Can be extended to scrape different product categories and search keywords

## 📈 Future Improvements

* Add pagination support
* Extract product details from individual product pages
* Add automated data cleaning
* Store scraped data in PostgreSQL
* Build an ETL pipeline
* Add support for multiple search keywords
* Schedule automated scraping jobs

## ⚠️ Disclaimer

This project is created for **educational and portfolio purposes**. Please respect Amazon's terms of service, robots.txt, and applicable laws when using or modifying the scraper.
