import sqlite3

def initialize_db():
    conn = sqlite3.connect("recommendation.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY,
                        name TEXT,
                        age INTEGER,
                        gender TEXT,
                        location TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        product_id INTEGER PRIMARY KEY,
                        name TEXT,
                        category TEXT,
                        price REAL,
                        tags TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS user_behavior (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        product_id INTEGER,
                        action TEXT)''')

    # Insert dummy data only once
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO users (user_id, name, age, gender, location) VALUES (1, 'Alice', 25, 'F', 'NY')")
        cursor.execute("INSERT INTO user_behavior (user_id, product_id, action) VALUES (1, 101, 'view')")
        cursor.execute("INSERT INTO user_behavior (user_id, product_id, action) VALUES (1, 102, 'purchase')")
        cursor.execute("INSERT INTO products (product_id, name, category, price, tags) VALUES (101, 'Phone', 'Electronics', 699.99, 'tech,smartphone')")
        cursor.execute("INSERT INTO products (product_id, name, category, price, tags) VALUES (102, 'Headphones', 'Electronics', 199.99, 'tech,audio')")
        cursor.execute("INSERT INTO products (product_id, name, category, price, tags) VALUES (103, 'Charger', 'Electronics', 29.99, 'tech,power')")

    conn.commit()
    conn.close()

def get_user_behavior(user_id):
    conn = sqlite3.connect("recommendation.db")
    cursor = conn.cursor()
    cursor.execute("SELECT product_id FROM user_behavior WHERE user_id = ?", (user_id,))
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]

def get_product_info(product_id):
    conn = sqlite3.connect("recommendation.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, category, price, tags FROM products WHERE product_id = ?", (product_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            "product_id": product_id,
            "name": row[0],
            "category": row[1],
            "price": row[2],
            "tags": row[3]
        }
    return None
