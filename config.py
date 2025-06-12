from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

MAIN_CHANNEL = "@noswattt"  # Основной канал для проверки
EXTRA_CHANNELS = [
    ("NS — Личный бренд", "https://t.me/noswattt"),
    ("NSP — Арбитраж и партнёрки", "https://t.me/nospartners"),
    ("NSB — Прогнозы и ставки", "https://t.me/noswattbet"),
]