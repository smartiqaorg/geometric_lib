from rectangle import area, perimeter
from tests.unittest.TEST_DATA import TEST_RECTANGLE_AREA_DATA, TEST_RECTANGLE_PERIMETER_DATA

"""_______ПЛОЩАДЬ_______\n"""
for test_data in TEST_RECTANGLE_AREA_DATA:
    side_a = test_data[0]
    side_b = test_data[1]
    expected_result = test_data[2]

    if round(area(side_a, side_b), 2) == expected_result:
        print(f"Успешно!\nВходные данные: сторона a = {side_a}, сторона b = {side_b}\nВыходные данные: {expected_result}\n")
    else:
        print(f"Неудачно!\nВходные данные: сторона a = {side_a}, сторона b = {side_b}\nОжидалось: {expected_result}\nВыходные данные: {round(area(side_a, side_b), 2)}\n")

"""_______ПЕРИМЕТР_______\n"""
for test_data in TEST_RECTANGLE_PERIMETER_DATA:
    side_a = test_data[0]
    side_b = test_data[1]
    expected_result = test_data[2]

    if round(perimeter(side_a, side_b), 2) == expected_result:
        print(f"Успешно!\nВходные данные: сторона a = {side_a}, сторона b = {side_b}\nВыходные данные: {expected_result}\n")
    else:
        print(f"Неудачно!\nВходные данные: сторона a = {side_a}, сторона b = {side_b}\nОжидалось: {expected_result}\nВыходные данные: {round(perimeter(side_a, side_b), 2)}\n")