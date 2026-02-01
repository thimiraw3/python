# PRODUCT_SCRAPER_V1 📚

Welcome to **PRODUCT_SCRAPER_V1**, a simple yet powerful Python project that scrapes product data from online stores and stores it in a local SQLite database. Perfect for learning web scraping, data storage, and building your first data-driven project! 🚀

---

## Features ✨
- Scrape product details like **name**, **price**, **rating**, and **scraped date**.
- Store scraped data in a **SQLite database** for easy access.
- Modular design:
  - `scraper.py` handles web scraping
  - `db.py` manages database creation and insertion
  - `main.py` orchestrates the workflow
- Fully **expandable** to scrape multiple websites or add more product details.

---

## Getting Started 🏁

### Prerequisites
- Python 3.8+
- Pip (Python package manager)

---

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/PRODUCT_SCRAPER_V1.git
   cd PRODUCT_SCRAPER_V1

2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows

3. Install dependencies:

   ```bash
   pip install -r requirements.txt

---

### Usage

- Open main.py and change the URL variable if you want to scrape a different site.

- Run the script:

   ```bash
   python main.py

- Your scraped products will be stored in data/products.db.

---

### Project Structure 🗂️

  ```bash
  PRODUCT_SCRAPER_V1/
  │
  ├─ analysis/         # Any analysis scripts
  ├─ data/
  │  └─ products.db    # SQLite database
  ├─ database/
  │  └─ db.py          # Database functions
  ├─ scraper/
  │  └─ scraper.py     # Scraping logic
  ├─ main.py           # Entry point
  ├─ requirements.txt  # Python dependencies
  └─ README.md         # Project overview
```
---

### Inspiration 💡

This project is more than just code—it’s a step toward mastering data collection, automation, and Python development. Whether you’re a beginner or an aspiring data engineer, PRODUCT_SCRAPER_V1 shows how simple tools can unlock powerful insights. Imagine scraping thousands of products effortlessly, analyzing them, and building your own recommendations system—this is where it all starts. 🌟

---

### License 📄

This project is open-source and available under the MIT License.
