from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

@router.message(F.text == "/start")
async def start_handler(message: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛍 Каталог товаров", callback_data="shop")],
        [InlineKeyboardButton(text="💳 Пополнить баланс", callback_data="topup")],
        [InlineKeyboardButton(text="🪪 Мой профиль", callback_data="profile")],
        [InlineKeyboardButton(text="📩 Связаться", callback_data="support")],
        [InlineKeyboardButton(text="🎁 Получить бонусы", callback_data="bonus")],
    ])
    await message.answer("👋 Добро пожаловать в магазин!", reply_markup=kb)

@router.callback_query(F.data == "shop")
async def show_shop(callback: CallbackQuery):
    items = [
        "📦 Деньги на трафике", "📂 Абузы", "🗃 Архивы", "👤 Аккаунты", "🏪 Готовый бизнес",
        "🎓 Обучение", "🎟 Лотерея", "❤️ Здоровье", "💼 Кошельки с балансом",
        "🌐 Прокси", "📲 СМС-чеки", "🧠 Сид-фразы", "🚀 Бизнес-идеи", "💻 Скрипты", "🎫 Последний билет"
    ]
    text = "\n".join([f"• {item}" for item in items])
    await callback.message.edit_text(f"📦 Каталог товаров:\n{text}")

@router.callback_query(F.data == "topup")
async def topup_balance(callback: CallbackQuery):
    builder = InlineKeyboardBuilder()
    for amount in [250, 500, 1000, 2000, 3000, 4000, 5000, 10000, 15000, 20000]:
        builder.button(text=f"{amount}₽", callback_data=f"topup_{amount}")
    builder.button(text="Другая сумма", callback_data="topup_custom")
    builder.adjust(3)
    await callback.message.edit_text("💳 Выберите сумму для пополнения (мин. 50₽):", reply_markup=builder.as_markup())

@router.callback_query(F.data == "profile")
async def profile_view(callback: CallbackQuery):
    user_id = callback.from_user.id
    # Здесь можно добавить запрос в БД
    text = (
        f"🪪 Мой профиль\n\n"
        f"ID: {user_id}\n"
        f"Регистрация: 16.06.2025\n\n"
        f"Основной баланс: 0₽\n"
        f"Партнёрский баланс: 0₽\n\n"
        f"Статистика\nВсего покупок: 0\n"
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛒 Мои заказы", callback_data="my_orders")],
        [InlineKeyboardButton(text="💳 Пополнить", callback_data="topup")],
        [InlineKeyboardButton(text="🤝 Реферальная программа", callback_data="referral")]
    ])
    await callback.message.edit_text(text, reply_markup=kb)

@router.callback_query(F.data == "support")
async def support_view(callback: CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📨 Создать обращение", callback_data="create_ticket")],
        [InlineKeyboardButton(text="📁 Мои обращения", callback_data="my_tickets")]
    ])
    await callback.message.edit_text("📩 Поддержка\n\nЗдесь вы можете обратиться в службу поддержки:", reply_markup=kb)

@router.callback_query(F.data == "bonus")
async def bonus_view(callback: CallbackQuery):
    await callback.message.edit_text("🎁 Бонусы и розыгрыши:\n\nСледи за обновлениями и акциями. Не пропусти халяву!")
