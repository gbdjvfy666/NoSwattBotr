import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import router
from database import init_db



async def main():
    # Инициализируем бота без дополнительных аргументов
    bot = Bot(token=BOT_TOKEN)

    
    dp = Dispatcher()
    dp.include_router(router)

    # Инициализация базы данных
    await init_db()
    print("Бот запущен!")
    
    # Запускаем бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

