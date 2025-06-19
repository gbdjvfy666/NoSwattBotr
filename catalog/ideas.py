from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.callback_query(lambda c: c.data == "item_ideas")
async def ideas_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("images/Bidea.jpg")  # Убедись, что файл существует

    caption = (
        "✨ <b>Бизнес идеи</b>\n\n"
        "➥ В данном разделе находятся лучшие бизнес идеи, с помощью которых уже в ближайшие дни каждый из вас сможет стать предпринимателем, "
        "главное — придерживаться инструкции и верить в себя.\n\n"
        "💰 Бизнес идеи только по самым доступным ценам!"
    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Пак 50 товаров для перепродажи • 2250₽", callback_data="idea_pack_50")],
        [InlineKeyboardButton(text="До 900₽ за 5 минут на продаже онлайн товара • 2250₽", callback_data="idea_online_900")],
        [InlineKeyboardButton(text="Прибыльный офлайн бизнес • 2250₽", callback_data="idea_offline")],
        [InlineKeyboardButton(text="6000₽ в день на создании и продаже Тг ботов • 5600₽", callback_data="idea_tg_bots")],
        [InlineKeyboardButton(text="Серо-белый бизнес(годнота) • 3800₽", callback_data="idea_gray")],
        [InlineKeyboardButton(text="От 2.000₽ в день на развитии Тг Каналов! • 1990₽", callback_data="idea_channels")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_catalog")]
    ])

    await callback_query.message.answer_photo(
        photo=photo,
        caption=caption,
        reply_markup=markup,
        parse_mode="HTML"
    )

    await callback_query.answer()
