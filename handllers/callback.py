from aiogram import types, Dispatcher
from config import Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# =====================================================================================================================

async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_2 = InlineKeyboardButton('Дальше!', callback_data='button_2')
    markup.add(button_2)

    questions = 'ЧИ ИЛИ НИ ЧИ !?'
    answers = [
        'ЧИ',
        'НИ ЧИ',
        'Ты че дурак?'
    ]


    await Bot.send_poll(
        call.from_user.id,
        question=questions,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        explanation="IZI",
        open_period=60,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton('Next', callback_data='button_call_3')
    markup.add(button_call_3)

    question = 'Оромо или манты?'
    answer = [
        'Оромо',
        'Манты',
        'И то и то'
    ]

    await Bot.send_poll(
        call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        explanation="izi",
        open_period=60,
        reply_markup=markup
    )


async def quiz_4(call: types.CallbackQuery):

    question = 'Что он выведет?'
    answer = [
        'Бесконечный цикл слово Hello',
        'Выведет просто Hello'
    ]



    await Bot.send_poll(
        call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        explanation="izi",
        open_period=60
    )

# =====================================================================================================================

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text='button_1')
    dp.register_callback_query_handler(quiz_3, text='button_2')
    dp.register_callback_query_handler(quiz_4, text='button_call_3')

# =====================================================================================================================