import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from handlers import start_handlers, calc_handlers, order_handlers
from database import database
import os


# Функция конфигурирования и запуска бота
async def main():
    # Инициализируем бот и диспетчер
    load_dotenv()
    bot = Bot(
        token=os.getenv('TOKEN'),  # sima_test
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()

    # Запускаем базу данных
    await database.db_start()

    # Регистриуем роутеры в диспетчере
    dp.include_router(start_handlers.router)
    dp.include_router(calc_handlers.router)
    dp.include_router(order_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
