from aiogram import Router, types
from aiogram.types import FSInputFile

router = Router()

@router.callback_query(lambda c: c.data == "item_scripts")
async def scripts_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("images/scripts.jpg")  # Убедись, что файл images/scripts.jpg существует

    caption = (
        "⚙️ Скрипты\n\n"
        "➥Дорогостоящие скрипты по самым доступным ценам."
    )

    await callback_query.message.answer_photo(
        photo=photo,
        caption=caption,
        parse_mode="HTML"
    )

    await callback_query.answer()
