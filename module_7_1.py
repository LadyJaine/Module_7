from pprint import pprint

class Product:
    def __init__(self,name:str,weight:float,category:str):
        self.name = name
        self.weight = weight
        self.category = category
        return

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'
class Shop:
    def __init__(self,__file_name = 'products.txt'):
        self.__file_name = __file_name


    def get_products(self):  #открыли файл, считали информацию, вернули информацию в единой строке
        file = open(self.__file_name, "r",encoding='utf-8')
        rosmen = file.read()
        file.close()
        return rosmen

    def add(self, *products):
        for i in products:
            file = open(self.__file_name, 'a',encoding='utf-8')
            if i.name not in self.get_products():
                file.write(str(i)+'\n')
            else:
                print(f'Продукт {i.name} уже есть в магазине.')

# Пример работы программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__
print()
s1.add(p1, p2, p3)

print(s1.get_products())
#
# Вывод на консоль:
# Первый запуск:
# Spaghetti, 3.4, Groceries
# Продукт Potato уже есть в магазине
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Второй запуск:
# Spaghetti, 3.4, Groceries
# Продукт Potato уже есть в магазине
# Продукт Spaghetti уже есть в магазине
# Продукт Potato уже есть в магазине
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Как выглядит файл после запусков:
#
#
#
# Примечания:
# Не забывайте при записи в файл добавлять спец. символ перехода на следующую строку
# в конце - '\n'.
# При проверке на существование товара в методе add можно вызывать метод get_products
# для получения текущих продуктов.
# Не забывайте закрывать файл вызывая метод close() у объектов файла.

