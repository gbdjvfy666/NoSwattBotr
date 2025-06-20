from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

router = Router()

@router.callback_query(lambda c: c.data == "abuse_sch_5")
async def abuse_sch_5_callback(callback_query: types.CallbackQuery):
    caption = (
        "<b>💸 Абуз ПП — 2.000₽/круг</b>\n\n"
        "<b>Описание от автора:</b>\n"
        "Мануал по абузу партнёрской программы, где за целевое действие платят 2.800₽.\n"
        "Расход на один круг — около 800₽, на выходе — чистые 2.000₽. Аппрув — 100%.\n"
        "⏱ Один круг — до 30 минут. Желателен iOS.\n\n"
        "📈 Цвет — белый. Без оформления карт, кредитов, казино, БК и МФО.\n"
        "Дропы не нужны. Для масштабирования — прокси и антидетект-браузер.\n\n"
        "💰 <b>Заработок:</b> от 2.000₽/круг\n"
        "⚪️ <b>Цвет:</b> Белый\n"
        "💸 <b>Вложения:</b> ~800₽\n"
        "⏳ <b>Срок жизни:</b> долгий\n"
        "🌍 <b>ГЕО:</b> любое\n"
        "🤼‍♀️ <b>Конкуренция:</b> пока нет\n\n"
        "💸 <b>Цена у автора:</b> 18 000₽\n"
        "🔥 <b>Цена у нас:</b> 1 950₽"
    )

    photo = FSInputFile("catalog/Abuse/images/abuse_sch_5.jpg")  # замените путь, если нужно

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить за 1950₽", callback_data="pay_abuse_sch_5")],
        [InlineKeyboardButton(text="🎁 Есть промокод", callback_data="promo_abuse_sch_5")],
        [InlineKeyboardButton(text="📤 Поделиться", switch_inline_query="Абуз партнёрки 2000₽/круг")],
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
