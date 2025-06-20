from aiogram import Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

router = Router()

@router.callback_query(lambda c: c.data == "abuse_sch_3")
async def abuse_sch_3_callback(callback_query: types.CallbackQuery):
    caption = (
        "<b>🚕 Катаемся бесплатно на Янд3кс.Такси / UB3R</b>\n\n"
        "<b>Описание от автора:</b>\n"
        "🚖 Схема рефанда полностью белая\n"
        "🚕 Возвращают средства почти всегда\n"
        "🚖 Если не вернут — дадут промокод\n"
        "🚕 Для рефанда нужен только смартфон\n"
        "🚖 Всё расписано очень понятным языком\n\n"
        "⚪️ <b>Цвет:</b> Белый\n"
        "💸 <b>Максимум:</b> поездки до 1000₽\n"
        "⏳ <b>Срок жизни:</b> предпосылок смерти нет\n"
        "⛰ <b>Гео:</b> без ограничений\n"
        "🤼‍♀️ <b>Конкуренция:</b> нет\n\n"
        "💸 <b>Цена у автора:</b> 17 000₽\n"
        "🔥 <b>Цена у нас:</b> 1 950₽"
    )

    photo_url = "https://cdn.1dmp.shop/iWWtLmlCmR7mPx0tH"

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить за 1950₽", callback_data="pay_abuse_sch_3")],
        [InlineKeyboardButton(text="🎁 Есть промокод", callback_data="promo_abuse_sch_3")],
        [InlineKeyboardButton(text="📤 Поделиться", switch_inline_query="Катаемся бесплатно на Яндекс.Такси / UBER")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="buy_abuse_schemes")]
    ])

    await callback_query.message.edit_media(
        media=InputMediaPhoto(
            media=photo_url,
            caption=caption,
            parse_mode="HTML"
        ),
        reply_markup=markup
    )

    await callback_query.answer()
