#Modules
from settings import TOKEN
from consts import HELP_TXT, DESCRIPTION_TXT, SET_STICKERS_ID, KIR_ID
import logging
import time
import random

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


#Cog
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True,
one_time_keyboard=True)
button_1 = KeyboardButton('/help')
button_2 = KeyboardButton('/description')
button_3 = KeyboardButton('/start')
kb.add(button_1).add(button_2).add(button_3)

async def on_startup(_):
    print('running...')

#Handlers
@dp.message_handler(commands=['description'])
async def description(message: types.Message):
    await message.reply(text=DESCRIPTION_TXT, 
    parse_mode='HTML')
    await message.delete()

@dp.message_handler(commands=['help'])
async def description(message: types.Message):
    await message.reply(text=HELP_TXT)
    await message.delete()

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='<em>Никита сделал бота - GC!!!</em>', 
    parse_mode='HTML')
    await message.delete()

@dp.message_handler()
async def random_sticker_reply(message: types.Message | types.Sticker):
    k = random.randint(0, 6)
    if k == 3 or message.from_user.id == KIR_ID:
        comp = random.randint(0,11)
        if message.from_user.id == KIR_ID and comp == 6:
            await message.reply(text='<em>Кирилл, ты сегодня такой красивый</em>', parse_mode='HTML')
        else:
            await bot.send_sticker(message.chat.id,
            sticker=random.choice(SET_STICKERS_ID))

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

    