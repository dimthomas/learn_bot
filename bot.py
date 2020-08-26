import logging
from settings import API_KEY, PROXY_URL, PROXY_USERNAME, PROXY_PASSWORD
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from handlers import (greet_user, guess_number, send_hero_picture,
                      user_coordinates, talk_to_me)


logging.basicConfig(filename="bot.log", level=logging.INFO)

'''PROXY = {'proxy_url': PROXY_URL,
            'urllib3_proxy_kwargs': {'username': PROXY_USERNAME,
            'password': PROXY_PASSWORD}} - для использования прокси сервера'''


def main():
    mybot = Updater(API_KEY, use_context=True)  # добавить аргумент (request_kwargs=PROXY) для использования прокси сервера

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler("hero", send_hero_picture))
    dp.add_handler(MessageHandler(Filters.regex('^(Герой Overwatch)$'), send_hero_picture))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
