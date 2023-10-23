from square import area, perimeter
from tests.unittest.TEST_DATA import TEST_SQUARE_AREA_DATA, TEST_SQUARE_PERIMETER_DATA


print("_______ПЛОЩАДЬ_______")
for test_data in TEST_SQUARE_AREA_DATA:
    side_a = test_data[0]
    expected_result = test_data[1]

    if round(area(side_a),2) == expected_result:
        print(f"Успешно!\nВходные данные: сторона a = {side_a}\nОжидалось: {expected_result}\n")
    else:
        print(f"Неудачно!\nВходные данные: сторона a = {side_a}\nОжидалось: {expected_result}\nВыходные данные: {round(area(side_a),2)}\n")

print("_______ПЕРИМЕТР_______")
for test_data in TEST_SQUARE_PERIMETER_DATA:
    side_a = test_data[0]
    expected_result = test_data[1]

    if round(perimeter(side_a),2) == expected_result:
        print(f"Успешно!\nВходные данные: сторона a = {side_a}\nОжидалось: {expected_result}\n")
    else:
        print(f"Неудачно!\nВходные данные: сторона a = {side_a}\nОжидалось: {expected_result}\nВыходные данные: {round(perimeter(side_a),2)}\n")