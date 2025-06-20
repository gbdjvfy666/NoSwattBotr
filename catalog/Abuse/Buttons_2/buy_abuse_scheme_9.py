from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

router = Router()

@router.callback_query(lambda c: c.data == "abuse_sch_food")
async def abuse_sch_food_callback(callback_query: types.CallbackQuery):
    caption = (
        "<b>🥗 Бесплатная еда — схема</b>\n\n"
        "<b>Описание от автора:</b>\n"
        "Схема, которая позволяет получать <b>абсолютно бесплатно продукты питания</b>\n"
        "из одного из самых популярных сервисов доставки 🟢.\n\n"
        "📦 <i>Мануал очень качественный</i>, всё расписано по шагам, есть тесты заказов — никаких додумок.\n\n"
        "⚙️ Подходит всем, работает стабильно и эффективно.\n\n"
        "💸 <b>Цена у автора:</b> 6 500₽\n"
        "🔥 <b>Наша цена:</b> 1 875₽"
    )

    photo = FSInputFile("catalog/Abuse/images/abuse_sch_9.jpg")  # Переименуй и положи фото по этому пути

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить за 1875₽", callback_data="pay_abuse_sch_food")],
        [InlineKeyboardButton(text="🎁 Есть промокод", callback_data="promo_abuse_sch_food")],
        [InlineKeyboardButton(text="📤 Поделиться", switch_inline_query="Схема: Бесплатная еда из доставки 🟢. 0₽ за продукты!")],
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
