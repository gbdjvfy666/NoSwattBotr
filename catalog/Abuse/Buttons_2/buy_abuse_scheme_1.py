from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

router = Router()

@router.callback_query(lambda c: c.data == "abuse_sch_1")
async def abuse_sch_1_callback(callback_query: types.CallbackQuery):
    caption = (
        "<b>🛍 Очень жирный абуз Wildberries</b>\n\n"
        "<b>Описание от автора:</b>\n"
        "💰 Заработок на Wildberries — профит ограничен только вашим желанием и вложениями.\n"
        "В среднем приносит <b>60–100 тыс. руб/мес</b>.\n"
        "Тема будет жить вечно, пока жив сам ВБ.\n"
        "🔒 Набор <b>до 10 учеников</b>, гарант до профита.\n\n"
        "<b>Краткое описание схемы:</b>\n"
        "➤ Серые оттенки, но <b>полностью легально</b>\n"
        "➤ Достаточно телефона для работы\n"
        "➤ С некоторых товаров возврат 500–1000₽ и выше\n"
        "➤ Вложения от 500₽ (желательно 5–10К для хорошего старта)\n"
        "➤ Профит уже на 3-й день (30–50% от вложений)\n\n"
        "💰 <b>Средний заработок:</b> 60–100 000₽\n"
        "⚪️ <b>Цвет:</b> белый\n"
        "💸 <b>Вложения:</b> физические SIM-карты\n"
        "⏳ <b>Срок жизни:</b> будет жить вечно\n"
        "⛰ <b>Гео:</b> без ограничений\n"
        "🤼‍♀️ <b>Конкуренция:</b> нет\n\n"
        "💸 <b>Цена у автора:</b> 38 000₽\n"
        "🔥 <b>Цена у нас:</b> 1 687.5₽"
    )

    photo = FSInputFile("catalog/Abuse/images/abuse_sch_1.jpg")  # Замени путь, если фото в другом месте

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить за 1687.5₽", callback_data="pay_abuse_sch_1")],
        [InlineKeyboardButton(text="🎁 Есть промокод", callback_data="promo_abuse_sch_1")],
        [InlineKeyboardButton(text="📤 Поделиться", switch_inline_query="Очень жирный абуз Wildberries")],
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
 