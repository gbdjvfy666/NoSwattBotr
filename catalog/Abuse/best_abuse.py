from aiogram import Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .Buttons.buy_abuse_1 import router as abuse_1_router
from .Buttons.buy_abuse_2 import router as abuse_2_router
from .Buttons.buy_abuse_3 import router as abuse_3_router

router = Router()

router.include_router(abuse_3_router)
router.include_router(abuse_2_router)
router.include_router(abuse_1_router)
@router.callback_query(lambda c: c.data == "buy_best_abuse")
async def best_abuse_callback(callback_query: types.CallbackQuery):
    caption = (
        "⚡️ <b>Абузы</b>  ›  👑 <b>Лучшие Абузы</b> 👑\n\n"
        "➥ Самые <b>лучшие абузы</b>, с <b>топовыми профитами</b> и <b>лёгкой реализацией</b>."
    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💰 Абуз партнёрки 30к/круг • 2362.5₽", callback_data="abuse_1")],
        [InlineKeyboardButton(text="🎰 Абуз UP-X (не тот слитый) • 2550₽", callback_data="abuse_2")],
        [InlineKeyboardButton(text="📈 Абуз ПП — 320 руб/круг • 1950₽", callback_data="abuse_3")],
        [InlineKeyboardButton(text="📦 Абуз Ozon — бесплатные товары • 2512.5₽", callback_data="abuse_4")],
        [InlineKeyboardButton(text="🎯 Бонусхантинг до 6.000₽/круг • 2145₽", callback_data="abuse_5")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="item_abuse")]
    ])

    await callback_query.message.edit_caption(
        caption=caption,
        reply_markup=markup,
        parse_mode="HTML"
    )

    await callback_query.answer()
