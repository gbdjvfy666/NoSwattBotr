from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.callback_query(lambda c: c.data == "item_traffic")
async def traffic_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("images/traffic_cover.jpg")  # Обнови путь к файлу, если нужно

    caption = (
        "🔥 <b>Деньги на Трафике</b> 🔥\n\n"
        "Исключительно рабочие материалы, написанные топовыми арбитражниками, УБТшниками и SEOшниками, \n"
        "специально для наших покупателей. Только реальные кейсы, поэтому это \u043dе просто \"\u043fродажа информации\", \n"
        "а продажа многолетнего опыта, который стоит дороже любых теорий.\n\n"
        "Каждый материал — это пошаговый путь, от нуля и до профита, которым авторы сами зарабатывают деньги \n"
        "прямо сейчас. Это не просто кейсы по привлечению трафика, но и готовые инструкции \n"
        "по его монетизации.\n\n"
        "<b>Форматы обучения:</b>\n"
        "📖 - текстовый\n"
        "📹 - видео\n"
        "💻 - видео и текст\n\n"
        "Если хочешь лить и зарабатывать по настоящему — начни прямо сейчас! 👇"
    )

    await callback_query.message.answer_photo(
        photo=photo,
        caption=caption,
        parse_mode="HTML"
    )
    await callback_query.answer()
