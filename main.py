#Modules
from settings import TOKEN, SET_STICKERS_ID
import logging
import time
import random

from aiogram import Bot, Dispatcher, executor, types


#Cog
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

HELP_TXT = '''
/description - описание бота
/help - команды бота
'''

DESCRIPTION_TXT = '''
Бот, который отправляет смешнявки
'''

async def on_startup(_):
    print('running')

#Handlers
@dp.message_handler(commands=['description'])
async def description(message: types.Message):
    await message.reply(text=DESCRIPTION_TXT)

@dp.message_handler(commands=['help'])
async def description(message: types.Message):
    await message.reply(text=HELP_TXT)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='<em>Никита сделал бота - GC!!!</em>', parse_mode='HTML')

@dp.message_handler()
async def random_sticker_reply(message: types.Message or types.Sticker):
    k = random.randint(0, 6)
    if k == 3:
        await bot.send_sticker(message.from_user.id, sticker=random.choice(SET_STICKERS_ID))

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

    