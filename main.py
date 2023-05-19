from aiogram.utils import executor
import logging
from handllers import callback, commands, extra, fsmAdminMentor, notification
import asyncio

from config import dp
from database.bot_db import sql_create

async def on_startup(_):
    asyncio.create_task(notification.scheduler())
    sql_create()


callback.register_handlers_callback(dp)
commands.register_handler_command(dp)
callback.register_handlers_callback(dp)
fsmAdminMentor.register_handlers_fsm_anketa(dp)
notification.register_handlers_notification(dp)


extra.register_handlers_extra(dp)



# @dp.message_handler(commands=['mem'])
# async def mem1(message: types.Message):
#     photo = open('media/mem.jpg', 'rb')
#     photo = open('media/mem1.jpg', 'rb')
#     photo = open('media/mem2.jpg', 'rb')
#     photo = open('media/mem3.jpg', 'rb')
#     await bot.send_photo(message.from_user.id, photo=photo)




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
