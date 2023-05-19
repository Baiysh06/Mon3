from config import Bot
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

from perser.cross import parser


# =====================================================================================================================

async def start_handler(message: types.Message):
    await Bot.send_message(message.from_user.id,
                           f"Hello {message.from_user.first_name}",)
    await Bot.send_message(message.from_user.id,
                           f"Commands: \n"
                           f"/start\n"
                           f"/info\n"
                           f"/quiz\n"
                           f"/mem\n\n")


async def info_handler(message: types.Message):
    await message.answer("Гугли!")


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('Next', callback_data='button_call_1')
    markup.add(button_call_1)

    question = "By whom invented Python?"
    answers = [
        "Harry Potter",
        "Putin",
        "Guido Van Rossum",
        "Voldemort",
        "Griffin",
        "Linus Torvalds",
    ]


    await message.answer_poll(
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        open_period=10,
        reply_markup=markup
    )


async def images_mem(message: types.Message):
    photo = open('media/img.png', 'rb')
    await Bot.send_photo(message.from_user.id, photo=photo)


async def cross_handler(message: types.Message):
    for data in parser():
        await message.answer_photo(
            data['img'],
            caption=f"<a href='{data['url']}'>{data['brand']}</a>\n"
                    f"<b>{data['link']}</b>\n"
                    f"#Y{data['price']}\n",
            reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton("Смотреть ->", url=data['url'])
            ),
            parse_mode=ParseMode.HTML

        )




# =====================================================================================================================

def register_handler_command(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(info_handler, commands=['info'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(cross_handler, commands=['parser'])
    # dp.register_message_handler(images_mem, commands=['mem'])
