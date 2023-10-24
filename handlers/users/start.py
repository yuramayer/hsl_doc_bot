from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp


@dp.message_handler(Command('start'))
async def lets_start(message: types.Message):
    await message.answer('Привет! 🙋🏼‍♀️\n\n'
                         'Я помогаю студентам Высшей Школы Права оформить справку об обучении.\n\n'
                         '👉🏻 Для того, чтобы начать, выбери команду <b>/new_doc</b>')
