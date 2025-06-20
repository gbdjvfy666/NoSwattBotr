from aiogram import Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
from .Buttons_2.buy_abuse_scheme_1 import router as abuse_sch_1_router
from .Buttons_2.buy_abuse_scheme_2 import router as abuse_sch_2_router
from .Buttons_2.buy_abuse_scheme_3 import router as abuse_sch_3_router
from .Buttons_2.buy_abuse_scheme_4 import router as abuse_sch_4_router
from .Buttons_2.buy_abuse_scheme_5 import router as abuse_sch_5_router
from .Buttons_2.buy_abuse_scheme_6 import router as abuse_sch_6_router
from .Buttons_2.buy_abuse_scheme_7 import router as abuse_sch_7_router
from .Buttons_2.buy_abuse_scheme_8 import router as abuse_sch_8_router
from .Buttons_2.buy_abuse_scheme_9 import router as abuse_sch_9_router
from .Buttons_2.buy_abuse_scheme_10 import router as abuse_sch_10_router
from .Buttons_2.buy_abuse_scheme_11 import router as abuse_sch_11_router


router = Router()

router.include_router(abuse_sch_11_router)
router.include_router(abuse_sch_10_router)
router.include_router(abuse_sch_9_router)
router.include_router(abuse_sch_8_router)
router.include_router(abuse_sch_7_router)
router.include_router(abuse_sch_6_router)
router.include_router(abuse_sch_5_router)
router.include_router(abuse_sch_4_router)
router.include_router(abuse_sch_3_router)
router.include_router(abuse_sch_2_router)
router.include_router(abuse_sch_1_router)
@router.callback_query(lambda c: c.data == "buy_abuse_schemes")
async def abuse_schemes_callback(callback_query: types.CallbackQuery):
    caption = (
        "⚡️ <b>Абузы</b> › 🍉 <b>Схемы Абуза</b> 🍉\n\n"
        "➥ <b>Дорогостоящие абузы</b>, абсолютно на любой вкус и любого цвета — по самым <b>доступным ценам</b>!"
    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🍇 Очень жирный абуз Wildberries • 1687.5₽", callback_data="abuse_sch_1")],
        [InlineKeyboardButton(text="📞 Абуз партнёрки на звонках • 2092.5₽", callback_data="abuse_sch_2")],
        [InlineKeyboardButton(text="🚕 Бесплатная Янд3кс.Такси / UBER • 1950.5₽", callback_data="abuse_sch_3")],
        [InlineKeyboardButton(text="💻 Возврат денег за технику • 2212.5₽", callback_data="abuse_sch_4")],
        [InlineKeyboardButton(text="📦 Абуз ПП 2.000₽/круг • 1950₽", callback_data="abuse_sch_5")],
        [InlineKeyboardButton(text="💰 25–65% к депозиту с круга • 2002.5₽", callback_data="abuse_sch_6")],
        [InlineKeyboardButton(text="🤖 Абуз ChatGPT-4 — 800₽/30 мин • 1650₽", callback_data="abuse_sch_7")],
        [InlineKeyboardButton(text="🎮 Абуз Fortnite — 1.500₽/круг • 1717.5₽", callback_data="abuse_sch_8")],
        [InlineKeyboardButton(text="🍔 Бесплатная еда • 1875₽", callback_data="abuse_sch_9")],
        [InlineKeyboardButton(text="💨 Поды за 0 рублей • 1785₽", callback_data="abuse_sch_10")],
        [InlineKeyboardButton(text="💸 10K/ДЕНЬ на АБУЗЕ СКИДОК • 1875₽", callback_data="abuse_sch_11")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="item_abuse")]
    ])

    await callback_query.message.answer_photo(
        caption=caption,
        parse_mode="HTML",
        reply_markup=markup
    )

    await callback_query.answer()
