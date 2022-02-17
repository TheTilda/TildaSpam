from enum import unique
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.executor import start_webhook
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from datetime import datetime
import os
import glob
import pyrogram
import os



bot = Bot(token='5273176481:AAGqLhTwkQPMT8_Hrt8t6xyl6Bv_BbiNDJw')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

def extract_unique_code(text):
    # Extracts the unique_code from the sent /start command.
    return text.split()[1] if len(text.split()) > 1 else None


@dp.message_handler(content_types=['document'])
async def input_document(message):
    #file = await bot.get_file(message.document.file_id)
    file_info = await bot.get_file(message.document.file_id)
    await message.document.download(file_info.file_path.split('/')[1]) # ++

@dp.message_handler(commands=['start'])
async def start(message, state: FSMContext):
    unique_code = extract_unique_code(message.text)
    kb = InlineKeyboardMarkup().add(InlineKeyboardButton('Да', callback_data='yes')).add(InlineKeyboardButton('Нет', callback_data='no'))
    if unique_code and glob.glob(f'{unique_code}.session'):
        async with state.proxy() as data:
            data['files'] = glob.glob(f'{unique_code}.session')[0]
            await message.reply(f'{unique_code} \n Удалить?', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton('Да', callback_data='yes')).add(InlineKeyboardButton('Нет', callback_data='no')))
    else:
        pass
    await message.reply('АДМИН ПАНЕЛЬ', reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Изменить')))
@dp.message_handler(text='Изменить')
async def send_list(message):
    os.chdir(os.getcwd())
    for i in glob.glob('*.session'):
        await bot.send_message(message.chat.id, f'https://t.me/Spam_boomBOT?start={i.replace(".session", "")}')
    

@dp.callback_query_handler(lambda c: c.data == 'yes')
async def yes(callback_query):
    
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), callback_query.message.text.split()[0]+ '.session')
    os.remove(path)
    await bot.send_message(callback_query.from_user.id, 'Удалено')


@dp.callback_query_handler(lambda c: c.data == 'no')
async def yes(callback_query):
    await bot.send_message(callback_query.from_user.id , 'АДМИН ПАНЕЛЬ', reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Изменить')))

if __name__ == '__main__':
	executor.start_polling(dp)