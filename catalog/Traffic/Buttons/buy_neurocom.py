from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

router = Router()

@router.callback_query(lambda c: c.data == "buy_neurocom")
async def buy_neurocom_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("catalog/Traffic/images/neurocom.jpg")  # Убедись, что путь корректный

    caption = (
        "<b>📹 | Нейрокомментинг — пассивная прибыль</b>\n\n"
        "🧠 Нейронки развиваются очень быстро и Telegram они тоже не обошли стороной. Благодаря нейрокомментингу и дополнительному способу, "
        "можно привлекать сотни подписчиков в месяц на свои проекты, тратя в разы меньше и получая больше трафика, чем при закупе рекламы.\n\n"
        "🔧 И главное — нужно один раз всё настроить, нажать кнопку и трафик пойдёт на пассиве.\n\n"
        "✅ <b>В обучении вы узнаете:</b>\n"
        "1. Как работать с нейрокомментингом\n"
        "2. Как его настроить\n"
        "3. Оптимальные лимиты\n"
        "4. Как привлекать больше трафика\n"
        "5. Всё о расходниках — аккаунты, прокси и где их брать\n"
        "6. Как оформить аккаунты, переходники и канал\n"
        "7. Как правильно привлекать аудиторию\n"
        "8. Дополнительный способ привлечения с помощью чужих рук\n\n"
        "🎁 <b>Бонус:</b> как с малыми вложениями привлекать трафик через буксы.\n\n"
        "📱 Можно работать с телефона и ПК\n"
        "📹 Подробное пошаговое видео\n"
        "💸 Поможет выстроить пассивный доход и трафик\n"
        "🧩 Простая реализация\n\n"
        "⭐️ Отзывы: @otzyvy\n\n"
        "<b>ВКРАТЦЕ:</b>\n"
        "💰 Заработок: неограничен\n"
        "⚪️ Цвет: белый\n"
        "⏳ Срок жизни: бессрочно\n"
        "⛰ Гео: СНГ\n"
        "🤼‍♀️ Конкуренция: неважна\n\n"
        "<b>Цена у нас — 4348.5₽</b>"
    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить за 4348.5₽", callback_data="pay_neurocom")],
        [InlineKeyboardButton(text="🎁 Есть промокод", callback_data="promo_neurocom")],
        [InlineKeyboardButton(text="📤 Поделиться", switch_inline_query="Нейрокомментинг")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="item_traffic")]
    ])

    await callback_query.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=caption, parse_mode="HTML"),
        reply_markup=markup
    )

    await callback_query.answer()
