from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
router = Router()

@router.callback_query(lambda c: c.data == "abuse_5")
async def abuse_5_callback(callback_query: types.CallbackQuery):
    caption = (
        "<b>🎁 Бонусхантинг до 6.000₽/круг</b>\n\n"
        "💰 <b>Заработок:</b> до 6.000 руб/круг\n"
        "⚪️ <b>Цвет:</b> белый\n"
        "💸 <b>Вложения:</b> 50–60 руб/круг\n"
        "⏳ <b>Срок жизни:</b> долго\n"
        "⛰ <b>Гео:</b> не важно\n"
        "🤼‍♀️ <b>Конкуренция:</b> низкая\n\n"
        "<b>Описание от автора:</b>\n"
        "➤ Мануал + видео\n"
        "➤ Гео неважно\n"
        "➤ Возраст не важен\n"
        "➤ Работаю уже год, признаков смерти нет\n"
        "➤ Белая схема\n"
        "➤ Без общения с людьми\n"
        "➤ Профит до 6к за круг\n"
        "➤ Длительность круга зависит от вложений\n"
        "➤ Строки, прокси, виртуальные номера — всё нужно\n"
        "➤ Дам контакты для покупки расходников\n"
        "➤ Холда нет, мануал объясняет всё в деталях\n\n"
        "💸 <b>Цена у автора:</b> 16 800₽\n"
        "🔥 <b>Цена у нас:</b> 2 145₽"
    )

    photo = FSInputFile("catalog/Abuse/images/abuse_5.jpg") 

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить за 2145₽", callback_data="pay_abuse_5")],
        [InlineKeyboardButton(text="🎁 Есть промокод", callback_data="promo_abuse_5")],
        [InlineKeyboardButton(text="📤 Поделиться", switch_inline_query="Бонусхантинг до 6.000₽/круг")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="buy_best_abuse")]
    ])

    await callback_query.message.edit_media(
        media=InputMediaPhoto(
            media=photo_url,
            caption=caption,
            parse_mode="HTML"
        ),
        reply_markup=markup
    )

    await callback_query.answer()
