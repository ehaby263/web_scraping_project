# Web Scraping Projects

A collection of **Python web scraping projects** built to practice and demonstrate different web scraping techniques, data extraction methods, and automation tools.

The repository includes projects using **Scrapy, Selenium, Playwright, CSS Selectors, XPath, and APIs**, with a focus on collecting structured data that can be used for data engineering and analysis.

---

## 🚀 Projects

### 1. Amazon Product Scraper

A Scrapy-based project that extracts product information from Amazon search results.

**Technologies:**

* Python
* Scrapy
* CSS Selectors
* XPath

**Data collected:**

* Product Name
* Price
* Rating
* Number of Reviews
* Product URL

📂 Project:

```text
amazon-product-scraper/
```

---

### 2. UEFA Champions League Standings Scraper

A Scrapy project that extracts UEFA Champions League group-stage standings from ESPN.

The project collects data for the **2020–21 UEFA Champions League season**, covering Groups A–H.

**Technologies:**

* Python
* Scrapy
* CSS Selectors
* XPath

**Data collected:**

* Season
* Group
* Position
* Team
* Games Played
* Wins
* Draws
* Losses
* Goals For
* Goals Against
* Goal Difference
* Points

📂 Project:

```text
espn-champions-league-scraper/
```

---

## 🛠️ Technologies

| Technology    | Purpose                      |
| ------------- | ---------------------------- |
| Python        | Programming language         |
| Scrapy        | Web scraping framework       |
| Selenium      | Browser automation           |
| Playwright    | JavaScript-rendered websites |
| CSS Selectors | HTML data extraction         |
| XPath         | HTML/XML data extraction     |
| APIs          | Direct data collection       |
| Pandas        | Data processing              |
| PostgreSQL    | Data storage                 |

---

## 📁 Repository Structure

```text
web-scraping-projects/
│
├── README.md
│
├── amazon-product-scraper/
│   ├── scrapy.cfg
│   └── amazon/
│       ├── items.py
│       ├── middlewares.py
│       ├── pipelines.py
│       ├── settings.py
│       └── spiders/
│           └── products.py
│
└── espn-champions-league-scraper/
    ├── scrapy.cfg
    └── espn/
        ├── items.py
        ├── middlewares.py
        ├── pipelines.py
        ├── settings.py
        └── spiders/
            └── champions_league.py
```

---

## 🎯 Goals

The main goals of this repository are to:

* Build practical experience with web scraping
* Learn different scraping techniques
* Work with static and dynamic websites
* Extract and structure real-world data
* Practice data cleaning and transformation
* Prepare scraped data for databases and ETL pipelines
* Build a portfolio of practical Python projects

---

## 📈 Future Projects

More projects will be added as I continue developing my web scraping and data engineering skills.

Planned areas include:

* Selenium Web Scraping
* Playwright Web Scraping
* JavaScript-rendered websites
* API-based data extraction
* Pagination and large-scale scraping
* PostgreSQL data storage
* Data cleaning and transformation
* Automated ETL pipelines
* Sports data scraping
* E-commerce data scraping

---

## 👨‍💻 About

This repository is part of my journey toward becoming a **Data Engineer**, with a particular focus on **Python, Web Scraping, Data Collection, ETL, and Data Engineering**.

The projects are continuously updated as I learn new technologies and techniques.

---

## ⚠️ Disclaimer

These projects are created for **educational and portfolio purposes**. When scraping websites, users should respect the target website's terms of service, robots.txt directives, applicable laws, and rate limits.

