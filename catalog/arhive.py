from aiogram import Router, types
from aiogram.types import FSInputFile

router = Router()

@router.callback_query(lambda c: c.data == "item_archives")
async def archives_callback(callback_query: types.CallbackQuery):

    photo = FSInputFile("images/arhive.jpg")  # убедись, что файл существует

    caption = (
        "🔞 <b>Архивы</b>\n\n"
        "❤️‍🔥 <b>Что это такое?</b> — <a href='https://telegra.ph/CHto-takoe-arhiv-i-chto-za-sleng-03-24'>Ответ здесь</a>\n\n"
        "➥ <b>Эксклюзивы</b> — самые элитные архивы: с окончаниями внутрь, сногсшибательные красотки, вписки и жёсткие сцены без цензуры.\n\n"
        "➥ <b>Любительские</b> — от 18-летних до MILF, анала, сквирта, ролевых игр. Всё, что вы любите, собрано в лучших архивах.\n\n"
        "➥ <b>Разное</b> — подборки сладких бывших, шлюшек, медленного глубокого секса и редких нишевых тем.\n\n"
        "➥ <b>Подписки</b> — эксклюзивные сливы каждую неделю. Три уровня, последний из которых включает всё и даже больше:\n"
        "😍 Бонусом — архивы с лишением девственности.\n\n"
        "💡 <i>Хватит тратить время на поиски — у нас всё уже собрано!</i>"
    )

    await callback_query.message.answer_photo(
        photo=photo,
        caption=caption,
        parse_mode="HTML"
    )
    await callback_query.answer()
