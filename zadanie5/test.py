import pytest

from module_employee import Fish, Aquarium


# Проверка на отрицательную цену
def test_wrong_price():
    with pytest.raises(ValueError):
        fish_1 = Fish("Щука", "Озёра", -300, 30, "черви", 15)


# Проверка на увелечение цены
def test_increase_price():
    fish_1 = Fish("Щука", "Озёра", 300, 30, "черви", 15)
    fish_1.price += 100
    assert fish_1.price == 400


# Проверка при добавлении рыбы. (неверный тип)
def test_wrong_type_Fish():
    with pytest.raises(TypeError):
        fish_1 = Fish('Щука', 'Озера', '300', '30', 'черви', '15')
        aq2 = Aquarium('100', 'Квадратная', '11.08.2017')
        aq2.append_fish("Щука")


# Сравниваем двух рыб по цене
def test_employees_lt():
    fish_1 = Fish("Щука", "Озёра", 300, 30, "черви", 15)
    fish_2 = Fish("Пираньи", "Реки", 1000, 20, "растительная пища", 50)
    assert (fish_1 < fish_2) == True


# Проверка при добавлении рыбы (добавтли правильно)
def test_append_Fish():
    fish_1 = Fish("Щука", "Озёра", 300, 30, "черви", 15)
    aq1 = Aquarium('100', 'Квадратная', '11.08.2017')
    count_before = len(aq1.fishes)
    aq1.append_fish(fish_1)
    assert count_before == len(aq1.fishes) - 1


# Сравниваем двух аквариумов по объему
def test_employees_lot():
    class1 = Products('Гречка', 110, 100, 34, 'кг')
    class2 = Products('Рис', 90, 110, 23, 'кг')
    assert (aq1 > aq2) == False


# Проверка на числовые годы жизни
def test_wrong_type_Employee():
    with pytest.raises(TypeError):
        fish_1 = Fish("Щука", "Озёра", 300, 'аава', "черви", 15)


# Увелечиние объема
def test_increase_volume():
    aq1 = Aquarium(100, 'Квадратная', '11.08.2017')
    aq1.volume += 50
    assert aq1.volume == 150


# Увелечение срока жизни рыбы
def test_increase_volume1():
    fish_3 = Fish('Окунь', 'Озера', 200, 30, 'хлеб', 10)
    fish_3.Life_expectancy += 2
    assert fish_3.Life_expectancy == 32


#Удаление рыбы
def test_delete_fish():
    with pytest.raises(TypeError):
        aq1 = Aquarium(100, 'Квадратная', '11.08.2017')
        fish_1 = Fish('Окунь', 'Озера', 200, 30, 'хлеб', 10)
        fish_2 = Fish("Щука", "Озёра", 300, 20, "черви", 15)
        aq1.append_fish(fish_1)
        aq1.append_fish(fish_2)
        aq1.delete_fish("Окунь")
