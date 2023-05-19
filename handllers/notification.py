import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer('готово!')

async def go_to_beautician():
        await bot.send_message(chat_id=chat_id, text='Запишись к косметологу ♥')

async def scheduler():
    aioschedule.every().saturday.at('9:30').do(go_to_beautician)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(3)



def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id)
