from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

router = Router()

@router.callback_query(lambda c: c.data == "abuse_sch_fortnite")
async def abuse_sch_fortnite_callback(callback_query: types.CallbackQuery):
    caption = (
        "<b>🎮 Абуз Fortnite — 1.500₽/круг</b>\n\n"
        "Если ты считаешь, что <i>работа мечты</i> не существует — ты сильно ошибаешься.\n"
        "С этой схемой ты зарабатываешь просто перепродавая аккаунты Fortnite между площадками.\n"
        "📦 Купить дешево — продать дорого. Всё гениальное просто.\n\n"
        "⚙️ <b>Характеристики:</b>\n"
        "💰 Заработок: <b>1.500₽</b> за круг\n"
        "💸 Вложения: ~150₽ (на аккаунт)\n"
        "⚪️ Цвет: белый\n"
        "⛰ Гео: не важно\n"
        "🤼‍♀️ Конкуренция: низкая\n\n"
        "<b>Описание от автора:</b>\n"
        "• Покупаем аккаунт на одном сервисе\n"
        "• Делаем простые действия внутри\n"
        "• Продаём в 5–10 раз дороже на другой площадке\n"
        "• Живёт ещё минимум месяц\n"
        "• Автор лично делает 2–5к в день, при желании — 10–20к\n"
        "• Есть <b>гарант до профита</b>, схема <b>не в паблике</b>\n\n"
        "💸 <b>Цена у автора:</b> 11 500₽\n"
        "🔥 <b>Наша цена:</b> 1 717.5₽"
    )

    photo = FSInputFile("catalog/Abuse/images/abuse_sch_8.jpg")  # Проверь, что файл существует

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить за 1717.5₽", callback_data="pay_abuse_sch_fortnite")],
        [InlineKeyboardButton(text="🎁 Есть промокод", callback_data="promo_abuse_sch_fortnite")],
        [InlineKeyboardButton(text="📤 Поделиться", switch_inline_query="Абуз Fortnite — 1500₽/круг. Покупай дёшево — продавай дорого!")],
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
