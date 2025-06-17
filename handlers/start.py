from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

router = Router()

@router.message(F.text == "/start")
async def start_handler(message: Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🏪 Каталог товаров"), KeyboardButton(text="💳 Пополнить баланс")],
            [KeyboardButton(text="🪪 Мой профиль"), KeyboardButton(text="📩 Связаться")],
            [KeyboardButton(text="🎁ПОЛУЧИ БОНУСЫ🎁")],
        ],
        resize_keyboard=True
    )
    await message.answer("👋 Добро пожаловать в магазин!", reply_markup=kb)
