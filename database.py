import aiosqlite
from datetime import datetime

DB_PATH = "database.db"

async def create_user_table():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                registration_date TEXT,
                balance INTEGER DEFAULT 0,
                partner_balance INTEGER DEFAULT 0,
                purchases INTEGER DEFAULT 0
            )
        """)
        await db.commit()

async def get_or_create_user(user_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)) as cursor:
            user = await cursor.fetchone()
        if not user:
            date = datetime.now().strftime("%d.%m.%Y")
            await db.execute(
                "INSERT INTO users (user_id, registration_date) VALUES (?, ?)",
                (user_id, date)
            )
            await db.commit()

async def get_user_profile(user_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(
            "SELECT registration_date, balance, partner_balance, purchases FROM users WHERE user_id = ?",
            (user_id,)
        ) as cursor:
            return await cursor.fetchone()
