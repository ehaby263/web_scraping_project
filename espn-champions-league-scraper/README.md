# UEFA Champions League Standings Scraper

A web scraping project built with **Python and Scrapy** to extract UEFA Champions League group-stage standings from **ESPN**.

## 📌 Project Overview

This project scrapes UEFA Champions League standings data from ESPN and extracts information for all teams participating in the group stage.

The project currently collects data from the **2020–21 UEFA Champions League season**, including all eight groups (A–H).

## 🛠️ Technologies Used

* Python
* Scrapy
* CSS Selectors
* XPath
* Web Scraping
* Data Extraction

## 📊 Data Collected

For each team, the scraper extracts:

* Season
* Group
* Position
* Team Name
* Team Abbreviation
* Games Played (GP)
* Wins (W)
* Draws (D)
* Losses (L)
* Goals For (F)
* Goals Against (A)
* Goal Difference (GD)
* Points (P)

## 📁 Project Structure

```text
espn-champions-league-scraper/
│
├── scrapy.cfg
│
└── espn/
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── settings.py
    │
    └── spiders/
        ├── __init__.py
        └── champions_league.py
```

## 📋 Sample Scraped Data

### UEFA Champions League 2020–21 — Group A

| Season  | Group | Position | Team             | GP |  W |  D |  L |  F |  A |  GD |  P |
| ------- | ----- | -------: | ---------------- | -: | -: | -: | -: | -: | -: | --: | -: |
| 2020-21 | A     |        1 | Bayern Munich    |  6 |  5 |  1 |  0 | 18 |  5 | +13 | 16 |
| 2020-21 | A     |        2 | Atlético Madrid  |  6 |  2 |  3 |  1 |  7 |  8 |  -1 |  9 |
| 2020-21 | A     |        3 | RB Salzburg      |  6 |  1 |  1 |  4 | 10 | 17 |  -7 |  4 |
| 2020-21 | A     |        4 | Lokomotiv Moscow |  6 |  0 |  3 |  3 |  5 | 10 |  -5 |  3 |

### Group B

| Position | Team                     | GP |  W |  D |  L |  F |  A | GD |  P |
| -------: | ------------------------ | -: | -: | -: | -: | -: | -: | -: | -: |
|        1 | Real Madrid              |  6 |  3 |  1 |  2 | 11 |  9 | +2 | 10 |
|        2 | Borussia Mönchengladbach |  6 |  2 |  2 |  2 | 16 |  9 | +7 |  8 |
|        3 | Shakhtar Donetsk         |  6 |  2 |  2 |  2 |  5 | 12 | -7 |  8 |
|        4 | Internazionale           |  6 |  1 |  3 |  2 |  7 |  9 | -2 |  6 |

## 🔍 Example

The scraper processes the standings and converts the information into structured records.

Example:

```text
{
    "season": "2020-21",
    "group": "A",
    "position": 1,
    "team": "Bayern Munich",
    "gp": 6,
    "wins": 5,
    "draws": 1,
    "losses": 0,
    "goals_for": 18,
    "goals_against": 5,
    "goal_difference": "+13",
    "points": 16
}
```

## 🚀 Running the Spider

Install the required dependencies:

```bash
pip install scrapy
```

Run the spider:

```bash
scrapy crawl champions_league
```

To export the scraped data to CSV:

```bash
scrapy crawl champions_league -o champions_league.csv
```

To export to JSON:

```bash
scrapy crawl champions_league -o champions_league.json
```

## 📈 Future Improvements

* Scrape multiple Champions League seasons
* Scrape all seasons from 2003 to 2025
* Store the data in PostgreSQL
* Build an automated ETL pipeline
* Add data cleaning and validation
* Create visualizations and dashboards
* Extend the scraper to collect match results and team statistics



