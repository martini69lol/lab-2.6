# создайте словарь, связав его с переменной school , и наполните данными,
# которые бы отражали количество учащихся в разных классах (1а, 1б, 2б, 6а, 7в и т. п.).
# Внесите изменения в словарь согласно следующему: а) в одном из классов изменилось
# количество учащихся, б) в школе появился новый класс, с) в школе был расформирован
# (удален) другой класс. Вычислите общее количество учащихся в школе.

SCHOOL = {
    '1а': 22,
    '1б': 15,
    '6а': 16,
    '7в': 20,
    '6б': 14,
    '5в': 14
}


def changes_class(class_school, quantity):
    SCHOOL.update(
        {
            class_school: quantity
        }
    )


def new_class(class_name, quantity):
    SCHOOL.update(
        {
            class_name: quantity
        }
    )


def disbanded_class(class_name):
    SCHOOL.pop(class_name)


def quantity_in_school():
    result = 0
    for v in SCHOOL.values():
        result += v

    return result

