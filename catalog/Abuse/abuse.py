from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton
from .best_abuse import router as buy_best_abuse_router
from .best_abuse import router as buy_best_abuse_router
from .buy_abuse_schemes import router as buy_abuse_schemes_router

router = Router()
router.include_router(buy_best_abuse_router)
router.include_router(buy_abuse_schemes_router)

@router.callback_query(lambda c: c.data == "item_abuse")
async def abuse_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("images/abuse.jpg") 

    caption = (
        "⚡️ <b>Абузы</b>\n\n"
        "➥ <b>Абуз</b> — это злоупотребление плюшками, которые предлагают различные платформы.\n"
        "Это может быть участие в акции, регистрация по реферальной ссылке, выполнение заданий и другое.\n\n"
        "💬 <i>От себя добавим:</i> абуз — один из самых <b>лёгких</b> и <b>эффективных</b> способов быстро заработать.\n\n"
        "🔍 <b>Часто задаваемый вопрос:</b> «<i>Почему так дёшево?</i>»\n\n"
        "✅ Мы покупаем схемы у авторов и перепродаём их по низкой цене, делая ставку на массовость. "
        "Таким образом окупаем затраты и зарабатываем.\n\n"
        "🔥 Готовые схемы ждут тебя. Успей первым!"
    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💥 Лучшие Абузы", callback_data="buy_best_abuse")],
        [InlineKeyboardButton(text="📜 Схемы Абуза", callback_data="buy_abuse_schemes")],
        [InlineKeyboardButton(text="💸 Дешевые Абузы", callback_data="buy_cheap_abuse")],
        [InlineKeyboardButton(text="📦 Паки Абузов", callback_data="buy_abuse_packs")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_catalog")]
    ])

    await callback_query.message.answer_photo(
        photo=photo,
        caption=caption,
        parse_mode="HTML",
        reply_markup=markup
    )
    await callback_query.answer()
