"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date = datetime.now()
    delta = timedelta(days=30)
    print(date - delta)


def str_2_datetime(dt):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_format = datetime.strptime(dt, '%d/%m/%y.%H:%M:%S')
    return date_format

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20.12:10:03"))
