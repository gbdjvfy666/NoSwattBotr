from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

router = Router()

@router.callback_query(lambda c: c.data == "abuse_sch_6")
async def abuse_sch_6_callback(callback_query: types.CallbackQuery):
    caption = (
        "<b>📈 Получаем 25–65% к депозиту с круга</b>\n\n"
        "<b>Описание от автора:</b>\n"
        "Идеальное решение для тех, кто хочет ничего не делать и получать деньги на пассиве.\n\n"
        "📚 Обучение заработку 25% с круга за 30 минут.\n"
        "⚠️ Гарантия окупаемости через 24 часа после покупки.\n"
        "💳 Схема максимально простая и связана с абузом банков.\n\n"
        "🔹 Цвет: белый\n"
        "🔹 Без дропов\n"
        "🔹 Можно работать со старого ПК\n"
        "🔹 Вложения: 5.000₽ (или от 2.000₽ при наличии ресурсов)\n"
        "🔹 Круг занимает ~30 минут\n\n"
        "💰 <b>Заработок:</b> от 1.250₽ за круг\n"
        "⚪️ <b>Цвет:</b> белый\n"
        "💸 <b>Вложения:</b> от 2.000–5.000₽ (возвращаются сразу)\n"
        "⏳ <b>Срок жизни:</b> долгий\n"
        "🌍 <b>ГЕО:</b> не важно\n"
        "🤼‍♀️ <b>Конкуренция:</b> ниже среднего\n\n"
        "💸 <b>Цена у автора:</b> 17 700₽\n"
        "🔥 <b>Цена у нас:</b> 2 002.5₽"
    )

    photo = FSInputFile("catalog/Abuse/images/abuse_sch_6.jpg")  # убедись, что файл существует

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить за 2002.5₽", callback_data="pay_abuse_sch_6")],
        [InlineKeyboardButton(text="🎁 Есть промокод", callback_data="promo_abuse_sch_6")],
        [InlineKeyboardButton(text="📤 Поделиться", switch_inline_query="Получаем 25–65% к депозиту с круга")],
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
