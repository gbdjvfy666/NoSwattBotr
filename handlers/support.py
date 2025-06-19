from aiogram import Router, F, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

router = Router()

# Обработка кнопки "🆘 Связаться с поддержкой"
@router.message(F.text == "📩 Связаться")
async def support_main(message: types.Message):
    await message.answer_sticker("CAACAgEAAxkBAAEP9JBoUu3FQj3Bri3TkCFSDEaegKUfUgACNQIAAtkboEY5xCjIsSP_yTYE")
    await asyncio.sleep(0.3)
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📨 Создать обращение", callback_data="support_create")],
        [InlineKeyboardButton(text="📂 Мои обращения", callback_data="support_my_tickets")]
    ])
    await message.answer("🛠 Здесь вы можете обратиться в службу поддержки:", reply_markup=markup)


# Обработка "Создать обращение"
@router.callback_query(F.data == "support_create")
async def choose_topic(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📦 Проблема с заказом", callback_data="topic_order")],
        [InlineKeyboardButton(text="💳 Проблема с пополнением", callback_data="topic_topup")],
        [InlineKeyboardButton(text="💰 Проблема с оплатой", callback_data="topic_payment")],
        [InlineKeyboardButton(text="📋 Вопрос по товару", callback_data="topic_product")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_support")]
    ])
    await callback.message.edit_text(
        "🆘 <b>Служба поддержки › Выбор темы</b>\n\n"
        "Выберите тему обращения:",
        reply_markup=markup,
        parse_mode="HTML"
    )
    await callback.answer()


# Обработка "Назад" в выбор темы
@router.callback_query(F.data == "back_to_support")
async def back_to_support(callback: types.CallbackQuery):
    await support_main(callback.message)
    await callback.answer()
