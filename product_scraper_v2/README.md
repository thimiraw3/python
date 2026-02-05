#📦 Python Web Scraper & Data Analyzer (V2)

This project is a Python-based web scraping and data analysis system. Version 1 focuses on scraping product data from a website and storing it in a database. Version 2 extends the project by analyzing the stored data and visualizing it using charts.

---

##🚀 Features

- Scrape product names and prices from a website
- Store scraped data in a SQLite database
- Analyze product data using pandas
- Display statistics in the command line (CLI)
- Visualize product prices using matplotlib charts

---

##🗂️ Project Structure

project-root/
│
├── main.py                  # Entry point for scraping (V1)
├── scraper/
│   └── scraper.py           # Web scraping logic
│
├── database/
│   └── db.py                # SQLite database operations
│
├── analyze.py               # Data analysis & visualization (V2)
├── data/
│   └── products.db          # SQLite database file
│
├── requirements.txt
└── README.md

---

##⚙️ Installation

1. Clone the repository
2. Create and activate a virtual environment (optional but recommended)
3. Install dependencies

```bash
pip install requests beautifulsoup4 pandas matplotlib
```

---

🕷️ Running the Scraper (V1)

-Run the scraper to collect product data and store it in the database:

```bash
python main.py
```

---


##📊 Data Analysis & Visualization (V2)

-After scraping data, analyze and visualize it using:

```bash
python analyze.py
```

---

-This will display basic statistics such as total products, average price, minimum and maximum price, and show a horizontal bar chart of product prices.

---

##📝 Notes

-This project scrapes data from http://books.toscrape.com/ for educational purposes only. Ensure you comply with website terms before scraping other websites.

---

##📌 Versioning

V1 – Data scraping and database storage  
V2 – Data analysis, CLI output, and chart visualization

