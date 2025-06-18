from aiogram import Router, types
from aiogram.types import FSInputFile

router = Router()

@router.callback_query(lambda c: c.data == "item_edu")
async def education_callback(callback_query: types.CallbackQuery):
    photo = FSInputFile("images/learn.jpg") 
    caption = (
        "🎓 <b>Обучение</b>\n\n"
        "➥ <b>Дорогостоящие курсы</b> по доступной цене.\n"
        "➥ На любой вкус, цвет и уровень подготовки.\n\n"
        "📚 <i>Самое ценное вложение — это знания.</i>\n"
        "Изучив сотни материалов, вы оторвётесь от большинства настолько, будто бы сравнивают "
        "обезьяну с Альбертом Эйнштейном — как бы громко это ни звучало.\n\n"
        "🌍 Люди, знающие многое в разных сферах, ценятся везде: и в обществе, и у работодателей, "
        "и могут <b>сами стать БОССАМИ</b>.\n\n"
        "🚀 Начни учиться сегодня — и станешь в разы сильнее завтра."
    )

    await callback_query.message.answer_photo(
        photo=photo,
        caption=caption,
        parse_mode="HTML"
    )

    await callback_query.answer()
