import requests
from bs4 import BeautifulSoup
from datetime import datetime

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def scrape_products(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    products = []

    product_cards = soup.select("article.product_pod")

    for card in product_cards:
        name = card.select_one("h3 > a").get("title")
        price_text = card.select_one("p.price_color").text.strip()
        price = float(price_text.replace("£", "").replace("Â", ""))

        products.append({
            "name": name,
            "price": price,
            "rating": None,
            "date": datetime.now().strftime("%Y-%m-%d")
        })

    return products
