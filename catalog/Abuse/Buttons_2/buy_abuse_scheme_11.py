from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

router = Router()

@router.callback_query(lambda c: c.data == "abuse_sch_discounts")
async def abuse_sch_discounts_callback(callback_query: types.CallbackQuery):
    caption = (
        "<b>💸 10К/день на абузе скидок</b>\n\n"
        "💰 <b>Заработок:</b> от 500₽ до 10.000₽/день\n"
        "⚪️ <b>Цвет:</b> белый\n"
        "💸 <b>Вложения:</b> не требуются\n"
        "⏳ <b>Срок жизни:</b> вечно\n"
        "⛰ <b>ГЕО:</b> не важно\n"
        "🤼‍♀️ <b>Конкуренция:</b> низкая\n\n"
        "<b>Описание от автора:</b>\n"
        "🔥 Кристально белая тема\n"
        "🔥 Работает уже больше года\n"
        "🔥 Подходит даже тем, кто далёк от схем\n"
        "🔥 Возможность заказывать с разных магазинов\n"
        "🔥 Это <b>не рефаунд</b>, не скидочные карты и не бонус-боты\n"
        "🔥 <b>Можно покупать каждый день — заказов неограниченно</b>\n\n"
        "📌 <i>Заработок — без вложений, окупаемость в первый же день.</i>\n\n"
        "💸 <b>Цена у автора:</b> 7 900₽\n"
        "🔥 <b>Наша цена:</b> 1 875₽"
    )

    photo = FSInputFile("catalog/Abuse/images/abuse_sch_11.jpg")  # Файл должен быть локально

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить за 1875₽", callback_data="pay_abuse_sch_discounts")],
        [InlineKeyboardButton(text="🎁 Есть промокод", callback_data="promo_abuse_sch_discounts")],
        [InlineKeyboardButton(text="📤 Поделиться", switch_inline_query="10К/день на абузе скидок — без вложений, белая схема!")],
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
