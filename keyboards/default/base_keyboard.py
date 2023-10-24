from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

base_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Бюджет'),
        ],
        [
            KeyboardButton(text='Коммерция')
        ]
    ], resize_keyboard=True
)
