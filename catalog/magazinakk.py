from aiogram import Router, types
from aiogram.types import FSInputFile

router = Router()

@router.callback_query(lambda c: c.data == "item_accounts")
async def accounts_callback(callback_query: types.CallbackQuery):
    # Фото (обложка для магазина аккаунтов)
    photo = FSInputFile("images/magazinakk.jpg") 

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

    await callback_query.message.answer_photo(
        photo=photo,
        caption=caption,
        parse_mode="HTML"
    )

    await callback_query.answer()
