class Cassa:  # Класс касса
    def __init__(self, products, date, price, productss=None):
        self.spicok = []
        if productss is not None:
            self.spicok.append(productss)
        self.products = products
        self.date = date
        if price < 0:
            raise ValueError("Цена не может быть < 0")
        self.price = price

    def append_tovar(self, tovar):  # добавляет продукты в список продуктов
        if type(tovar) != Products:
            raise TypeError("Неверный тип данных.")
        self.spicok.append(tovar)
        self.update_tovar()

    def delete_tovar(self, tovar):
        if type(tovar) != Products:
            raise TypeError(f"Неверный тип {tovar} вместо Products")

    def update_tovar(self):  # Изменяет цену
        self.price += len(self.spicok)
        print('Изменёнаная цена:', self.price)

    def __str__(self):  # Возврат информации о списке продуктов
        return f" {self.products} {self.date}, {self.price}, число товаров: {len(self.spicok)}"

    # Здесь и ниже операции сравнения >, >=, <, <=, ==, !=
    def __lt__(self, other):  # <
        self_kolvo, other_kolvo = (len(self.spicok), len(other.spicok))
        return self_kolvo < other_kolvo

    def __eq__(self, other):  # ==
        self_kolvo, other_kolvo = (len(self.spicok), len(other.spicok))
        return self_kolvo == other_kolvo

    def __le__(self, other):  # <=
        if self.__eq__(other):
            return True

        if self.__lt__(other):
            return True
        else:
            return False

    def __le__(self, other):  # <=
        if self.__eq__(other):
            return True

        if self.__lt__(other):
            return True
        else:
            return False


class Products:  # Класс товар
    def __init__(self, pricce, quantity, discount, measurements, products=None):
        self.products = []
        if products is not None:
            self.products.append(products)
        self.pricce = pricce
        self.quantity = quantity
        self.discount = discount
        self.measurements = measurements

    def print_products(self):  # добавляет товары в консоль
        for el in self.products:
            print(el)

    def append_products(self, title):  # Добавляет товары
        if type(title) != Products:
            raise TypeError("Неверный тип данных")
        self.title.append(title)

    def delete_products(self, title):
        if type(title) != Products:
            raise TypeError(f"Указан неверный тип {title} вместо Fish")
        if title in self.products:
            self.products.remove(title)
        print("Раба удалена.")

    def __str__(self):  # Возврат информации о товаре
        return f" {self.pricce}, {self.quantity},{self.discount},{self.measurements}"

    # Здесь и ниже операции сравнения >, >=, <, <=, ==, !=
    def __lt__(self, other):  # <
        self_price, other_price = (self.pricce, other.pricce)
        return self_price < other_price

    def __eq__(self, other):  # ==
        self_price, other_price = (self.pricce, other.pricce)
        return self_price == other_price

    def __le__(self, other):  # <=
        if self.__eq__(other):
            return True

        if self.__lt__(other):
            return True
        else:
            return False

    # Изменяем цены
    def increase_salary(self, summa):
        self.pricce += summa


#
if __name__ == "__main__":
    class1 = Products('Гречка', 110, 100, 34, 'кг')
    class2 = Products('Рис', 90, 110, 23, 'кг')
    class3 = Products('Сыр', 140, 120, 32, 'кг')
    class4 = Cassa('Гречка', '29.11.2022', 110, class1)
    class4.append_tovar(class3)
    class5 = Cassa('Рис', '30.11.2022', 90, class1)

    print('Сравнение по цене товара: ')
    print(class1 < class2)
    print(class1 == class2)
    print(class1 <= class2)
    print('Касса: ')
    print(class4)
    print(class1)
