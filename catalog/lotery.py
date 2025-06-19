from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.callback_query(lambda c: c.data == "item_lottery")
async def lottery_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("images/lotery.jpg") 

    caption = (
        "🎫 <b>Лотерея</b>\n\n"
        "➥ <b>Банк лотереи</b> формируется <i>исключительно за счёт</i> покупки билетов участниками.\n"
        "➥ Мы сотрудничаем с крупными магазинами, где тоже представлены наши розыгрыши — "
        "поэтому <b>банк набирается очень быстро</b>!\n\n"
        "🔥 Чем больше у тебя билетов — тем выше шансы на победу. Никаких ограничений на количество!\n\n"
        "🎁 <i>Ты можешь выиграть главный приз буквально с одного билета.</i>\n"
        "И не волнуйся — <b>если ты победишь</b>, мы <u>сами напишем тебе и вручим приз</u>.\n\n"
        "🎊 Участвуй — и пусть именно <b>твой</b> билет окажется победным! 👇"
    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="ПРИЗОВОЙ: 300.000₽ • 450₽", callback_data="lottery_300k")],
        [InlineKeyboardButton(text="ПРИЗОВОЙ: 200.000₽ • 300₽", callback_data="lottery_200k")],
        [InlineKeyboardButton(text="ПРИЗОВОЙ: 100.000₽ • 150₽", callback_data="lottery_100k")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_shop")]
    ])

    await callback_query.message.answer_photo(
        photo=photo,
        caption=caption,
        parse_mode="HTML",
        reply_markup=markup
    )

    await callback_query.answer()
