from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.callback_query(lambda c: c.data == "item_seed")
async def seed_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("images/seed.jpg")  # Убедись, что файл seed.jpg есть в папке images

    caption = (
        "💲 Сид-фразы\n\n"
        "➥ База брут фраз для крипто-кошельков с реальными шансами получить кошелёк с балансом. \n\n"
        "Одна удачная покупка — и вы сможете вывести тысячи, а то и миллионы долларов! \n\n"
        "Наш приватный AI подборщик перебирает старые и забытые кошельки, тем самым делая такой вид заработка полностью легальным, "
        "ведь доступ вы получаете именно к утерянным средствам. \n\n"
        "Не упустите шанс заработать на готовых фразах, которые могут сделать вас богаче!\n\n"
        "⚡️Читай подробнее по кнопке👇"
    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="ОБЫЧНАЯ ПОКУПКА", callback_data="seed_buy_regular")],
        [InlineKeyboardButton(text="ОПТОВАЯ ПОКУПКА", callback_data="seed_buy_bulk")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_catalog")]
    ])

    await callback_query.message.answer_photo(
        photo=photo,
        caption=caption,
        reply_markup=markup,
        parse_mode="HTML"
    )

    await callback_query.answer()
