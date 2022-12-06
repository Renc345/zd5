import datetime as DT


def str_to_date(self_date, other_date):
    dt1 = self_date.split(".")
    dt2 = other_date.split(".")
    self_bdate = DT.date(int(dt1[2]), int(dt1[1]), int(dt1[0]))
    other_bdate = DT.date(int(dt2[2]), int(dt2[1]), int(dt2[0]))
    return self_bdate, other_bdate


class Fish:
    def __init__(self, title, habitat_climate, price, Life_expectancy, what_they_eat, count_fish):
        self.title = title
        self.habitat_climate = habitat_climate
        if price < 0:
            raise ValueError("Цена не может быть < 0")
        self.price = price
        self.Life_expectancy = Life_expectancy
        if type(Life_expectancy) != int:
            raise TypeError("годы жизни рыбы должены быть числовыми")
        self.what_they_eat = what_they_eat
        self.count_fish = count_fish

    def __str__(self):
        return f"{self.title} {self.price} руб."

    def __lt__(self, other):  # <
        self_price, other_price = (self.price, other.price)
        return self_price < other_price

    def __eq__(self, other):  # ==
        self_price, other_price = (self.price, other.price)
        return self_price == other_price

    def __le__(self, other):  # <=
        if self.__eq__(other):
            return True

        if self.__lt__(other):
            return True
        else:
            return False


class Aquarium:
    def __init__(self, volume, shape, cleaning_date, fishes=None):
        self.volume = volume
        self.shape = shape
        self.cleaning_date = cleaning_date
        self.fishes = []
        if fishes is not None:
            self.fishes.append(fishes)

    def append_fish(self, fish):
        if type(fish) != Fish:
            raise TypeError("Неверный тип данных")
        self.fishes.append(fish)

    def delete_fish(self, fish):
        if type(fish) != Fish:
            raise TypeError(f"Указан неверный тип {fish} вместо Fish")
        if fish in self.fishes:
            self.fishes.remove(fish)
        print("Раба удалена.")

    def print_fishes(self):
        for f in self.fishes:
            print(f)

    def sale_fish(self, id):
        if id <= len(self.fishes) - 1:
            print("Рыбку:", self.fishes.pop(id), "продали")

    def __lt__(self, other):  # <
        self_count, other_count = (len(self.fishes), len(other.fishes))
        return self_count < other_count

    def __eq__(self, other):  # ==
        self_count, other_count = (len(self.fishes), len(other.fishes))
        return self_count == other_count

    def __le__(self, other):  # <=
        if self.__eq__(other):
            return True

        if self.__lt__(other):
            return True
        else:
            return False


if __name__ == "__main__":
    fish1 = Fish('Щука', 'Озера', 300, 30, 'черви', 15)
    fish2 = Fish('Пираньи', 'Реки', 1000, 20, 'растительная пища', 50)
    fish3 = Fish('Окунь', 'Озера', 200, 30, 'хлеб', 10)
    aq1 = Aquarium(50, 'Круглая', '21.03.2014', fish1)
    aq2 = Aquarium(100, 'Квадратная', '11.08.2017')
    aq3 = Aquarium(60, 'Треугольная', '19.04.2012')
    aq1.append_fish(fish2)
    aq1.print_fishes()
    # - Продажа рыбки
    # aq1.sale_fish(int(input("Укажите номер записи для продажи рыбки: ")))
    print(aq1 > aq2)

    # Сравним рыб по цене
    print('Сравним рыб по цене:')
    print(fish1 < fish2)
    print(fish2 > fish3)
    print(fish1 == fish3)
    print(fish2 <= fish3)
