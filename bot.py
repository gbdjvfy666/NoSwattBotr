import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from config import BOT_TOKEN
from database import create_user_table

# Хендлеры
from handlers import start, shop, profile
from handlers.balance import router as balance_router
from handlers.support import router as support_router

# Каталог
from catalog.Traffic.traffic import router as traffic_router
from catalog.Abuse.abuse import router as abuse_router
from catalog.arhive import router as arhive_router
from catalog.magazinakk import router as magazinakk_router
from catalog.buisness import router as business_router
from catalog.shema import router as shema_router
from catalog.learn import router as learn_router
from catalog.lotery import router as lotery_router
from catalog.health import router as health_router
from catalog.wallets import router as wallets_router
from catalog.proxies import router as proxies_router
from catalog.sms import router as sms_router
from catalog.checks import router as checks_router
from catalog.seed import router as seed_router
from catalog.ideas import router as ideas_router
from catalog.scripts import router as scripts_router
from catalog.lastticket import router as lastticket_router


async def main():
    logging.basicConfig(level=logging.INFO)

    await create_user_table()

    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()

    # Роутеры
    dp.include_router(start.router)
    dp.include_router(shop.router)
    dp.include_router(profile.router)
    dp.include_router(traffic_router)
    dp.include_router(abuse_router)
    dp.include_router(arhive_router)
    dp.include_router(magazinakk_router)
    dp.include_router(business_router)
    dp.include_router(shema_router)
    dp.include_router(learn_router)
    dp.include_router(lotery_router)
    dp.include_router(health_router)
    dp.include_router(wallets_router)
    dp.include_router(proxies_router)
    dp.include_router(sms_router)
    dp.include_router(checks_router)
    dp.include_router(seed_router)
    dp.include_router(ideas_router)
    dp.include_router(scripts_router)
    dp.include_router(lastticket_router)
    dp.include_router(balance_router)
    dp.include_router(support_router)

    await bot.delete_webhook(drop_pending_updates=True)

    try:
        await dp.start_polling(bot)
    except asyncio.CancelledError:
        print("Polling cancelled. Shutting down...")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot manually stopped.")
