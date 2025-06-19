from aiogram import Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.callback_query(lambda c: c.data == "item_wallets")
async def wallets_callback(callback_query: types.CallbackQuery):
    caption = (
        "👛 <b>Кошельки с балансом</b> 🔐\n\n"
        "➥ Свежайшие кошельки прямиком из печи! Лютейшие логи от воркеров, проверенные на транзакции.\n\n"
        "Отзывы:\n"
        "<a href='https://telegra.ph/Otzyvy-o-koshelkah-03-31'>https://telegra.ph/Otzyvy-o-koshelkah-03-31</a>\n\n"
        "Шанс огромных балансов и балансов в целом невероятно высокий, поэтому и цена на порядок выше, чем у обычных сид-фраз. Это вам не AI-подборщики — здесь чистая ручная добыча от топовых воркеров.\n\n"
        "Почему не отрабатываем сами? \n"
        "Говорим прямо, деньги на кошельках не совсем чистые. Оптимально использовать их для покупок, переводов или оплаты различных услуг. \n\n"
        "❗️ <b>Категорически не рекомендуем</b> выводить напрямую на личную карту, хоть и шанс что поиском крипты кто-то будет заниматься, не больше 5%, лучше не играйте с огнём. "
        "Для вывода используйте проверенные AML-чистки, хорошие сервисы можете найти на лолзе, там полно вариантов с депозитом.\n\n"
        "🧨 Товар мега-жирный и появляется в очень ограниченном количестве, небольшими партиями. "
        "<b>Если прямо сейчас есть в наличии — считай тебе конкретно фортануло.</b>"
    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Кошелек с балансом | с логов • 2100₽", callback_data="wallet_buy")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_shop")]
    ])

    await callback_query.message.answer(
        text=caption,
        parse_mode="HTML",
        reply_markup=markup
    )

    await callback_query.answer()
