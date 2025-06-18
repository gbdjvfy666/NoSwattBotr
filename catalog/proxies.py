from aiogram import Router, types

router = Router()

@router.callback_query(lambda c: c.data == "item_proxies")
async def proxies_callback(callback_query: types.CallbackQuery):
    caption = (
        "💎 Прокси\n\n"
        "❗️Мы не предоставляем прокси под черные цели! Вы несете полную ответственность за свои действия! "
        "»подробнее« (https://telegra.ph/Pravila-soglasheniya-i-politika-08-06)\n\n"
        "Выберите тип прокси:"
    )

    await callback_query.message.answer(
        text=caption,
        parse_mode="HTML"
    )

    await callback_query.answer()
