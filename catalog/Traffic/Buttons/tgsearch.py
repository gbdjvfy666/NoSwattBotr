from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

router = Router()

@router.callback_query(lambda c: c.data == "buy_tgsearch")
async def buy_tgsearch_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("catalog/Traffic/images/tgsearch.jpg")  # проверь путь к файлу

    caption = (
        "<b>📖| Монетизируем трафик из поиска TG</b>\n\n"
        "Материал от одного из топовых арбитражников, который обеспечил себе пассивную прибыль, поставив несколько ботов в поиск и получая с этого автоматическую монетизацию.\n\n"
        "Схема по выводу бота в поиск Telegram:\n"
        "👆 Создаёшь бота → выполняешь действия по схеме → получаешь пассивный трафик на свой оффер.\n\n"
        "Подробно описано два метода:\n"
        "✅ быстрый — за пару дней\n"
        "✅ долгий — за 5 дней\n\n"
        "Какой использовать — решать тебе.\n\n"
        "Плюс узнаешь про мега-крутой оффер для полной пассивной монетизации, от тебя требуется только поставить бота в нужный запрос.\n\n"
        "Схема подходит для вывода в абсолютно любой запрос поиска Telegram.\n\n"
        "✅ Вложения минимум от 2000₽\n"
        "✅ Достаточно смартфона\n"
        "✅ Всё пошагово — справится даже новичок\n"
        "✅ Полностью пассивная прибыль\n"
        "✅ Множество вариантов масштабировать\n\n"
        "⭐️ Отзывы: @otzyvy\n\n"
        "<b>ВКРАТЦЕ:</b>\n"
        "💰 Заработок: неограничен\n"
        "⚪️ Цвет: белый\n"
        "⏳ Срок жизни: неограничен\n"
        "⛰ Гео: не важно\n"
        "🤼‍♀️ Конкуренция: зависит от запроса\n\n"
        "<b>Цена у нас — 3750₽</b>"
    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить за 3750₽", callback_data="pay_tgsearch")],
        [InlineKeyboardButton(text="🎁 Есть промокод", callback_data="promo_tgsearch")],
        [InlineKeyboardButton(text="📤 Поделиться", switch_inline_query="Монетизируем трафик из поиска TG")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="item_traffic")]
    ])

    await callback_query.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=caption, parse_mode="HTML"),
        reply_markup=markup
    )

    await callback_query.answer()
