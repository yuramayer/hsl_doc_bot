from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

sex_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Мужской'),
        ],
        [
            KeyboardButton(text='Женский')
        ]
    ], resize_keyboard=True
)
