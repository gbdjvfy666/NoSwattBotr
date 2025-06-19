from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

router = Router()

@router.callback_query(lambda c: c.data == "buy_abuse")
async def buy_abuse_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("catalog/Traffic/images/abuse_channel.jpg")  # проверь путь к картинке

    caption = (
        "<b>📖| 100.000р в месяц с абуз канала</b>\n\n"
        "Сам автор зарабатывает в неделю от 30 до 50 тысяч рублей с 1 топового оффера — не считая дохода с продажи рекламы. "
        "В этом авторском мануале он подробно объяснит, как закупать рекламу в Телеграм выгодно, а также раскроет тонкости, "
        "например, как получать доход в 2 раза больше при тех же вложениях, что и у конкурентов (иногда не совсем честными методами).\n\n"
        "Вы узнаете:\n"
        "✅ Оценку трафика\n"
        "✅ Увеличение конверсий на любой оффер\n"
        "✅ Доступ ко всем инструментам для ведения канала\n"
        "✅ Готовую топовую связку для монетизации с примером воронки\n"
        "✅ Наставления для новичков и опытных админов\n\n"
        "После покупки вы попадёте в закрытый канал с информацией для быстрого старта.\n\n"
        "💸 Стартовые вложения от 50$\n"
        "📱 Достаточно смартфона\n"
        "📖 Подробные пошаговые инструкции\n"
        "🚀 Поможет увеличить прибыль\n"
        "🔄 Будет работать всегда\n\n"
        "⭐️ Отзывы: @otzyvy\n\n"
        "<b>ВКРАТЦЕ:</b>\n"
        "💰 Заработок: неограничен\n"
        "⚪️ Цвет: белый\n"
        "⏳ Срок жизни: неограничен\n"
        "⛰ Гео: не важно\n"
        "🤼‍♀️ Конкуренция: минимальна\n\n"
        "<b>Цена у нас — 3150₽</b>"
    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить за 3150₽", callback_data="pay_abuse")],
        [InlineKeyboardButton(text="🎁 Есть промокод", callback_data="promo_abuse")],
        [InlineKeyboardButton(text="📤 Поделиться", switch_inline_query="100.000р в месяц с абуз канала")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="item_traffic")]
    ])

    await callback_query.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=caption, parse_mode="HTML"),
        reply_markup=markup
    )

    await callback_query.answer()
