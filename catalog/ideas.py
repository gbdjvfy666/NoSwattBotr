from aiogram import Router, types
from aiogram.types import FSInputFile

router = Router()

@router.callback_query(lambda c: c.data == "item_ideas")
async def ideas_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("images/Bidea.jpg")  # Убедись, что файл images/ideas.jpg существует

    caption = (
        "✨ Бизнес идеи\n\n"
        "➥В данном разделе находятся лучшие бизнес идеи, с помощью которых уже в ближайшие дни каждый из вас сможет стать предпринимателем, главное - придерживаться инструкции, и верить в себя.\n\n"
        "Бизнес идеи только по самым доступным ценам!"
    )

    await callback_query.message.answer_photo(
        photo=photo,
        caption=caption,
        parse_mode="HTML"
    )

    await callback_query.answer()
