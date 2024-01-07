from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup


def get_contact():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True,
                                   keyboard=[[KeyboardButton(text='Отправить номер телефона',
                                                             request_contact=True)]])
    return keyboard


def keyboard_1():
    # Создаем объекты inline-кнопок
    button1 = InlineKeyboardButton(
        text='Аффирмация',
        callback_data='aff'
    )
    button2 = InlineKeyboardButton(
        text='Код богатства',
        callback_data='cod'
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[button1, button2]]
    )
    return keyboard


def affirmacia_keyboard():
    # Создаем объекты inline-кнопок
    button1 = InlineKeyboardButton(
        text='Волна',
        callback_data='volna'
    )
    button2 = InlineKeyboardButton(
        text='Гармония',
        callback_data='garmonia'
    )
    button3 = InlineKeyboardButton(
        text='Релакс',
        callback_data='relax'
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[button1, button2, button3]]
    )
    return keyboard
