from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

router = Router()

@router.callback_query(lambda c: c.data == "abuse_1")
async def abuse_1_callback(callback_query: types.CallbackQuery):
    caption = (
        "<b>💸 Абуз партнёрки 30к/круг</b>\n\n"
        "Искал топовую тему, а вокруг только инфоцыгане? Ты нашел!\n\n"
        "➖ Продам ЛИЧНУЮ полностью белую схему абуза \"щели\" партнерской программы, "
        "откуда мы будем вытаскивать до 30К за круг!\n\n"
        "➖ В комплекте к схеме я обучу тебя фин. арбитражу и расскажу тебе как получить доступ "
        "в одну приватную партнерку (где профиты гораздо выше!)\n\n"
        "💰 <b>Доход:</b> 30К/круг (1–2 дня)\n"
        "🔸 Цвет: белый\n"
        "🔸 Полупассив\n"
        "🔸 Нет конкуренции\n"
        "🔸 Без вложений ❗️\n"
        "🔸 Без общения с людьми\n"
        "🔸 Освоит любой\n"
        "🔸 Работа с ПК/телефона\n"
        "🔸 Поддержка 24/7\n"
        "🔸 ГЕО — неважно\n\n"
        "<i>Причина продажи:</i> я сам буду работать по этой схеме, и мне нужно отобрать адекватных ребят, "
        "которые купят схему и заработают свои лёгкие деньги. С ними я создам команду и буду работать по другим проектам.\n"
        "Освоение этой схемы будет как бы испытанием😉\n\n"
        "💸 <b>Цена у автора:</b> 22 000₽\n"
        "🔥 <b>Цена у нас:</b> 2 362.5₽"
    )

    photo = FSInputFile("catalog/Abuse/images/abuse_1.jpg")  # Убедись, что файл существует

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить за 2362.5₽", callback_data="pay_abuse_1")],
        [InlineKeyboardButton(text="🎁 Есть промокод", callback_data="promo_abuse_1")],
        [InlineKeyboardButton(text="📤 Поделиться", switch_inline_query="Абуз партнёрки 30к/круг")],
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
