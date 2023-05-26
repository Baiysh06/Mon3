 # SQL - Structured Query Language
# СУБД - Система Управления Базой Данных
# CRUD = Create Read Update Delete
from aiogram import types, Dispatcher
import random
import sqlite3
#=====================================================================================================================

db = sqlite3.connect("database/bot.sqlite3")
cursor = db.cursor()

#=====================================================================================================================

def sql_create():

    if db:
        print("База данных подключена!")
        db.execute("CREATE TABLE IF NOT EXISTS mentors "
                   "(named VARCHAR (255), "
                   "direction VARCHAR(255), "
                   "age INTEGER, "
                   "gruppa VARCHAR(255))")

    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentors "
                       "(named, direction, age, gruppa) VALUES "
                       "(?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random_mentors(message : types.Message):
    result = cursor.execute("SELECT * FROM mentors").fetchall()
    user = random.choice(result)
    await message.answer(
        f"Name:  {user[0]} \nDirection:  {user[1]} \n"
        f"Age:  {user[2]} \nGroup:  {user[3]}"
    )

async def sql_command_all():
    return cursor.execute("SELECT * FROM mentors").fetchall()


async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM mentors WHERE id = ?", (user_id,))
    db.commit()

#=====================================================================================================================

def register_message_Bot_db(dp: Dispatcher):
    dp.register_message_handler(sql_command_random_mentors, commands=['get'])
