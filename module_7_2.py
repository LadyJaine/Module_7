# Задача "Записать и запомнить":
# Создайте функцию custom_write(file_name, strings), которая принимает аргументы
# file_name - название файла для записи, strings - список строк для записи.
# Функция должна:
# Записывать в файл file_name все строки из списка strings, каждая на новой строке.
# Возвращать словарь strings_positions, где ключом будет кортеж
# (<номер строки>, <байт начала строки>),
# а значением - записываемая строка.
# Для получения номера байта начала строки используйте метод tell() перед записью.
# Пример полученного словаря:
# {(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
# Где:
# 1, 2 - номера записанных строк.
# 0, 16 - номера байт, на которых началась запись строк.
# 'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.

from pprint import pprint
strings1 = ['Text for tell.','Используйте кодировку utf-8.',
               'Because there are 2 languages!','Спасибо!']
file_name = 'file_name.txt'

def custom_write(file_name, strings):
    file = open(file_name, "a", encoding='utf-8')
    strings_position = {}
    counter = 0
    for i in strings:
        counter += 1
        p = file.tell()
        strings_position[(counter, p)] = i
        file.write(i +'\n')
    file.close()
    return strings_position

pprint(custom_write(file_name,strings1))


