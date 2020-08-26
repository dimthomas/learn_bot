from emoji import emojize
from settings import USER_EMOJI
from random import choice, randint
from telegram import ReplyKeyboardMarkup, KeyboardButton


def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']


def play_random_number(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f"Вы загадали число {user_number}, я загадал число {bot_number}. Вы выиграли"
    elif user_number < bot_number:
        message = f"Вы загадали число {user_number}, я загадал число {bot_number}. Вы проиграли"
    else:
        message = f"Вы загадали число {user_number}, я загадал число {bot_number}. У нас ничья"
    return message


def main_keyboard():
    return ReplyKeyboardMarkup([['Герой Overwatch', KeyboardButton('Мои координаты', request_location=True)]])
