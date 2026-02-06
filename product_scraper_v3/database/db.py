import sqlite3

DB_NAME = "data/products.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL,
            rating REAL,
            scraped_date TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_product(product):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO products (name, price, rating, scraped_date)
        VALUES (?, ?, ?, ?)
    """, (
        product["name"],
        product["price"],
        product["rating"],
        product["date"]
    ))

    conn.commit()
    conn.close()
