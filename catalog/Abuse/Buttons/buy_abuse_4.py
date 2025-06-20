from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

router = Router()

@router.callback_query(lambda c: c.data == "abuse_4")
async def abuse_4_callback(callback_query: types.CallbackQuery):
    caption = (
        "<b>📦 Абуз Ozon — бесплатные товары</b>\n\n"
        "Новая схема, при помощи которой вы сможете <b>бесплатно покупать вещи на Озон</b>. "
        "⚠️ Прошу не злоупотреблять: схему обнаружили <b>буквально пару дней назад</b>.\n\n"
        "💸 <b>Вложения:</b> не требуются\n"
        "⚡️ <b>Профит:</b> быстрый\n"
        "❤️ <b>Срок жизни:</b> от года и более\n\n"
        "💸 <b>Цена у автора:</b> 7 999₽\n"
        "🔥 <b>Цена у нас:</b> 2 512.5₽"
    )

    photo = FSInputFile("catalog/Abuse/images/abuse_4.jpg")  # Убедись, что файл существует

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить за 2512.5₽", callback_data="pay_abuse_4")],
        [InlineKeyboardButton(text="🎁 Есть промокод", callback_data="promo_abuse_4")],
        [InlineKeyboardButton(text="📤 Поделиться", switch_inline_query="Абуз Ozon — бесплатные товары")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="buy_best_abuse")]
    ])

    await callback_query.message.edit_media(
        media=InputMediaPhoto(
            media=photo,
            caption=caption,
            parse_mode="HTML"
        ),
        reply_markup=markup
    )

    await callback_query.answer()
