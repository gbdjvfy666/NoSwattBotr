from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.callback_query(lambda c: c.data == "item_business")
async def business_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("images/business.jpg")  # Убедись, что файл существует

    caption = (
        "💻 <b>Готовый бизнес</b> 🚀\n\n"
        "➥ В данном разделе вы можете приобрести готовые бизнес-решения. "
        "Для реализации большинства из них вам даже не понадобится ПК и каких-то дополнительных знаний, "
        "так как всё уже решено и расписано за вас.\n\n"
        "🧠 Также много интересных готовых проектов вы можете найти в разделе «⚙️СКРИПТЫ⚙️»"
    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="CRYPTO-HACK | Взлом и угон крипты • 17.850₽", callback_data="biz_crypto_hack")],
        [InlineKeyboardButton(text="100.000₽/мес на боте ChatGPT! • 2550₽", callback_data="biz_gpt_bot")],
        [InlineKeyboardButton(text="ТОП Телеграм магазин • 3450₽", callback_data="biz_shop")],
        [InlineKeyboardButton(text="ТОП Копия казино UPX • 4950₽", callback_data="biz_upx")],
        [InlineKeyboardButton(text="Интим Бот - скам дрочеров • 2998.5₽", callback_data="biz_intim")],
        [InlineKeyboardButton(text="Свой гарант-сервис • 3300₽", callback_data="biz_guarantee")],
        [InlineKeyboardButton(text="ТОП Казино WINX Barkin • 5998.5₽", callback_data="biz_winx")],
        [InlineKeyboardButton(text="Криптоскам проект (пассив) • 3980₽", callback_data="biz_crypto_scam")],
        [InlineKeyboardButton(text="Топ Opencase CSGO — казино • 2100₽", callback_data="biz_opencase")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_shop")]
    ])

    await callback_query.message.answer_photo(
        photo=photo,
        caption=caption,
        parse_mode="HTML",
        reply_markup=markup
    )

    await callback_query.answer()
