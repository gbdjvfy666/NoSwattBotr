from aiogram import Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile

# Импорты обработчиков для карточек товаров
from .Buttons.buy_2025 import router as buy_2025_router
from .Buttons.buy_ubt_tg import router as buy_ubt_tg_router
from .Buttons.buy_neurocom import router as buy_neurocom_router
from .Buttons.freeads import router as buy_freeads_router
from .Buttons.tgsearch import router as buy_tgsearch_router
from .Buttons.neuromontage import router as buy_neuromontage_router
from .Buttons.ubt_bundle import router as buy_ubt_bundle_router
from .Buttons.abuse_channel import router as buy_abuse_router
from .Buttons.dorway import router as buy_dorway_router

router = Router()


router.include_router(buy_2025_router)
router.include_router(buy_ubt_tg_router)
router.include_router(buy_neurocom_router)
router.include_router(buy_freeads_router)
router.include_router(buy_tgsearch_router)
router.include_router(buy_neuromontage_router)
router.include_router(buy_ubt_bundle_router)
router.include_router(buy_abuse_router)
router.include_router(buy_dorway_router)

@router.callback_query(lambda c: c.data == "item_traffic")
async def traffic_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("images/traffic_cover.jpg")

    caption = (
        "🔥 <b>Деньги на Трафике</b> 🔥\n\n"
        "Исключительно рабочие материалы, написанные топовыми арбитражниками, УБТшниками и SEOшниками.\n"
        "Каждый материал — это пошаговый путь от нуля до профита, которым авторы реально зарабатывают сейчас.\n\n"
        "<b>Форматы обучения:</b>\n"
        "📖 — текст\n"
        "📹 — видео\n"
        "💻 — комбо\n\n"
        "Выбери товар ниже и начни прямо сейчас 👇"
    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💸 | Измени свой 2025 ($$$) • 15150₽", callback_data="buy_2025")],
        [InlineKeyboardButton(text="🚀 | До 15 000₽ в День на связке УБТ + Телеграм • 4989.5₽", callback_data="buy_ubt_tg")],
        [InlineKeyboardButton(text="🧠 | Нейрокомментинг — пассивная прибыль • 4320.5₽", callback_data="buy_neurocom")],
        [InlineKeyboardButton(text="🎯 | Бесплатная реклама + монетизация трафика • 4050₽", callback_data="buy_freeads")],
        [InlineKeyboardButton(text="🔎 | Монетизируем трафик из поиска TG • 3750₽", callback_data="buy_tgsearch")],
        [InlineKeyboardButton(text="🎥 | Неограниченная прибыль с нейромантажа • 3675₽", callback_data="buy_neuromontage")],
        [InlineKeyboardButton(text="📲 | Полная связка УБТ: TikTok, Instagram, YouTube • 3598.5₽", callback_data="buy_ubt_bundle")],
        [InlineKeyboardButton(text="📈 | 100.000р в месяц с абуз канала • 3150₽", callback_data="buy_abuse")],
        [InlineKeyboardButton(text="🌐 | Получаем дорвейный трафик из поиска TG • 2998.5₽", callback_data="buy_dorway")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_catalog")]
    ])

    await callback_query.message.answer_photo(
        photo=photo,
        caption=caption,
        reply_markup=markup,
        parse_mode="HTML"
    )

    await callback_query.answer()
