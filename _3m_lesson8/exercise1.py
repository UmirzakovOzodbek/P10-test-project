import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "6045806921:AAHXCASHFc_l7wMzVBvruG_uwvINQ8DN5vo"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handlers(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user send /start or /help command
    """
    await message.reply("Hi\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handlers()
async def echo(message: types.Message):
    # old style:
    # await bot

    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)





