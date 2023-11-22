import circle
import math


def test_circle_area():
    for i in range(len(test_input)):
        if circle.area(test_input[i]) == test_answers_area[i]:
            print(f"AREA TEST №{i + 1}")
            print(f"INPUT:  {test_input[i]}")
            print(f"TRUE: {circle.area(test_input[i])} = {test_answers_area[i]}\n")
        else:
            print(f"AREA TEST №{i + 1}")
            print(f"INPUT: {test_input[i]}")
            print(f"FALSE: {circle.area(test_input[i])} != {test_answers_area[i]}\n")


def test_circle_perimeter():
    for i in range(len(test_input)):
        if circle.perimeter(test_input[i]) == test_answers_perimeter[i]:
            print(f"PERIMETER TEST №{i + 1}")
            print(f"INPUT:  {test_input[i]}")
            print(f"TRUE: {circle.perimeter(test_input[i])} = {test_answers_perimeter[i]}\n")
        else:
            print(f"PRIMETER TEST №{i + 1}")
            print(f"INPUT: {test_input[i]}")
            print(f"FALSE: {circle.perimeter(test_input[i])} != {test_answers_perimeter[i]}\n")


'''
    Данные для проверки площади и периметра [r]:
        r - радиус окружности
                                                '''

test_input = [4, 8, 15, 34]
test_answers_area = [50.26548245743669, 201.06192982974676, 706.8583470577034, 3631.6811075498013]
test_answers_perimeter = [25.132741228718345, 50.26548245743669, 94.24777960769379, 213.62830044410595]

test_circle_area()
test_circle_perimeter()