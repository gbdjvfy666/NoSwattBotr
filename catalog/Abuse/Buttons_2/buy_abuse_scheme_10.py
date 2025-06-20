from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

router = Router()

@router.callback_query(lambda c: c.data == "abuse_sch_pods")
async def abuse_sch_pods_callback(callback_query: types.CallbackQuery):
    caption = (
        "<b>💨 Покупаем поды за 0 рублей</b>\n\n"
        "<b>Описание от автора:</b>\n"
        "Предлагаем <b>максимально подробный мануал</b> по покупке подов за 0₽.\n"
        "Без рисков, без заморочек — <i>разберётся даже ребёнок</i>!\n\n"
        "🔧 <b>Сложность схемы:</b> 2/10\n\n"
        "💸 <b>Цена у автора:</b> 5 900₽\n"
        "🔥 <b>Наша цена:</b> 1 785₽"
    )

    photo = FSInputFile("catalog/Abuse/images/abuse_sch_10.jpg")  # Убедись, что файл есть по пути

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить за 1785₽", callback_data="pay_abuse_sch_pods")],
        [InlineKeyboardButton(text="🎁 Есть промокод", callback_data="promo_abuse_sch_pods")],
        [InlineKeyboardButton(text="📤 Поделиться", switch_inline_query="Схема: Покупаем поды за 0₽. Без рисков и заморочек!")],
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
