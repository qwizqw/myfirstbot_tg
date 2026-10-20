import asyncio
import logging
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

# 1. Настройка логирования (чтобы видеть ошибки в консоли)
logging.basicConfig(level=logging.INFO)

# 2. Токен бота
# ВАЖНО: Лучше хранить токен отдельно, но для начала вставим сюда.
# Замени 'YOUR_TOKEN_HERE' на свой реальный токен из Шага 1
BOT_TOKEN = input('Введи ключ бота')

# 3. Инициализация объектов
# Bot - сам клиент, который общается с серверами Telegram
# Dispatcher - диспетчер событий, он решает, кто будет обрабатывать входящее сообщение
# Router - маршрутизатор, куда привязываются хэндлеры (обработчики)
router = Router()
dp = Dispatcher()
dp.include_router(router)

# 4. Хэндлер (Обработчик) команды /start
# @router.message(CommandStart()) говорит: "Если пришла команда /start, запусти эту функцию"
@router.message(CommandStart())
async def handle_start(message: Message):
    # message.text содержит текст сообщения
    # Ответим пользователю
    await message.answer("Привет! \nСпасибо за обращение!")


# 5. ГЛАВНАЯ ФУНКЦИЯ ЗАПУСКА
async def main():
# Создаем бота с полученным токеном
    bot = Bot(token=BOT_TOKEN)

    try:
    # 5.1. Говорим всем: "Я стартую"
        print("Бот запущен! ...")

    # 5.2. Включаем режим ожидания сообщений.
    # Программа ЗАВИСАЕТ здесь навсегда, пока её не убьют.
        await dp.start_polling(bot)

    finally:
    # 5.3. Как только polling прекратился (любой причиной):
    # Аккуратно закрываем соединение с Telegram API.
    # Это хорошая гигиена кода.
        await bot.session.close()


# 6. Точка входа: запускаем асинхронную функцию main()
if __name__ == "__main__":
    asyncio.run(main())