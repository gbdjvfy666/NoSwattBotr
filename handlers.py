from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()

# === Сообщение ===
WELCOME_TEXT = (
    "😎 Приветствую!\n\n"
    "🔒 Твоя заявка скоро будет одобрена.\n\n"
    "А пока — подпишись на наши лучшие каналы:\n\n"
    "1) <b>NS — Личный бренд, бонусы и инсайды</b>\n"
    "👉 <a href='https://t.me/noswattt'>noswattt</a>\n\n"
    "2) <b>NSP — Арбитраж и партнёрки</b>\n"
    "👉 <a href='https://t.me/nospartners'>nospartners</a>\n\n"
    "3) <b>NSB — Прогнозы и ставки</b>\n"
    "👉 <a href='https://t.me/noswattbet'>noswattbet</a>\n\n"
    "Подпишись на всё, что тебе по душе, и готовься к заработку "
)

# === /start ===
@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(WELCOME_TEXT, parse_mode="HTML", disable_web_page_preview=True)

# === Ответ на любое сообщение ===
@router.message(F.text)
async def echo_handler(message: Message):
    await message.answer(WELCOME_TEXT, parse_mode="HTML", disable_web_page_preview=True)
