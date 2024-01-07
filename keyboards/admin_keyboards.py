from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def keyboard_admin():
    # Создаем объекты inline-кнопок
    button1 = InlineKeyboardButton(
        text='Рассылка',
        callback_data='mailing'
    )
    button2 = InlineKeyboardButton(
        text='Статистика',
        callback_data='stats'
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[button1, button2]]
    )
    return keyboard
