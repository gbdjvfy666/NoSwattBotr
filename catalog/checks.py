from aiogram import Router, types
from aiogram.types import FSInputFile

router = Router()

@router.callback_query(lambda c: c.data == "item_checks")  
async def checks_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("images/cryptobot.jpg")  

    caption = (
        "💸Чеки 🤖 с $$$\n\n"
        "Заработай мгновенно с забытыми чеками Криптобота! Продаем легально найденные чеки с гарантированным балансом, "
        "который ты можешь сразу вывести на карту или кошелек. Балансы достигают сотен и тысяч долларов!\n\n"
        "⚡️ Уникальная возможность поймать свой джекпот. Быстро, безопасно и просто. Осталось только попробовать!\n\n"
        "Читайте подробнее👇"
    )

    await callback_query.message.answer_photo(
        photo=photo,
        caption=caption,
        parse_mode="HTML"
    )

    await callback_query.answer()
