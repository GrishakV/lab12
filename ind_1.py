#!/usr/bin/env python3
# -*- config: utf-8 -*-

# 13. Создать класс Goods (товар). В классе должны быть представлены поля: на именование
# товара, дата оформления, цена товара, количество единиц товара, номер накладной, по
# которой товар поступил на склад. Реализовать методы изменения цены товара, изменения
# количества товара (увеличения и умень шения), вычисления стоимости товара.


class Goods:

    def __init__(self, name=' ', date=' ', price=0, num=0, waybill=' '):
        price = int(price)
        num = int(num)

        self.__name = name
        self.__date = date
        self.__price = abs(price)
        self.__num = abs(num)
        self.__waybill = waybill

    @property
    def name(self):
        return self.__name

    @property
    def date(self):
        return self.__date

    @property
    def price(self):
        return self.__price

    @property
    def num(self):
        return self.__num

    @property
    def waybill(self):
        return self.__waybill

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(str, line.split(',', maxsplit=5)))

        self.__name = parts[0]
        self.__date = parts[1]
        self.__price = abs(int(parts[2]))
        self.__num = abs(int(parts[3]))
        self.__waybill = parts[4]

    def display(self):
        print(
            f"Наименование товара: {self.__name}\n"
            f"Дата оформления: {self.__date}\n"
            f"Цена товара: {self.__price}\n"
            f"Количество едениц товара: {self.__num}\n"
            f"Номер накладной: {self.__waybill}\n"
        )

    def price_add(self, new):
        if isinstance(new, Goods):
            price = self.price + new.price

            return Goods(name=self.__name, date=self.__date, price=price, num=self.__num, waybill=self.waybill)
        else:
            raise ValueError()

    def price_sub(self, new):
        if isinstance(new, Goods):
            price = self.price - new.price

            return Goods(name=self.__name, date=self.__date, price=price, num=self.__num, waybill=self.waybill)
        else:
            raise ValueError()

    def num_add(self, new):
        if isinstance(new, Goods):
            num = self.num + new.num

            return Goods(name=self.__name, date=self.__date, price=self.__price, num=num, waybill=self.waybill)
        else:
            raise ValueError()

    def num_sub(self, new):
        if isinstance(new, Goods):
            num = self.num - new.num

            return Goods(name=self.__name, date=self.__date, price=self.__price, num=num, waybill=self.waybill)
        else:
            raise ValueError()

    def total(self, new):
        if isinstance(new, Goods):
            old_total = self.price * self.num
            new_total = new.price * new.num

            return old_total, new_total
        else:
            raise ValueError()


if __name__ == '__main__':
    a1 = Goods("Товар", "дата", 1000, 5, "накладная")
    a1.display()

    a2 = Goods()
    a2.read("Введите новые данные через запятую: ")
    a2.display()

    a3 = a2.price_add(a1)
    a3.display()

    a4 = a2.price_sub(a1)
    a4.display()

    a5 = a2.num_add(a1)
    a5.display()

    a6 = a2.num_sub(a1)
    a6.display()

    a7 = a2.total(a1)
    print(f"Новая сумма = {a7[0]}, Старая сумма = {a7[1]}")
