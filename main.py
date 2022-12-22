#Modules
from settings import TOKEN, ADMIN_ID
import logging
import time

from aiogram import Bot, Dispatcher, executor, types


#Cog
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


#Handlers
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message()):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_name = message.from_user.first_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')

    await message.reply(f'Спасибо {user_name} за то, что добавил меня!')



if __name__ == '__main__':
    executor.start_polling(dp)

    