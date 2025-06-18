from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, FSInputFile

router = Router()

@router.message(F.text == "/start")
async def start_handler(message: Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🏪 Каталог товаров"), KeyboardButton(text="💳 Пополнить баланс")],
            [KeyboardButton(text="🪪 Мой профиль"), KeyboardButton(text="📩 Связаться")],
            [KeyboardButton(text="🎁ПОЛУЧИ БОНУСЫ🎁")],
        ],
        resize_keyboard=True
    )

    photo = FSInputFile("images/welcome.jpg")  

    caption = (
        "<b>👋 Добро пожаловать.</b>\n\n"
        "Скорее всего у многих из вас появится вопрос — <i>«почему всё так дёшево?»</i>, "
        "и он более чем логичен, ведь цены у нас и в правду крайне низкие. Я отвечу вам на него:\n\n"
        "Мы зарабатываем на том, что покупаем дорогостоящие материалы и продаём их по более низкому прайсу, "
        "чем у авторов, но на более обширную аудиторию!\n\n"
        "❗️<b>Правила магазина:</b> <a href='https://teletype.in/@userofferagreement/UkSB5QtXVxu'>ссылка</a>"
    )

    await message.answer_photo(photo, caption=caption, reply_markup=kb, parse_mode="HTML")
