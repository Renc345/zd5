from PRODUCT import Cassa, Products
import pytest


# Проверка на отрицательную цену
def test_wrong_price():
    with pytest.raises(ValueError):
        class5 = Cassa('Рис', '30.11.2022', -90)


# Проверка на увелечение цены
def test_increase_price():
    class1 = Products(110, 'Гречка', 100, 34, 'кг')
    class1.pricce += 100
    assert class1.pricce == 210


# Проверка при добавлении рыбы. (неверный тип)
def test_wrong_type_Fish():
    with pytest.raises(TypeError):
        class1 = Products('Гречка', 110, 100, 34, 'кг')
        class4 = Cassa('Гречка', '29.11.2022', 110)
        class4.append_tovar("Гречка")


# Сравниваем двух рыб по цене
def test_employees_lt():
    class2 = Products('Рис', 90, 110, 23, 'кг')
    class3 = Products('Сыр', 140, 120, 32, 'кг')
    assert (class2 < class3) == True


# Проверка при добавлении рыбы (добавтли правильно)
def test_append_Fish():
    class3 = Products('Сыр', 140, 120, 32, 'кг')
    class4 = Cassa('Гречка', '29.11.2022', 110)
    count_before = len(class4.spicok)
    class4.append_tovar(class3)
    assert count_before == len(class4.spicok) - 1


# Сравниваем двух аквариумов по объему
def test_employees_lot():
    class4 = Cassa('Гречка', '29.11.2022', 110)
    class5 = Cassa('Рис', '30.11.2022', 90)
    assert (class4 > class5) == False


# Сравниваем двух аквариумов по объему
def test_employees_lot():
    class1 = Products('Гречка', 110, 100, 34, 'кг')
    class2 = Products('Рис', 90, 110, 23, 'кг')
    assert (class1 < class2) == True


# Увелечиние объема
def test_increase_volume():
    class4 = Cassa('Гречка', '29.11.2022', 110)
    class4.price += 50
    assert class4.price == 160


# 4 3
def test_increase_volume1():
    class1 = Products('Гречка', 110, 100, 34, 'кг')
    class1.quantity += 2
    assert class1.quantity == 112



# Удаление рыбы
def test_delete_fish():
    class5 = Cassa('Рис', '30.11.2022', 90)
    class1 = Products('Гречка', 110, 100, 34, 'кг')
    class2 = Products('Рис', 90, 110, 23, 'кг')
    class5.append_tovar(class1)
    class5.append_tovar(class2)
    with pytest.raises(TypeError):
        class5.delete_tovar("Гречка")

