from aiogram import Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.callback_query(lambda c: c.data == "item_proxies")
async def proxies_callback(callback_query: types.CallbackQuery):
    caption = (
        "💎 <b>Прокси</b>\n\n"
        "❗️Мы не предоставляем прокси под чёрные цели! Вы несёте полную ответственность за свои действия!\n"
        "<a href='https://telegra.ph/Pravila-soglasheniya-i-politika-08-06'>»подробнее«</a>\n\n"
        "Выберите тип прокси:"
    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Приватные IPv4", callback_data="proxy_private_ipv4")],
        [InlineKeyboardButton(text="Общие IPv4", callback_data="proxy_shared_ipv4")],
        [InlineKeyboardButton(text="Приватные IPv6", callback_data="proxy_private_ipv6")],
        [InlineKeyboardButton(text="📜 История заказов", callback_data="proxy_history")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_shop")]
    ])

    await callback_query.message.answer(
        text=caption,
        parse_mode="HTML",
        reply_markup=markup
    )

    await callback_query.answer()
