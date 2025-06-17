from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()

@router.callback_query(F.data == "bonus")
async def bonus_view(callback: CallbackQuery):
    await callback.message.edit_text("🎁 Бонусы и розыгрыши:\n\nСледи за обновлениями и акциями. Не пропусти халяву!")