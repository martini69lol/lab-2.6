#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    school = {'1а': 25, '1б': 27, '2б': 29, '6а': 22, '7в': 30}

    # Изменяем количество учеников в классе
    school['1б'] = 28

    # Добавляем новый класс
    school['7а'] = 25

    # Удаляем класс
    del school['6а']

    # Вычисляем общее количество учащихся в школе
    total_students = sum(school.values())

    print(school)
    print("Общее количество учащихся в школе:", total_students)
