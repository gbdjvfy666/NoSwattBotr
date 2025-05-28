from aiogram import Router, types, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart
from config import RECEIVER_ADDRESS
from database import add_user
from aiogram.utils.markdown import hlink

router = Router()

# === Настройки ===
REF_LINK = "https://1wmndv.life/?p=mvmr"
SUPPORT_LINK = "https://t.me/noswattw"
CLOSED_CHANNEL = "ITL"
CHECK_CHANNEL = "@noswattt"  # для проверки подписки

# === Меню ===
def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎁 Получить бонус 500%", callback_data="get_bonus")],
        [InlineKeyboardButton(text="📘 Как сделать депозит?", callback_data="how_to_deposit")],
        [InlineKeyboardButton(text="📞 Поддержка", url=SUPPORT_LINK)]
    ])

# === Команда /start ===
@router.message(CommandStart())
async def cmd_start(message: Message, bot):
    await add_user(
        tg_id=message.from_user.id,
        username=message.from_user.username,
        full_name=message.from_user.full_name
    )

    welcome_text = (
        f"👋 Привет, {message.from_user.first_name}!\n\n"
        "Добро пожаловать в бот проекта 🧠 NoSwatt!\n\n"
        "📌 Здесь ты получишь:\n"
        "— 🎁 Бонус 500% на 1win\n"
        "— 📘 Пошаговую инструкцию\n"
        "— 🔐 Доступ в закрытый Telegram-канал\n\n"
        "👇 Выбирай, с чего начать:"
    )

    await message.answer(welcome_text, reply_markup=main_menu())

# === Кнопка: Получить бонус ===
@router.callback_query(F.data == "get_bonus")
async def handle_bonus(callback: CallbackQuery, bot):
    user_id = callback.from_user.id

    # Проверка подписки
    try:
        member = await bot.get_chat_member(chat_id=CHECK_CHANNEL, user_id=user_id)
        if member.status not in ("member", "administrator", "creator"):
            raise ValueError("not subscribed")
    except:
        await callback.message.answer("❗ Чтобы получить бонус, подпишись на канал:", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="📢 Перейти в канал", url="https://t.me/noswattt")],
                [InlineKeyboardButton(text="✅ Я подписался", callback_data="check_sub")]
            ]
        ))
        return

    # При успешной подписке:
    await callback.message.answer(
        "✅ Подписка подтверждена!\n\n📘 Инструкция:\n"
        "1. Перейди по кнопке и зарегистрируйся\n"
        "2. Соверши депозит\n"
        "3. Получи до 500% бонусов\n\n"
        "После этого тебе будет доступен канал с прогнозами 👇",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔗 Перейти на 1win", url=REF_LINK)],
            [InlineKeyboardButton(text="🚪 Войти в закрытый канал", url=f"https://t.me/+s6J8oZOnS-M5ZjRi")]
        ])
    )

# === Проверка после подписки ===
@router.callback_query(F.data == "check_sub")
async def check_subscription(callback: CallbackQuery, bot):
    user_id = callback.from_user.id

    try:
        member = await bot.get_chat_member(chat_id=CHECK_CHANNEL, user_id=user_id)
        if member.status not in ("member", "administrator", "creator"):
            raise ValueError("not subscribed")
    except:
        await callback.message.answer("❌ Подписка не найдена. Попробуй снова после подписки.")
        return

    await callback.message.answer("✅ Подписка подтверждена!\nТы получаешь бонус на 1win и доступ в закрытый канал с прогнозами.", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔗 Как получить бонус", url=REF_LINK)],
        [InlineKeyboardButton(text="🚪 Постучаться в закрытый канал", url=f"https://t.me/+s6J8oZOnS-M5ZjRi")]
    ]))

# === Как сделать депозит ===
@router.callback_query(F.data == "how_to_deposit")
async def how_to_deposit(callback: CallbackQuery):
    text = (
        "📘 Как сделать депозит на 1win:\n\n"
        "1. Перейди на сайт 1win: " + f"https://1wmndv.life/?p=mvmr" + "\n"
        "2. Зарегистрируйся\n"
        "3. Перейди в раздел «Касса»\n"
        "4. Выбери способ пополнения\n"
        "5. Пополни баланс и получи бонус 🎁"
    )
    await callback.message.answer(text, parse_mode="HTML")
    