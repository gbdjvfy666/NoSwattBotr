import aiosqlite

DB_NAME = "bot.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tg_id INTEGER UNIQUE,
            username TEXT,
            full_name TEXT
        )""")
        await db.execute("""
        CREATE TABLE IF NOT EXISTS proxies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            proxy TEXT,
            is_issued INTEGER DEFAULT 0
        )""")
        await db.execute("""
        CREATE TABLE IF NOT EXISTS issued_proxies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tg_id INTEGER,
            proxy TEXT,
            issued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")
        await db.commit()

async def add_user(tg_id, username, full_name):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        INSERT OR IGNORE INTO users (tg_id, username, full_name)
        VALUES (?, ?, ?)""", (tg_id, username, full_name))
        await db.commit()

async def get_free_proxy():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT id, proxy FROM proxies WHERE is_issued = 0 LIMIT 1") as cursor:
            row = await cursor.fetchone()
            if row:
                proxy_id, proxy = row
                await db.execute("UPDATE proxies SET is_issued = 1 WHERE id = ?", (proxy_id,))
                await db.commit()
                return proxy
    return None

async def log_issued_proxy(tg_id, proxy):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        INSERT INTO issued_proxies (tg_id, proxy)
        VALUES (?, ?)""", (tg_id, proxy))
        await db.commit()