from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.callback_query(F.data == "shop")
async def show_shop(callback: CallbackQuery):
    # Кнопки вручную по строкам
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📦 Деньги на трафике", callback_data="item_traffic")],
        [InlineKeyboardButton(text="📂 Абузы", callback_data="item_abuse"),
         InlineKeyboardButton(text="🗃 Архивы", callback_data="item_archives")],
        [InlineKeyboardButton(text="👤 Аккаунты", callback_data="item_accounts")],
        [InlineKeyboardButton(text="🏪 Готовый бизнес", callback_data="item_business"),
         InlineKeyboardButton(text="🎓 Обучение", callback_data="item_edu")],
        [InlineKeyboardButton(text="🎟 Лотерея", callback_data="item_lottery")],
        [InlineKeyboardButton(text="❤️ Здоровье", callback_data="item_health"),
         InlineKeyboardButton(text="💼 Кошельки с балансом", callback_data="item_wallets")],
        [InlineKeyboardButton(text="🌐 Прокси", callback_data="item_proxies")],
        [InlineKeyboardButton(text="📲 СМС-чеки", callback_data="item_sms"),
         InlineKeyboardButton(text="🧠 Сид-фразы", callback_data="item_seed")],
        [InlineKeyboardButton(text="🚀 Бизнес-идеи", callback_data="item_ideas")],
        [InlineKeyboardButton(text="💻 Скрипты", callback_data="item_scripts"),
         InlineKeyboardButton(text="🎫 Последний билет", callback_data="item_lastticket")]
    ])
    
    await callback.message.edit_text("📦 Каталог товаров:", reply_markup=markup)
