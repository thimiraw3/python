# 📊 Python Web Scraper & Dashboard (V3)

This is Version 3 of the Python Web Scraper project. It builds on previous versions by providing a simple web-based dashboard using Flask to analyze and visualize scraped product data.

**🚀 Features**
- Scrape product data from a website (V1)
- Store data in a SQLite database
- Analyze data using pandas (V2)
- Generate charts using matplotlib
- Display statistics and charts on a web dashboard (V3)
- Responsive HTML dashboard with product table

**🗂️ Project Structure**

```bash
PRODUCT_SCRAPER_V3/
│
├─ analysis/         # Any analysis scripts (V2)
│  └─ analyze.py 
├─ data/
│  └─ products.db    # SQLite database
├─ database/
│  └─ db.py          # Database functions
├─ web/
│  |─ app.py         # Flask web dashboard (V3)
│  |─ static
│  |  └─ chart.png           #generated chart
│  └─ templates
│     └─ dashboard.html      # dashboard template
├─ scraper/
│  └─ scraper.py     # Web scraping logic
├─ main.py           # Entry point (V1)
├─ requirements.txt  # Python dependencies
└─ README.md         # Project overview
```

**⚙️ Installation**

1. Clone the repository
2. (Optional) Create and activate a virtual environment
3. Install required dependencies

```bash
pip install flask requests beautifulsoup4 pandas matplotlib
```

**🕷️ Running the Scraper (V1)**

```bash
python main.py
```

**📊 CLI Analysis (V2)**

```bash
python analyze.py
```

**🌐 Web Dashboard (V3)**

```bash
python app.py
```

- Open http://127.0.0.1:5000/ in your browser

**📌 Version History**

V1 – Web scraping and database storage  
V2 – CLI-based data analysis and visualization  
V3 – Flask-based web dashboard

**📝 Notes**

This project scrapes data from http://books.toscrape.com/ for educational purposes only.
