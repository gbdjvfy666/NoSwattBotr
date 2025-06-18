from aiogram import Router, types
from aiogram.types import FSInputFile

router = Router()

@router.callback_query(lambda c: c.data == "item_shema")
async def shema_callback(callback_query: types.CallbackQuery):
    # Обложка для раздела «Схемы»
    photo = FSInputFile("images/shema.jpg")

    caption = (
        "💰 <b>Схемы</b>\n\n"
        "➥ Рабочие методы и связки\n"
        "➥ На любой вкус, цвет и бюджет\n\n"
        "📈 Лей, зарабатывай, масштабируй!"
    )

    await callback_query.message.answer_photo(
        photo=photo,
        caption=caption,
        parse_mode="HTML"
    )

    await callback_query.answer()
