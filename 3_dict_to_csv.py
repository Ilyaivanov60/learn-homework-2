"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    user_lst = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        {'name': 'Петя', 'age': 33, 'job': 'Doctor'}
    ]

    with open('export.csv', 'w', encoding='utf-8') as file:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(file, fields, delimiter = ';')
        writer.writeheader()
        for user in user_lst:
            writer.writerow(user)
if __name__ == "__main__":
    main()
