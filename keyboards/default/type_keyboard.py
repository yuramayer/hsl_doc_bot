from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

type_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Очная'),
        ],
        [
            KeyboardButton(text='Заочная')
        ],
        [
            KeyboardButton(text='Очно-заочная')
        ]
    ], resize_keyboard=True
)
