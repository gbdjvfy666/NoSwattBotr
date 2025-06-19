from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

router = Router()

@router.callback_query(lambda c: c.data == "buy_neuromontage")
async def buy_neuromontage_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("catalog/Traffic/images/neuromontage.jpg")  # проверь путь к картинке

    caption = (
        "<b>📹| Неограниченная прибыль с нейроперсонажа</b>\n\n"
        "Уже видели, как нейроперсонажи взрывают рекомендации и собирают миллионы просмотров? В этом пошаговом обучении вы узнаете, как зарабатывать на нейроперсонажах — всё просто:\n\n"
        "✅ Создаёте по инструкции своего героя\n"
        "✅ Заливаете ролики с ним\n"
        "✅ Подключаете топовый оффер под связку\n"
        "✅ Получаете пассивную прибыль\n\n"
        "<b>В обучении вам расскажут:</b>\n"
        "1. Как работать с TikTok, Reels, Shorts\n"
        "2. С какими площадками стоит работать\n"
        "3. Как регистрировать аккаунты\n"
        "4. Как оформлять каналы\n"
        "5. Правильный прогрев\n"
        "6. Работа с антидетект браузером\n"
        "7. Как выкладывать ролики\n"
        "8. Куда вставлять ссылку\n"
        "9. Базовый монтаж роликов + фишки\n"
        "10. Работа с нейросетями и создание персонажа\n"
        "11. Какой контент срабатывает лучше\n"
        "12. Поиск идей для роликов\n"
        "13. Монетизация трафика и выбор оффера\n\n"
        "Максимально подробное пошаговое обучение, подойдёт новичкам и бывалым. Направлено на прямой пролив под оффер с УБТ площадок. Заработок не ограничен — всё зависит от вашей активности.\n\n"
        "✅ Вложения от 1000₽\n"
        "✅ Можно работать с телефона и ПК\n"
        "✅ Очень подробное пошаговое видео\n"
        "✅ Поможет построить пассивный доход\n"
        "✅ Очень лёгкая реализация\n\n"
        "⭐️ Отзывы: @otzyvy\n\n"
        "<b>ВКРАТЦЕ:</b>\n"
        "💰 Заработок: неограничен\n"
        "⚪️ Цвет: белый\n"
        "⏳ Срок жизни: неограничен\n"
        "⛰ Гео: не важно\n"
        "🤼‍♀️ Конкуренция: неважна\n\n"
        "<b>Цена у нас — 3675₽</b>"
    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить за 3675₽", callback_data="pay_neuromontage")],
        [InlineKeyboardButton(text="🎁 Есть промокод", callback_data="promo_neuromontage")],
        [InlineKeyboardButton(text="📤 Поделиться", switch_inline_query="Нейроперсонажи")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="item_traffic")]
    ])

    await callback_query.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=caption, parse_mode="HTML"),
        reply_markup=markup
    )

    await callback_query.answer()
