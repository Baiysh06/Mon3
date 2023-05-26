from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton('Backend'),
    KeyboardButton('Frontend'),
    KeyboardButton('IOS'),
    KeyboardButton('UX/IU'),
    KeyboardButton('Android'),
)

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton("CANCEL")
)