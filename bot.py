from emoji import emojize
from glob import glob
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from settings import API_KEY, PROXY_URL, PROXY_USERNAME, PROXY_PASSWORD, USER_EMOJI
from random import randint, choice

logging.basicConfig(filename="bot.log", level=logging.INFO)

'''PROXY = {'proxy_url': PROXY_URL,
            'urllib3_proxy_kwargs': {'username': PROXY_USERNAME,
            'password': PROXY_PASSWORD}} - для использования прокси сервера'''


def greet_user(update, context):
    print("Вызван /start")
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f"Привет, пользователь {context.user_data['emoji']}!")


def play_random_number(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f"Вы загадали число {user_number}, я загадал число {bot_number}. Вы выиграли"
    elif user_number < bot_number:
        message = f"Вы загадали число {user_number}, я загадал число {bot_number}. Вы проиграли"
    else:
        message = f"Вы загадали число {user_number}, я загадал число {bot_number}. У нас ничья"
    return message


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
    update.message.reply_text(message)


def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']


def send_hero_picture(update, context):
    hero_list = glob("images/*png")
    hero_pic_filename = choice(hero_list)
    name_hero = hero_pic_filename.split('/')[1].split('.')
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(hero_pic_filename, 'rb'))
    update.message.reply_text(f"Твой герой {name_hero[0]}")


def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    text = update.message.text
    print(text)
    update.message.reply_text(f"{text} {context.user_data['emoji']}")


def main():
    mybot = Updater(API_KEY, use_context=True)  # добавить аргумент (request_kwargs=PROXY) для использования прокси сервера

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler("hero", send_hero_picture))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
