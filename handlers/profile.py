from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.callback_query(F.data == "profile")
async def profile_view(callback: CallbackQuery):
    user_id = callback.from_user.id
    text = (
        f"🪪 Мой профиль\n\n"
        f"ID: {user_id}\n"
        f"Регистрация: 16.06.2025\n\n"
        f"Основной баланс: 0₽\n"
        f"Партнёрский баланс: 0₽\n\n"
        f"Статистика\nВсего покупок: 0\n"
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛒 Мои заказы", callback_data="my_orders")],
        [InlineKeyboardButton(text="💳 Пополнить", callback_data="topup")],
        [InlineKeyboardButton(text="🤝 Реферальная программа", callback_data="referral")]
    ])
    await callback.message.edit_text(text, reply_markup=kb)