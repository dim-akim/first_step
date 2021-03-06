"""
Комментарий для проверки работы гитхаба
"""

from flask import Flask, render_template

server = Flask(__name__)


@server.route('/')  # декоратор, который назначает путь
def hello():  # функция представления
    return '''Hello, World!
    <br>
    <a target="_blank" href="index">index</a>'''


# Добавить URL для ловли GET-запросов
# Добавить новый файл для отправки запросов и чтения ответов
# Нужна библиотека requests


@server.route('/index')
def index():  # функция представления
    name = 'Дмитрий Валерьевич'
    return render_template('index.html')


@server.route('/day-<num>')  # num - переменная
def day(num):  # функция представления
    return render_template(f'day-{num}.html')


server.run()  # Ctrl + Shift + F10
