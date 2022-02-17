from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

main_kb = ReplyKeyboardMarkup()
main_kb.add(KeyboardButton('Добавить аккаунт'))

otmena_kb = ReplyKeyboardMarkup()
otmena_kb.add(KeyboardButton('Отмена'))