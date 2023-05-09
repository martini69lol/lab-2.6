#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Создание исходного словаря
    slov = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

    # Применение метода items() к исходному словарю
    listt = slov.items()

    # Создание нового словаря, "обратного" исходному
    result = {i: k for k, i in listt}

    # Вывод исходного и результирующего словарей
    print("Исходный словарь:", slov)
    print("Результирующий словарь:", result)
