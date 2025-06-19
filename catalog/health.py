from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.callback_query(lambda c: c.data == "item_health")
async def health_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("images/health.jpg")

    caption = (
        "🍃 <b>Здоровье</b>\n\n"
        "➥ Стабильный заработок, саморазвитие, познание нового — это круто.\n"
        "Но всё это теряет смысл, если забывать о главном — <b>о своём здоровье</b>.\n\n"
        "⚡️ В этом разделе ты найдёшь:\n"
        "• Авторские программы тренировок 🏋️‍♂️\n"
        "• Рабочие диеты 🍽\n"
        "• Подборки лучших добавок для продуктивности 💊\n\n"
        "🌿 Заботься о себе. Вкладывай в здоровье с умом."
    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🥗 Именные программы питания • 1500₽", callback_data="health_diet")],
        [InlineKeyboardButton(text="🏃‍♂️ Курс: спорт без инвентаря • 1500₽", callback_data="health_course")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_shop")]
    ])

    await callback_query.message.answer_photo(
        photo=photo,
        caption=caption,
        parse_mode="HTML",
        reply_markup=markup
    )

    await callback_query.answer()
