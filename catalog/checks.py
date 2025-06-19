from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton

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

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="ЧЕКИ С БАЛАНСОМ • 750₽", callback_data="check_basic")],
        [InlineKeyboardButton(text="GOLD ЧЕКИ С БАЛАНСОМ • 899₽", callback_data="check_gold")],
        [InlineKeyboardButton(text="VIP ЧЕКИ С БАЛАНСОМ • 1875₽", callback_data="check_vip")],
        [InlineKeyboardButton(text="ОПТ | ЧЕКИ С БАЛАНСОМ • 5250₽", callback_data="check_opt")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_catalog")]
    ])

    await callback_query.message.answer_photo(
        photo=photo,
        caption=caption,
        reply_markup=markup,
        parse_mode="HTML"
    )

    await callback_query.answer()
