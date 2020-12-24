#!/usr/bin/env python3
# -*- config: utf-8 -*-


class Pair:
    def __init__(self, a=0, b=1):
        a = int(a)
        b = int(b)

        self.__first = abs(a)
        self.__second = abs(b)

    @property
    def first(self):
        return self.__first

    @property
    def second(self):
        return self.__second

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(int, line.split(',', maxsplit=1)))

        self.__first = abs(parts[0])
        self.__second = abs(parts[1])

    def display(self):
        print(f"{self.__first}, {self.__second}")

    def mul(self, new):
        if isinstance(new, Pair):
            a = self.first * new.first
            b = self.second * new.second

            return Pair(a, b)
        else:
            raise ValueError()

    def add(self, new):
        if isinstance(new, Pair):
            a = self.first + new.first
            b = self.second + new.second

            return Pair(a, b)
        else:
            raise ValueError()


class Money(Pair):
    def __init__(self, a, b):
        super().__init__(a)
        super().__init__(b)
        self.__rub = a
        self.__penny = b

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(int, line.split(',', maxsplit=1)))

        self.__rub = abs(parts[0])
        self.__penny = abs(parts[1])

    def display(self):
        print(f"{self.__rub}, {self.__penny}")

    def mul(self, new):
        if isinstance(new, Money):
            rub = self.rub * new.rub
            penny = self.penny * new.penny

            return Money(rub, penny)
        else:
            raise ValueError()

    def add(self, new):
        if isinstance(new, Money):
            rub = self.rub + new.rub
            penny = self.penny + new.penny

            return Money(rub, penny)
        else:
            raise ValueError()


if __name__ == '__main__':
    p1 = Pair(1, 2)
    p1.display()

    p2 = Pair()
    p2.read("Введите пару чисел через запятую: ")
    p2.display()

    p3 = p2.add(p1)
    p3.display()

    p4 = p2.mul(p1)
    p4.display()

    m1 = Money(2, 6)
    m1.display()

    m2 = Money()
    m2.read("Введите рубли и копейки через запятую: ")
    m2.display()

    m3 = m2.add(m1)
    m3.display()

    m4 = m2.mul(m1)
    m4.display()
