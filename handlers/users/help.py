from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from keyboards.default import no_kb
from loader import dp


@dp.message_handler(Command('help'), state='*')
async def help_me(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('👩🏼‍💻 Чтобы начать, воспользуйся командой <b>/new_doc</b>\n\n'
                         '🖇 Другие боты МГЮА : <b>@msalbots</b>\n\n'
                         'По проблемам, опечаткам и коммерческим предложениям обращайся: Юра, <b>@botrqst</b> 😉 ',
                         reply_markup=no_kb)
