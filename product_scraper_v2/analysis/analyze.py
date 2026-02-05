import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_NAME = "data/products.db"

def load_data():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM products", conn)
    conn.close()
    return df

def analyze_data(df):
    print("\n📊 BASIC STATISTICS\n")

    print("Total products scraped:", len(df))
    print("Average price:", round(df["price"].mean(), 2))
    print("Minimum price:", df["price"].min())
    print("Maximum price:", df["price"].max())

    print("\n📦 Products:")
    print(df[["name", "price"]])

def plot_prices(df):
    plt.figure()
    plt.barh(df["name"], df["price"])
    plt.xlabel("Price")
    plt.ylabel("Product")
    plt.title("Product Prices")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = load_data()

    if df.empty:
        print("❌ No data found. Run the scraper first.")
    else:
        analyze_data(df)
        plot_prices(df)
