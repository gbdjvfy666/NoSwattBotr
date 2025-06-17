import sqlite3

def connect():
    return sqlite3.connect("database.db")

def create_tables():
    with connect() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                reg_date TEXT,
                balance REAL DEFAULT 0,
                partner_balance REAL DEFAULT 0,
                referrer_id INTEGER,
                total_purchases INTEGER DEFAULT 0
            )
        """)
        conn.commit()

def add_user(user_id: int, username: str, reg_date: str, referrer_id: int = None):
    with connect() as conn:
        c = conn.cursor()
        c.execute("SELECT id FROM users WHERE id = ?", (user_id,))
        if c.fetchone() is None:
            c.execute("""
                INSERT INTO users (id, username, reg_date, referrer_id)
                VALUES (?, ?, ?, ?)
            """, (user_id, username, reg_date, referrer_id))
            conn.commit()

def get_user(user_id):
    with connect() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        return c.fetchone()

def update_balance(user_id, amount):
    with connect() as conn:
        c = conn.cursor()
        c.execute("UPDATE users SET balance = balance + ? WHERE id = ?", (amount, user_id))
        conn.commit()

def update_partner_balance(user_id, amount):
    with connect() as conn:
        c = conn.cursor()
        c.execute("UPDATE users SET partner_balance = partner_balance + ? WHERE id = ?", (amount, user_id))
        conn.commit()
