from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'API'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
   await bot.send_message(message.chat.id, message.text)

def test_hi():
   print("Hello World")

if __name__ == '__main__':
   test_hi()
   executor.start_polling(dp, skip_updates=True)
