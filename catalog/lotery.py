from aiogram import Router, types
from aiogram.types import FSInputFile

router = Router()

@router.callback_query(lambda c: c.data == "item_lottery")
async def lottery_callback(callback_query: types.CallbackQuery):
    # Обложка для раздела «Лотерея»
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

    await callback_query.message.answer_photo(
        photo=photo,
        caption=caption,
        parse_mode="HTML"
    )

    await callback_query.answer()
