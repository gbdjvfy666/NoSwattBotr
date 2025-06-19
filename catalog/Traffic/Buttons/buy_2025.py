from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
import asyncio

router = Router()

@router.callback_query(lambda c: c.data == "buy_2025")
async def buy_2025_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("catalog/Traffic/images/2025.jpg")  
    caption = (
        "🔥 <b>| Измени свой 2025 ($$$)</b>\n\n"
        "Хочешь, чтобы 2025 прошёл как 2024? Тогда ничего не меняй. Но если ты хочешь в 2025 реально зарабатывать, перестать топтаться на месте — начни с того, что работает.\n\n"
        "Измени свой 2025 — это не просто сборник всех связок. Это возможность быстро выйти на новый уровень.\n\n"
        "<b>Что входит?</b>\n"
        "1️⃣ <a href='https://telegra.ph/Do-15-000-v-DEN-na-svyazke-UBT--Telegram-06-08'>До 15 000₽ в ДЕНЬ на связке УБТ + Телеграм</a>\n"
        "2️⃣ <a href='https://telegra.ph/Besplatnaya-reklama-monetizaciya-trafika-06-08'>Бесплатная реклама + монетизация трафика</a>\n"
        "3️⃣ <a href='https://telegra.ph/Monetiziruem-trafik-iz-poiska-tg-06-08'>Монетизируем трафик из поиска tg</a>\n"
        "4️⃣ <a href='https://telegra.ph/Neogranichennaya-pribyl-s-nejropersonazha-06-08'>Неограниченная прибыль с нейроперсонажа</a>\n"
        "5️⃣ <a href='https://telegra.ph/Polnaya-svyazka-UBT-TikTok-Instagram-YouTube-06-08'>Полная связка УБТ: TikTok, Instagram, YouTube</a>\n"
        "6️⃣ <a href='https://telegra.ph/100000r-v-mesyac-s-abuz-kanala-06-08'>100.000₽ в месяц с абуз канала</a>\n"
        "7️⃣ <a href='https://telegra.ph/Poluchaem-dorvejnyj-trafik-iz-poiska-tg-06-08'>Дорвеи из поиска TG</a>\n"
        "8️⃣ <a href='https://telegra.ph/Nejrokommenting--passivnaya-pribyl-06-18'>Нейрокомментинг — пассивная прибыль</a>\n\n"
        "🎁 И всё это — <b>со скидкой -50%</b>\n"
        "⭐️ Отзывы: @otzyvy\n\n"
        "🆓 Помимо скидки, этот пак включает ВСЕ будущие связки 2025 года — <u>бесплатно</u>.\n\n"
        "🔥 <b>Цена сейчас: 15150₽</b>\n"
    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить за 15150₽", callback_data="pay_2025")],
        [InlineKeyboardButton(text="🎁 У меня есть промокод", callback_data="promo_2025")],
        [InlineKeyboardButton(text="📤 Поделиться", switch_inline_query="Измени свой 2025 — @NoSwattBot")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="item_traffic")]
    ])

    # Меняем текущее сообщение с медиа и кнопками
    await callback_query.message.edit_media(
        media=InputMediaPhoto(media=photo, caption=caption, parse_mode="HTML"),
        reply_markup=markup
    )

    await callback_query.answer()
