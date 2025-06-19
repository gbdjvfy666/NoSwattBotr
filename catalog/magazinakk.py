from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.callback_query(lambda c: c.data == "item_accounts")
async def accounts_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("images/magazinakk.jpg")  # Убедись, что путь корректный

    caption = (
        "🏬 <b>Магазин аккаунтов</b> 📦\n\n"
        "➥ <b>Только лучшие аккаунты</b> от проверенных поставщиков.\n"
        "➥ <b>Цены</b> — одни из самых доступных на рынке.\n"
        "➥ <b>Гарантия</b> на каждый аккаунт.\n\n"
        "👥 В наличии:\n"
        "• Соцсети (Instagram, Telegram, TikTok и др.)\n"
        "• Крипто и финтех аккаунты\n"
        "• Стриминг (Netflix, Spotify и др.)\n"
        "• Платформы AI, сервисы подписок, бизнес и многое другое.\n\n"
        "💸 Работай, заливай, запускай — всё готово!"
    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="VPN", callback_data="acc_vpn"),
         InlineKeyboardButton(text="Соц.Сети", callback_data="acc_social")],
        [InlineKeyboardButton(text="Кинотеатры", callback_data="acc_cinema"),
         InlineKeyboardButton(text="Нейросети", callback_data="acc_ai")],
        [InlineKeyboardButton(text="Эл.Почты", callback_data="acc_email"),
         InlineKeyboardButton(text="Файлообменник", callback_data="acc_files")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_shop")]
    ])

    await callback_query.message.answer_photo(
        photo=photo,
        caption=caption,
        parse_mode="HTML",
        reply_markup=markup
    )

    await callback_query.answer()
