from aiogram import Router, types
from aiogram.types import FSInputFile

router = Router()

@router.callback_query(lambda c: c.data == "item_lastticket")
async def last_ticket_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("images/last.jpg")  # Убедись, что файл images/lastticket.jpg есть

    caption = (
        "🎰 Последний билет 🎟️\n\n"
        "Испытай удачу и забери главный приз от 5000 до 300.000 рублей - прямо сейчас! 💰\n\n"
        "В этой уникальной лотерее последний купленный билет становится победным. Всего 30 билетов с разными призами, "
        "которые зависят от выбранного вами билета. Чем больше билетов, тем выше твой шанс стать счастливчиком!\n\n"
        "🔑 Особенность: игра идет до последнего билета – успей сделать свой ход! 💳 Приз легко выводится на любые реквизиты, включая крипту.\n\n"
        "⏳ Не жди, пока кто-то другой станет победителем – играй первым, чтобы победить последним! 🚀\n\n"
        "👇ВЫБЕРИ БИЛЕТ👇"
    )

    await callback_query.message.answer_photo(
        photo=photo,
        caption=caption,
        parse_mode="HTML"
    )

    await callback_query.answer()
