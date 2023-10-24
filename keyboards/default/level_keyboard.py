from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

level_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Бакалавриат'),
        ],
        [
            KeyboardButton(text='Магистратура')
        ]
    ], resize_keyboard=True
)
