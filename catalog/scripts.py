from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.callback_query(lambda c: c.data == "item_scripts")
async def scripts_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("images/scripts.jpg")  # Убедись, что файл images/scripts.jpg существует

    caption = (
        "⚙️ <b>Скрипты</b>\n\n"
        "➥ Дорогостоящие скрипты по самым доступным ценам."
    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="TG БОТЫ", callback_data="scripts_tgbots"),
         InlineKeyboardButton(text="САЙТЫ", callback_data="scripts_sites")],
        [InlineKeyboardButton(text="ХАКИНГ", callback_data="scripts_hacking"),
         InlineKeyboardButton(text="РАЗНОЕ", callback_data="scripts_other")],
        [InlineKeyboardButton(text="ПАССИВНЫЙ ЗАРАБОТОК", callback_data="scripts_passive")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_catalog")]
    ])

    await callback_query.message.answer_photo(
        photo=photo,
        caption=caption,
        reply_markup=markup,
        parse_mode="HTML"
    )

    await callback_query.answer()
