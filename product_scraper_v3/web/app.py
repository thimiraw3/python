from flask import Flask, render_template
import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_NAME = os.path.join(BASE_DIR, "data", "products.db")

def load_data():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM products", conn)
    df = df.drop_duplicates(subset=["name"])
    df = df.sort_values(by="price")
    conn.close()
    return df


def generate_chart(df):
    df_sorted = df.sort_values(by="price", ascending=True)

    # Dynamic height: 0.4 inch per product (minimum 6)
    height = max(6, len(df_sorted) * 0.4)

    plt.figure(figsize=(12, height))

    plt.barh(df_sorted["name"], df_sorted["price"])

    plt.xlabel("Price")
    plt.ylabel("Product")
    plt.title("Product Prices")

    # Extra space for long names
    plt.subplots_adjust(left=0.35)

    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
    os.makedirs(static_dir, exist_ok=True)

    plt.savefig(
        os.path.join(static_dir, "chart.png"),
        dpi=150,
        bbox_inches="tight"
    )
    plt.close()



@app.route("/")
def dashboard():
    df = load_data()

    if df.empty:
        return "No data found. Run the scraper first."

    generate_chart(df)

    stats = {
        "count": len(df),
        "avg_price": round(df["price"].mean(), 2),
        "min_price": df["price"].min(),
        "max_price": df["price"].max()
    }

    products = df.to_dict(orient="records")

    return render_template(
        "dashboard.html",
        products=products,
        stats=stats
    )


if __name__ == "__main__":
    app.run(debug=True)
