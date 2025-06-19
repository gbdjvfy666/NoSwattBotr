from aiogram import Router, F, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime, timedelta
import asyncio
router = Router()

# Шаг 1: Нажата кнопка "💳 Пополнить баланс"
@router.message(F.text == "💳 Пополнить баланс")
async def choose_topup_amount(message: types.Message):
    await message.answer_sticker("CAACAgEAAxkBAAEP9JJoUu4YIoE_gpbfCX2RykWP0SfseAACfQIAAt8Z2EZFq0nDcXOtczYE")
    await asyncio.sleep(0.3)
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="250", callback_data="amount_250"),
            InlineKeyboardButton(text="500", callback_data="amount_500"),
            InlineKeyboardButton(text="1000", callback_data="amount_1000"),
            InlineKeyboardButton(text="2000", callback_data="amount_2000")
        ],
        [
            InlineKeyboardButton(text="3000", callback_data="amount_3000"),
            InlineKeyboardButton(text="4000", callback_data="amount_4000"),
            InlineKeyboardButton(text="5000", callback_data="amount_5000")
        ],
        [
            InlineKeyboardButton(text="10000", callback_data="amount_10000"),
            InlineKeyboardButton(text="15000", callback_data="amount_15000"),
            InlineKeyboardButton(text="20000", callback_data="amount_20000")
        ],
        [InlineKeyboardButton(text="Другая сумма", callback_data="amount_custom")]
    ])

    await message.answer(
        "💳 <b>Выберите сумму пополнения:</b>",
        reply_markup=markup,
        parse_mode="HTML"
    )

# Шаг 2: Выбрана сумма — показать способы оплаты
@router.callback_query(F.data.startswith("amount_"))
async def show_payment_methods(callback: types.CallbackQuery):
    amount = callback.data.split("_")[1]

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💸 Картой/СПБ", callback_data=f"pay_card_{amount}")],
        [InlineKeyboardButton(text="💰 CryptoBot", callback_data=f"pay_crypto_{amount}")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_amount")]
    ])

    await callback.message.edit_text(
        f"💳 <b>Пополнение баланса</b>\n\n"
        f"Сумма к оплате: <b>{amount}₽</b>\n"
        f"Выберите способ оплаты:",
        reply_markup=markup,
        parse_mode="HTML"
    )
    await callback.answer()

# Шаг 3: Выбран способ оплаты — показать финальный текст
@router.callback_query(F.data.startswith("pay_"))
async def show_payment_info(callback: types.CallbackQuery):
    parts = callback.data.split("_")
    method = parts[1]
    amount = parts[2]

    expire_time = datetime.now() + timedelta(minutes=20)
    formatted_time = expire_time.strftime("%d.%m.%Y %H:%M (МСК)")

    method_text = "Картой/СПБ" if method == "card" else "CryptoBot"

    await callback.message.edit_text(
        f"💳 <b>Пополнение баланса</b>\n\n"
        f"Сумма к оплате: <b>{amount}₽</b>\n"
        f"ℹ️ Сумма пополнения указана без учёта комиссии платёжной системы, которая добавляется при оплате. "
        f"Мы делим эту комиссию с вами, чтобы сохранять для вас низкие цены и качественный сервис.\n\n"
        f"<b>Время на оплату:</b> 20 минут\n"
        f"<b>Оплатить до:</b> {formatted_time}\n\n"
        f"Вы выбрали способ оплаты: <b>{method_text}</b>",
        parse_mode="HTML"
    )
    await callback.answer()

# Назад к выбору суммы
@router.callback_query(F.data == "back_to_amount")
async def back_to_amount(callback: types.CallbackQuery):
    await choose_topup_amount(callback.message)
    await callback.answer()
