from aiogram import types
from loader import dp


@dp.message_handler()
async def lets_start(message: types.Message):
    await message.answer('Чтобы начать, воспользуйся кнопкой <b>/new_doc</b>!')
