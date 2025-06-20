from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

router = Router()

@router.callback_query(lambda c: c.data == "abuse_sch_2")
async def abuse_sch_2_callback(callback_query: types.CallbackQuery):
    caption = (
        "<b>📞 Абуз партнёрки на звонках</b>\n\n"
        "<b>Описание от автора:</b>\n"
        "✅ Настройка 2–3 часа, затем 1 час в день\n"
        "✅ Работа онлайн — смартфон или ПК, не важно\n"
        "✅ Белая схема: без продаж, без общения, без поиска\n"
        "✅ Профит уже в первые 2–3 дня\n\n"
        "💰 <b>Заработок:</b> до 70 000₽\n"
        "⚫️ <b>Цвет:</b> Чёрный\n"
        "💸 <b>Вложения:</b> 150₽\n"
        "⏳ <b>Срок жизни:</b> достаточно долго\n"
        "⛰ <b>Гео:</b> любое\n"
        "🤼‍♀️ <b>Конкуренция:</b> низкая\n\n"
        "💸 <b>Цена у автора:</b> 13 000₽\n"
        "🔥 <b>Цена у нас:</b> 2 092.5₽"
    )

    photo = FSInputFile("catalog/Abuse/images/abuse_sch_2.jpg")  # Замени путь на актуальный

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить за 2092.5₽", callback_data="pay_abuse_sch_2")],
        [InlineKeyboardButton(text="🎁 Есть промокод", callback_data="promo_abuse_sch_2")],
        [InlineKeyboardButton(text="📤 Поделиться", switch_inline_query="Абуз партнёрки на звонках")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="buy_abuse_schemes")]
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
