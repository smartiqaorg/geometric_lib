from circle import area, perimeter
from TEST_DATA import TEST_CIRCLE_AREA_DATA, TEST_CIRCLE_PERIMETER_DATA


"""Тестирование Area"""
print("_______ПЛОЩАДЬ_______\n")
for test_data in TEST_CIRCLE_AREA_DATA:
    radius = test_data[0]
    expected_result = test_data[1]

    if round(area(radius), 2) == expected_result:
        print(f"Успешно!\nВходные данные: {radius}\nВыходные данные: {expected_result}\n")

    else:
        print(f"Неудачно!\nВходные данные: {radius}\nОжидалось: {expected_result}\nВыходные данные: {round(area(radius), 2)}\n")


"""Тестирование Perimeter"""
print("_______ПЕРИМЕТР_______\n")
for test_data in TEST_CIRCLE_PERIMETER_DATA:
    radius = test_data[0]
    expected_result = test_data[1]

    if round(perimeter(radius), 2) == expected_result:
        print(f"Успешно!\nВходные данные: {radius}\nВыходные данные: {expected_result}\n")
    else:
        print(f"Неудачно!\nВходные данные: {radius}\nОжидалось: {expected_result}\nВыходные данные: {round(perimeter(radius), 2)}\n")