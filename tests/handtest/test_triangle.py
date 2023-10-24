from triangle import area, perimeter
from tests.unittest.TEST_DATA import TEST_TRIANGLE_AREA_DATA, TEST_TRIANGLE_PERIMETER_DATA


print("_______ПЛОЩАДЬ_______")
for test_data in TEST_TRIANGLE_AREA_DATA:
    side_a = test_data[0]
    height = test_data[1]
    expected_result = test_data[2]

    if round(area(side_a, height), 2) == expected_result:
        print(f"Успешно!\nВходные данные: сторона a = {side_a}, высота = {height}\nОжидалось: {expected_result}\n")
    else:
        print(f"Неудачно!\nВходные данные: сторона a = {side_a}, высота = {height}\nОжидалось: {expected_result}\nВыходные данные: {round(area(side_a, height), 2)}\n")

print("_______ПЕРИМЕТР_______")
for test_data in TEST_TRIANGLE_PERIMETER_DATA:
    side_a = test_data[0]
    side_b = test_data[1]
    side_c = test_data[2]
    expected_result = test_data[3]

    if round(perimeter(side_a, side_b, side_c), 2) == expected_result:
        print(f"Успешно!\nВходные данные: сторона a = {side_a}, сторона b = {side_b}, сторона c = {side_c}\nОжидалось: {expected_result}\n")
    else:
        print(f"Неудачно!\nВходные данные: сторона a = {side_a}, сторона b = {side_b}, сторона c = {side_c}\nОжидалось: {expected_result}\nВыходные данные: {round(perimeter(side_a, side_b, side_c), 2)}\n")