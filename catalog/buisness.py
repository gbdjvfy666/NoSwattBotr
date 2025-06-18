from aiogram import Router, types
from aiogram.types import FSInputFile

router = Router()

@router.callback_query(lambda c: c.data == "item_business")
async def business_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("images/buisness.jpg")  # Проверь, что путь к файлу корректен

    caption = (
        "💻 <b>Готовый бизнес</b> 🚀\n\n"
        "➥ В этом разделе собраны <b>готовые решения</b> для старта заработка.\n"
        "➥ Не нужен ПК, не нужны глубокие знания — <b>всё уже сделано за вас</b>.\n"
        "➥ Пошаговые инструкции, материалы, оформление, источники трафика и связки — включено.\n\n"
        "⚙️ <i>Хочешь больше гибкости и тонкой настройки?</i> — загляни в раздел <b>«Скрипты»</b>, там ещё больше проектов, которые можно доработать под себя.\n\n"
        "🚀 Запускай и зарабатывай без лишней подготовки!"
    )

    await callback_query.message.answer_photo(
        photo=photo,
        caption=caption,
        parse_mode="HTML"
    )

    await callback_query.answer()
