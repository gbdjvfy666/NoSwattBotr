from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton

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

    # Инлайн-кнопки
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔥 Лучшие схемы", callback_data="shema_best")],
        [InlineKeyboardButton(text="💼 Схемы заработка", callback_data="shema_money")],
        [InlineKeyboardButton(text="💸 Дешевые схемы", callback_data="shema_cheap")],
        [InlineKeyboardButton(text="📦 Паки схем", callback_data="shema_packs")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_shop")]
    ])

    await callback_query.message.answer_photo(
        photo=photo,
        caption=caption,
        parse_mode="HTML",
        reply_markup=markup
    )

    await callback_query.answer()
