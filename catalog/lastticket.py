from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.callback_query(lambda c: c.data == "item_lastticket")
async def last_ticket_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("images/last.jpg")  # Убедись, что файл images/last.jpg есть

    caption = (
        "🎰 <b>Последний билет</b> 🎟️\n\n"
        "Испытай удачу и забери главный приз от 5000 до 300.000 рублей - прямо сейчас! 💰\n\n"
        "В этой уникальной лотерее последний купленный билет становится победным. Всего 30 билетов с разными призами, "
        "которые зависят от выбранного вами билета. Чем больше билетов, тем выше твой шанс стать счастливчиком!\n\n"
        "🔑 <b>Особенность:</b> игра идет до последнего билета – успей сделать свой ход! 💳 Приз легко выводится на любые реквизиты, включая крипту.\n\n"
        "⏳ Не жди, пока кто-то другой станет победителем – играй первым, чтобы победить последним! 🚀\n\n"
        "👇 <b>ВЫБЕРИ БИЛЕТ</b> 👇"
    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="ЗАБЕРИ 300.000 • 10500₽", callback_data="ticket_300k")],
        [InlineKeyboardButton(text="ЗАБЕРИ 100.000 • 5000₽", callback_data="ticket_100k")],
        [InlineKeyboardButton(text="ЗАБЕРИ 50.000 • 3000₽", callback_data="ticket_50k")],
        [InlineKeyboardButton(text="ЗАБЕРИ 20.000 • 1000₽", callback_data="ticket_20k")],
        [InlineKeyboardButton(text="ЗАБЕРИ 5.000 • 250₽", callback_data="ticket_5k")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_catalog")]
    ])

    await callback_query.message.answer_photo(
        photo=photo,
        caption=caption,
        reply_markup=markup,
        parse_mode="HTML"
    )

    await callback_query.answer()
