from aiogram import Dispatcher, types
from config import bot, ADMIN
from database.bot_db import sql_command_all, sql_command_delete
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def delete_data(message: types.Message):
    users = await sql_command_all()
    for user in users:
        await bot.send_message(
            message.from_user.id, user['id'],
            caption=f"{user['name']} {user['age']} {user['direction']} "
                    f"{user['group']}",
            reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton(f"delete {user[1]}",
                                     callback_data=f"delete {user[0]}")
            )
        )


async def delete_user(message: types.Message):
    users = await sql_command_all()
    for user in users:
        await bot.send_message(message.from_user.id,
                               f"id - {user[0]},name - {user[1]},dir - {user[2]}, "
                               f"age - {user[3]}, group - {user[4]}",
                               reply_markup=InlineKeyboardMarkup().add(
                                   InlineKeyboardButton(f"Delete {user[1]}", callback_data=f"delete {user[0]}")
                               ))
async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(int(call.data.replace('delete ', '')))
    await call.answer(text="Стёрт с базы данных", show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)


async def bin_handler(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMIN:  # Закреплять сообщения могут только админы
            await message.answer('Ты не админ!')
        elif not message.reply_to_message:
            await message.answer('Команда должна быть ответом на сообщение!')
        else:
            await bot.pin_chat_message(message.chat.id,
                                       message.reply_to_message.message_id)
    else:
        await message.answer('Пиши в группу')

def register_message_admin(dp: Dispatcher):
    dp.register_message_handler(delete_user, commands=["del"])
    dp.register_callback_query_handler(
        complete_delete,
        lambda call: call.data and call.data.startswith("delete")
    )
    dp.register_message_handler(bin_handler, commands=['bin'], command_prefix='!/')