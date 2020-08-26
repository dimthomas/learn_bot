# Проект TelegramBot

Это бот для Telegram, который присылает пользователюкартинки.

## Установка

1. Клонируйте репозиторий с Github
2. Создайте виртулаьное окружение
3. Установите зависимости `pip install -r requirements.txt`
4. Создайте файл `settings.py`
5. Впишите в settings.py переменные:
```
API_KEY = "API-ключ бота"
PROXY_URL = "Адрес прокси (если необходим)"
PROXY_USERNAME = "Логин на прокси"
PROXY_PASSWORD = "Пароль на прокси"
USER_EMOJI = [':yum:', ':alien:', ':stuck_out_tongue:', ':mask:', ':poop:', ':sunglasses:', ':chicken:']
```
6. Запустите бота командой `python bot.py`