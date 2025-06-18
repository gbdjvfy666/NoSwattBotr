from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile

router = Router()

@router.message(F.text == "🏪 Каталог товаров")
async def show_shop_from_text(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔥 Деньги на трафике  🔥", callback_data="item_traffic")],
        [InlineKeyboardButton(text="📂 Абузы", callback_data="item_abuse"),
         InlineKeyboardButton(text="🗃 Архивы", callback_data="item_archives")],
        [InlineKeyboardButton(text="👤 Магазин аккаунтов", callback_data="item_accounts")],
        [InlineKeyboardButton(text="🏪 Готовый бизнес", callback_data="item_business")],
        [InlineKeyboardButton(text="🎓 схемы", callback_data="item_shema"),
         InlineKeyboardButton(text="🎓 Обучение", callback_data="item_edu")],
        [InlineKeyboardButton(text="🎟 Лотерея", callback_data="item_lottery"),
         InlineKeyboardButton(text="❤️ Здоровье", callback_data="item_health")],
        [InlineKeyboardButton(text="💼 Кошельки с балансом", callback_data="item_wallets")],
        [InlineKeyboardButton(text="🌐 Прокси", callback_data="item_proxies"),
         InlineKeyboardButton(text="📲 СМС", callback_data="item_sms")],
        [InlineKeyboardButton(text="📲 ЧЕКИ 💸⛓️🗄", callback_data="item_checks"),
         InlineKeyboardButton(text="💵 Сид-фразы", callback_data="item_seed")],
        [InlineKeyboardButton(text="🚀 Бизнес-идеи", callback_data="item_ideas"),
         InlineKeyboardButton(text="💻 Скрипты", callback_data="item_scripts")],
        [InlineKeyboardButton(text="🎫 Последний билет", callback_data="item_lastticket")]
    ])

    # Путь к изображению (можно и URL, если файл загружен в интернет)
    photo = FSInputFile("images/ourgoods.jpg")  # Убедись, что файл существует

    await message.answer_photo(
        photo=photo,
        caption="📦 <b>Каталог товаров:</b>",
        reply_markup=markup
    )
