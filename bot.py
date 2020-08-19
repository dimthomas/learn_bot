import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from settings import API_KEY, PROXY_URL, PROXY_USERNAME, PROXY_PASSWORD

logging.basicConfig(filename="bot.log", level=logging.INFO)

#PROXY = {'proxy_url': PROXY_URL, 'urllib3_proxy_kwargs': {'username': PROXY_USERNAME, 'password': PROXY_PASSWORD}} - для использования прокси сервера


def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text("Привет, мудило")


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater(API_KEY, use_context=True) # добавить аргумент (request_kwargs=PROXY) для использования прокси сервера

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
