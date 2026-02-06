from scraper.scraper import scrape_products
from database.db import create_table, insert_product

URL = "http://books.toscrape.com/"  # CHANGE THIS

def main():
    print("🔍 Starting product scrape...")
    create_table()

    products = scrape_products(URL)
    print(f"📦 Found {len(products)} products")

    for product in products:
        insert_product(product)

    print("✅ Data saved successfully!")

if __name__ == "__main__":
    main()
