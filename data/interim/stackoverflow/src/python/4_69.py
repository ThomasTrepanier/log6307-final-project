from asyncio import get_event_loop
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'API'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot, loop=get_event_loop())  # Initialising event loop for the dispatcher

async def notify_message():
    print('Hello World')

if __name__ == '__main__':
    dp.loop.create_task(notify_message())  # Providing awaitable as an argument
    executor.start_polling(dp, skip_updates=True)
