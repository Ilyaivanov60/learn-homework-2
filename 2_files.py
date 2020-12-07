"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt') as file:
        # counter = 0
        # for line in file:
        #     line = line.split()
        #     counter += len(line)
        for line in file:
            line = line.replace('!', '.')
            with open ('referat2.txt', 'a') as file2:
                file2.write(line)
    # print(counter)
if __name__ == "__main__":
    main()
