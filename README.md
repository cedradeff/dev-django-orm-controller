# Пульт охраны банка
Это внутренний скрипт для подсчета общего количества пропусков и количества активных пропусков.

# Установка
1. Клонировать репозиторий: 
`git clone https://github.com/cedradeff/dev-django-orm-controller.git`
2. Установить зависимости:
`pip install -r requirements.txt`
3. Заполнить данные для подключения к БД в файле `.env`:
Занести в переменную DB_URL URL (пример для postgres БД):
`postgres://USER:PASSWORD@HOST:PORT/NAME`

# Запуск
Запустить скрипт командой:
`python main.py`