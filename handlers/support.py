from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.callback_query(F.data == "support")
async def support_view(callback: CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📨 Создать обращение", callback_data="create_ticket")],
        [InlineKeyboardButton(text="📁 Мои обращения", callback_data="my_tickets")]
    ])
    await callback.message.edit_text("📩 Поддержка\n\nЗдесь вы можете обратиться в службу поддержки:", reply_markup=kb)