from aiogram import Router, types

router = Router()

@router.callback_query(lambda c: c.data == "item_sms")
async def sms_callback(callback_query: types.CallbackQuery):
    caption = (
        "☎️ Выбор сервиса\n\n"
        "Выберите необходимый сервис:"
    )

    await callback_query.message.answer(

        text=caption,
        parse_mode="HTML"
    )

    await callback_query.answer()
