from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

router = Router()

@router.callback_query(lambda c: c.data == "buy_dorway")
async def buy_dorway_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("catalog/Traffic/images/dorway.jpg")  # проверь путь к картинке

    caption = (
        "<b>📖| Получаем дорвейный трафик из поиска TG</b>\n\n"
        "Один из самых жирных видов трафика на данный момент — удачно выбранный запрос может обеспечить вас пассивной прибылью при минимальных вложениях.\n\n"
        "Представьте: подбираете удачное название бота, выполняете несколько простых действий — и получаете постоянный пассивный источник дохода. При удачном запросе это сотни тысяч рублей ежемесячно.\n\n"
        "В мануале рассказывается:\n"
        "✅ Как выводить телеграм-ботов в поиск\n"
        "✅ Какую панель услуг использовать\n"
        "✅ 4 способа монетизации (2 — полностью пассивных)\n\n"
        "🎁 Получите ссылку на панель, владельцы которой всегда пишут обновления при изменении алгоритмов поиска — актуализация материала навсегда.\n\n"
        "✅ Вложения минимум от 5000₽\n"
        "✅ Для работы достаточно смартфона\n"
        "✅ Всё разжёвано — справится даже новичок\n"
        "✅ Отлично для пассивной прибыли\n"
        "✅ Сверхвысокая прибыль\n\n"
        "⭐️ Отзывы: @otzyvy\n\n"
        "<b>ВКРАТЦЕ:</b>\n"
        "💰 Заработок: колоссально огромный\n"
        "⚪️ Цвет: белый\n"
        "⏳ Срок жизни: неограничен\n"
        "⛰ Гео: не важно\n"
        "🤼‍♀️ Конкуренция: зависит от поиска\n\n"
        "<b>Цена у нас — 2998.5₽</b>"
    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить за 2998.5₽", callback_data="pay_dorway")],
        [InlineKeyboardButton(text="🎁 Есть промокод", callback_data="promo_dorway")],
        [InlineKeyboardButton(text="📤 Поделиться", switch_inline_query="Дорвейный трафик из поиска TG")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="item_traffic")]
    ])

    await callback_query.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=caption, parse_mode="HTML"),
        reply_markup=markup
    )

    await callback_query.answer()
