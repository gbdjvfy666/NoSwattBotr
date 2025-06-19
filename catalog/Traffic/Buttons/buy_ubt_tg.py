from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

router = Router()

@router.callback_query(lambda c: c.data == "buy_ubt_tg")
async def buy_ubt_tg_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("catalog/Traffic/images/before_15k.jpg")  # Убедись, что файл существует

    caption = (
        "<b>📹 | До 15 000₽ в ДЕНЬ на связке УБТ + Телеграм</b>\n\n"
        "Специально для вас, топовый трафер, целый месяц записывал обучение по связке, на которой сам поднял 660к₽.\n\n"
        "✅ После покупки вы получите:\n"
        "• 20-минутный ролик\n"
        "• Материалы и инструкции\n"
        "• Готовый онлайн-бизнес почти под ключ\n\n"
        "⚙️ Обучение включает:\n"
        "• Создание УБТ-акков\n"
        "• Контент и оформление\n"
        "• Монетизация Telegram\n"
        "• Рост прибыли и воронка\n\n"
        "🎁 В подарок — доступ к курсу по крео, монтажу и бонусные связки.\n\n"
        "⭐️ Отзывы: @otzyvy\n\n"
        "<b>Цена: 4948.5₽</b>\n"
    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить за 4948.5₽", callback_data="pay_ubt_tg")],
        [InlineKeyboardButton(text="🎁 Ввести промокод", callback_data="promo_ubt_tg")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="item_traffic")]
    ])

    await callback_query.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=caption, parse_mode="HTML"),
        reply_markup=markup
    )

    await callback_query.answer()
