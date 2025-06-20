from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

router = Router()

@router.callback_query(lambda c: c.data == "abuse_3")
async def abuse_3_callback(callback_query: types.CallbackQuery):
    caption = (
        "<b>📈 Абуз ПП — 320 руб./круг</b>\n\n"
        "💰 <b>Заработок:</b> 320 руб./круг\n"
        "⚪️ <b>Цвет:</b> белый\n"
        "💸 <b>Вложения:</b> 0–400 руб.\n"
        "⏳ <b>Срок жизни:</b> неизвестно\n"
        "⛰ <b>Гео:</b> не важно\n"
        "🤼‍♀️ <b>Конкуренция:</b> почти нет\n\n"
        "<b>Описание от автора:</b>\n"
        "➥ За круг получаем 320+ рублей, крутим на 1 аккаунт по 15–20 заявок.\n"
        "➥ Новый способ абуза ПП — ничего подобного вы не видели.\n"
        "➥ Не связан с картами, акциями, поддержкой, МФО.\n"
        "➥ Без расходников (но при вложении 300–400₽ результат выше).\n"
        "➥ Огромный мануал — от А до Я, всё понятно и легко.\n"
        "➥ Можно работать с телефона.\n"
        "➥ <u>Не</u> марафонбет, не леон, не винлайн, не бетбум и т.д.\n"
        "➥ Схема <b>не была в паблике</b>.\n\n"
        "💸 <b>Цена у автора:</b> 13 599₽\n"
        "🔥 <b>Цена у нас:</b> 1 950₽"
    )

    photo = FSInputFile("catalog/Abuse/images/abuse_3.jpg")

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить за 1950₽", callback_data="pay_abuse_3")],
        [InlineKeyboardButton(text="🎁 Есть промокод", callback_data="promo_abuse_3")],
        [InlineKeyboardButton(text="📤 Поделиться", switch_inline_query="Абуз ПП — 320 руб./круг")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="buy_best_abuse")]
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
