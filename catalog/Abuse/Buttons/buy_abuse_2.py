from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

router = Router()

@router.callback_query(lambda c: c.data == "abuse_2")
async def abuse_2_callback(callback_query: types.CallbackQuery):
    caption = (
        "<b>🎰 Абуз UP-X (не тот слитый)</b>\n\n"
        "<b>ВАЖНО:</b> вы получаете <u>не тот абуз</u>, который слили пару месяцев назад. "
        "Это <b>свежий и годный</b> абуз, который ещё долго будет актуален. "
        "<b>Вам не нужен большой депозит!</b>\n\n"
        "Что вы получаете при покупке:\n"
        "1️⃣ Личную стратегию для абуза.\n"
        "2️⃣ Информацию по отыгрышу бонусного баланса.\n"
        "3️⃣ Полноценный вывод средств без блокировки аккаунта, а также возможность увеличения объемов в работе.\n\n"
        "💸 <b>Цена у автора:</b> 13 300₽\n"
        "🔥 <b>Цена у нас:</b> 2 550₽"
    )

    photo = FSInputFile("catalog/Abuse/images/abuse_2.jpg")  # Убедись, что файл существует

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить за 2550₽", callback_data="pay_abuse_2")],
        [InlineKeyboardButton(text="🎁 Есть промокод", callback_data="promo_abuse_2")],
        [InlineKeyboardButton(text="📤 Поделиться", switch_inline_query="Абуз UP-X (не тот слитый)")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="buy_best_abuse")]
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
