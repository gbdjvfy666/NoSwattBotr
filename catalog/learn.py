from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton

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

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💸 От 100.000₽/месяц на ФРОДЕ CPA • 1742₽", callback_data="edu_fraud_100k")],
        [InlineKeyboardButton(text="🧩 Авторизация 2.0 от RED GROUP • 1777₽", callback_data="edu_auth_red")],
        [InlineKeyboardButton(text="🧠 Пассив + нейрорилсы • 3750₽", callback_data="edu_neuro_passive")],
        [InlineKeyboardButton(text="⚙️ ФРОД полупассив от А до Я • 1672₽", callback_data="edu_fraud_full")],
        [InlineKeyboardButton(text="🛡 Антикризисная схема • 1762₽", callback_data="edu_anti_crisis")],
        [InlineKeyboardButton(text="📊 80K на сером арбитраже • 1792₽", callback_data="edu_gray_arbitrage")],
        [InlineKeyboardButton(text="🚀 100K/мес на трафике • 1792₽", callback_data="edu_traffic_100k")],
        [InlineKeyboardButton(text="🔥 Импакт 90K от нейросети • 1755₽", callback_data="edu_neuro_impact")],
        [InlineKeyboardButton(text="🔄 YouTube + Telegram • 1782₽", callback_data="edu_yt_tg_loop")],
        [InlineKeyboardButton(text="🪙 500$/неделя на майнинге • 1798₽", callback_data="edu_mining")],
        [InlineKeyboardButton(text="💘 10-15$/3ч дейтинг • 1777₽", callback_data="edu_dating")],
        [InlineKeyboardButton(text="💳 Возврат транзакций P2P • 2100₽", callback_data="edu_p2p_return")],
        [InlineKeyboardButton(text="📈 3 P2P связки на крипте • 1980₽", callback_data="edu_p2p_crypto")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_shop")]
    ])

    await callback_query.message.answer_photo(
        photo=photo,
        caption=caption,
        parse_mode="HTML",
        reply_markup=markup
    )

    await callback_query.answer()
