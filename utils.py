from clarifai.rest import ClarifaiApp
from emoji import emojize
from settings import USER_EMOJI, CLARIFAI_API_KEY
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
    return ReplyKeyboardMarkup([
        ['Герой Overwatch', KeyboardButton('Мои координаты', request_location=True), 'Заполнить анкету']
        ], resize_keyboard=True)


def is_cat(file_name):
    app = ClarifaiApp(api_key=CLARIFAI_API_KEY)
    model = app.public_models.general_model
    responce = model.predict_by_filename(file_name, max_concepts=5)
    if responce['status']['code'] == 10000:
        for concept in responce['outputs'][0]['data']['concepts']:
            if concept['name'] == 'cat':
                return True
    return False


if __name__ == "__main__":
    print(is_cat("images/cat1.jpeg"))
    print(is_cat("images/ANA.png"))
