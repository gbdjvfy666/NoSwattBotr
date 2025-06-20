from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

router = Router()

@router.callback_query(lambda c: c.data == "abuse_sch_chatgpt4")
async def abuse_sch_chatgpt4_callback(callback_query: types.CallbackQuery):
    caption = (
        "<b>🤖 Абуз ChatGPT-4 — от 800₽ за 30 минут</b>\n\n"
        "<b>Держите мощную и свежую связку</b> по абузу GPT-4, с профитом от <b>800₽</b> за 1 круг (всего ~30 минут работы).\n\n"
        "⚙️ <b>Характеристики:</b>\n"
        "💰 Заработок: <b>от 800₽</b> за круг\n"
        "⏱️ Время: ~30 минут\n"
        "♾️ Кругов: <b>неограниченно</b>\n"
        "⚪️ Цвет: белый\n"
        "💸 Вложения: ~1800₽ за круг\n"
        "⏳ Срок жизни схемы: ~1 месяц\n"
        "🌍 Гео: не важно\n"
        "🧘‍♂️ Конкуренция: отсутствует\n\n"
        "🔥 <i>Очень актуальный абуз, почти никто о нём не знает.</i>\n"
        "📌 <b>Рекомендуем запускать прямо сейчас — пока работает!</b>\n\n"
        "💸 <b>Цена у автора:</b> 18 000₽\n"
        "🔥 <b>Наша цена:</b> 1 650₽"
    )

    photo = FSInputFile("catalog/Abuse/images/abuse_sch_7.jpg")

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить за 1650₽", callback_data="pay_abuse_sch_chatgpt4")],
        [InlineKeyboardButton(text="🎁 Есть промокод", callback_data="promo_abuse_sch_chatgpt4")],
        [InlineKeyboardButton(text="📤 Поделиться", switch_inline_query="Абуз ChatGPT-4 — от 800₽ за 30 минут")],
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
