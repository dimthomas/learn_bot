from glob import glob
from random import choice

from utils import get_smile, play_random_number, main_keyboard


def greet_user(update, context):
    print("Вызван /start")
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(
        f"Привет, пользователь {context.user_data['emoji']}!",
        reply_markup=main_keyboard()
    )


def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    text = update.message.text
    print(text)
    update.message.reply_text(f"{text} {context.user_data['emoji']}", reply_markup=main_keyboard())


def guess_number(update, context):
    print(context.args)
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_number(user_number)
        except (TypeError, ValueError):
            message = "Введите целое число"
    else:
        message = "Введите число"
    update.message.reply_text(message, reply_markup=main_keyboard())


def send_hero_picture(update, context):
    hero_list = glob("images/*png")
    hero_pic_filename = choice(hero_list)
    name_hero = hero_pic_filename.split('/')[1].split('.')
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(hero_pic_filename, 'rb'), reply_markup=main_keyboard())
    update.message.reply_text(f"Твой герой {name_hero[0]}")


def user_coordinates(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    coords = update.message.location
    update.message.reply_text(
        f"Ваши координаты {coords} {context.user_data['emoji']}!",
        reply_markup=main_keyboard()
    )
