from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

router = Router()

@router.callback_query(lambda c: c.data == "abuse_sch_4")
async def abuse_sch_4_callback(callback_query: types.CallbackQuery):
    caption = (
        "<b>📺 Возврат денег за технику</b>\n"
        "<i>ОФФЛАЙН схема с форума. Высокий доход</i>\n\n"
        "<b>Описание от автора:</b>\n"
        "Схема — это полный гайд по возврату ДЕНЕГ за технику на гарантии: телефоны, телевизоры, ноутбуки, даже авто.\n"
        "Опыт с 2016 года — всё подробно и с практикой.\n\n"
        "<b>Реализация:</b>\n"
        "📍 Полностью оффлайн\n"
        "📍 Без ИП и юр.лица\n"
        "📍 Справится любой (18+)\n"
        "📍 Далее можно подключать знакомых или работников как дропов\n\n"
        "👥 Подходит для любого населённого пункта со статусом города\n\n"
        "💰 <b>Чистая прибыль:</b> от 50% до 200% с цикла\n"
        "📱 Пример: iPhone XS за 35 000₽ → 90 000₽\n"
        "⚪️ <b>Цвет:</b> Серый (без обмана)\n"
        "💸 <b>Вложения:</b> от 10 000₽ в оборот\n"
        "⏳ <b>Срок жизни:</b> бессрочно\n"
        "🌍 <b>ГЕО:</b> РФ, СНГ, Европа, США\n"
        "🤼‍♀️ <b>Конкуренция:</b> отсутствует (только рыночная)\n\n"
        "💸 <b>Цена у автора:</b> 27 500₽\n"
        "🔥 <b>Цена у нас:</b> 2 212.5₽"
    )

    photo = FSInputFile("catalog/Abuse/images/abuse_sch_4.jpg")  # Заменить при необходимости

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить за 2212.5₽", callback_data="pay_abuse_sch_4")],
        [InlineKeyboardButton(text="🎁 Есть промокод", callback_data="promo_abuse_sch_4")],
        [InlineKeyboardButton(text="📤 Поделиться", switch_inline_query="Возврат денег за технику")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="buy_abuse_schemes")]
    ])

    await callback_query.message.edit_media(
        media=InputMediaPhoto(
            media=photo,
            caption=caption,
            parse_mode="HTML"
        ),
        reply_markup=markup
    )

    await callback_query.answer()
