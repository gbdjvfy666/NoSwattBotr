from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from database import get_or_create_user, get_user_profile
import asyncio
router = Router()

@router.message(F.text == "🪪 Мой профиль")
async def profile_handler(message: Message):
    
    await message.answer_sticker("CAACAgEAAxkBAAEP9ExoUudPQIu6fJYvt7IVC2Z-XzLvXwACugIAAiz4MEQksGc-EyV1qTYE")
    await asyncio.sleep(0.3)

    user_id = message.from_user.id
    await get_or_create_user(user_id)

    profile = await get_user_profile(user_id)
    if not profile:
        await message.answer("⚠️ Не удалось получить данные профиля.")
        return

    registration_date, balance, partner_balance, purchases = profile

    text = (
        "🪪 <b>Мой профиль</b>\n\n"
        f"ID: <code>{user_id}</code>\n"
        f"Регистрация: {registration_date}\n\n"
        f"Основной баланс: <b>{balance}₽</b>\n"
        f"Партнерский баланс: <b>{partner_balance}₽</b>\n\n"
        "📊 <b>Статистика</b>\n"
        f"Всего покупок: <b>{purchases}</b>"
    )

    # Создаем inline-кнопки
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📦 Мои заказы", callback_data="my_orders"),
         InlineKeyboardButton(text="💳 Пополнить", callback_data="top_up")],
        [InlineKeyboardButton(text="👥 Реферальная программа", callback_data="referral_program")]
    ])

    await message.answer(text, parse_mode="HTML", reply_markup=markup)
