from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.callback_query(lambda c: c.data == "buy_freeads")
async def buy_freeads_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("catalog/Traffic/images/freeads.jpg")  # замени на правильный путь к картинке

    caption = (
        "<b>📖 | Бесплатная реклама + монетизация трафика</b>\n\n"
        "Авторский УБТ мануал в виде закрытого канала, который научит зарабатывать на партнёрке и получать рекламу в различных Telegram-каналах абсолютно <b>БЕСПЛАТНО</b>.\n\n"
        "✨ Отлично подойдёт новичкам и даст ценные знания опытным. Мастхэв для тех, кто хочет результат — без вложений.\n\n"
        "🎁 <b>Обучение по монетизации трафика:</b> как получать трафик и монетизировать его буквально в те же минуты!\n"
        "Курс рассчитан на тех, кто <i>действительно</i> готов работать ради реальной выгоды.\n\n"
        "✅ Без вложений на рекламу\n"
        "✅ Работает даже с телефона\n"
        "✅ Всё разжёвано — справится каждый\n"
        "✅ Прокачивает навык общения\n"
        "✅ Долгосрочная схема — будет работать всегда\n\n"
        "⭐️ Отзывы: @otzyvy\n\n"
        "<b>ВКРАТЦЕ:</b>\n"
        "💰 Заработок: неограничен\n"
        "⚪️ Цвет: белый\n"
        "⏳ Срок жизни: неограничен\n"
        "⛰ Гео: не важно\n"
        "🤼‍♀️ Конкуренция: её нет\n\n"
        "<b>Цена у нас — 4050₽</b>"
    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить за 4050₽", callback_data="pay_freeads")],
        [InlineKeyboardButton(text="🎁 Есть промокод", callback_data="promo_freeads")],
        [InlineKeyboardButton(text="📤 Поделиться", switch_inline_query="Бесплатная реклама + монетизация трафика")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="item_traffic")]
    ])

    await callback_query.message.answer_photo(
        photo=photo,
        caption=caption,
        reply_markup=markup,
        parse_mode="HTML"
    )

    await callback_query.answer()
