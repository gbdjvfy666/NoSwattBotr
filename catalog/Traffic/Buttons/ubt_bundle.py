from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

router = Router()

@router.callback_query(lambda c: c.data == "buy_ubt_bundle")
async def buy_ubt_bundle_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("catalog/Traffic/images/ubt_bundle.jpg")  # проверь путь к картинке

    caption = (
        "<b>📹| Полная связка УБТ: TikTok, Instagram, YouTube</b>\n\n"
        "Подробнейший видео мануал по работе с УБТ трафиком и его монетизации через специальные офферы и собственный телеграм канал.\n\n"
        "Обучение в видеоформате от топового арбитражника, который с помощью этих знаний сделал более ₽1 млн оборота за короткий промежуток времени.\n\n"
        "🔥 В видео мануале вас ждёт:\n"
        "● Правильная регистрация и прогрев аккаунтов\n"
        "● Разбор связки №1 + 3 варианта залива\n"
        "● Разбор связки №2 + 2 варианта залива\n"
        "● Разбор залива собственного телеграм канала + 3 способа перелива\n"
        "● Советы по правильной структуре роликов\n"
        "● Обходы теневых банов\n"
        "● Экскурс по топовой партнёрке + подключение\n"
        "● Создание и ведение телеграм канала с монетизацией — всё пошагово\n"
        "● Дополнительная монетизация полностью пассивным способом\n"
        "● Готовые видео-обучения по монтажу коротких роликов\n\n"
        "✅ Вложения не нужны — всё работает без них\n"
        "✅ Для работы достаточно смартфона\n"
        "✅ Всё разжёвано — справится новичок\n"
        "✅ Очень годный материал\n"
        "✅ Много способов пассивного заработка\n\n"
        "⭐️ Отзывы: @otzyvy\n\n"
        "<b>ВКРАТЦЕ:</b>\n"
        "💰 Заработок: сверх высокий\n"
        "⚪️ Цвет: белый\n"
        "⏳ Срок жизни: неограничен\n"
        "⛰ Гео: не важно\n"
        "🤼‍♀️ Конкуренция: не важна\n\n"
        "<b>Цена у нас — 3598.5₽</b>"
    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить за 3598.5₽", callback_data="pay_ubt_bundle")],
        [InlineKeyboardButton(text="🎁 Есть промокод", callback_data="promo_ubt_bundle")],
        [InlineKeyboardButton(text="📤 Поделиться", switch_inline_query="Полная связка УБТ")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="item_traffic")]
    ])

    await callback_query.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=caption, parse_mode="HTML"),
        reply_markup=markup
    )

    await callback_query.answer()
