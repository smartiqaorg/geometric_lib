import square

def test_square_area():
    for i in range(len(test_input_area)):
        if square.area(test_input_area[i]) == test_answers_area[i]:
            print(f"AREA TEST №{i + 1}")
            print(f"INPUT:  {test_input_area[i]}")
            print(f"TRUE: {test_answers_area[i]} = {test_answers_area[i]}\n")
        else:
            print(f"AREA TEST №{i + 1}")
            print(f"INPUT: {test_input_area[i]}")
            print(f"FALSE: {square.area(test_input_area[i])} != {test_answers_area[i]}\n")


def test_square_perimeter():
    for i in range(len(test_input_perimeter)):
        if square.perimeter(test_input_perimeter[i]) == test_answers_perimeter[i]:
            print(f"PERIMETER TEST №{i + 1}")
            print(f"INPUT:  {test_input_perimeter[i]}")
            print(f"TRUE: {test_answers_perimeter[i]} = {test_answers_perimeter[i]}\n")
        else:
            print(f"PERIMETER TEST №{i + 1}")
            print(f"INPUT: {test_input_perimeter[i]}")
            print(f"FALSE: {square.perimeter(test_input_perimeter[i])} != {test_answers_perimeter[i]}\n")



'''
    Данные для проверки площади и периметра [a]:
        a - длина стороны квадрата
'''

test_input_area = [3, 99, 16, 79.5]
test_answers_area = [9, 9801, 256, 6320.25]

test_input_perimeter = [4, 6, 8.8, 90]
test_answers_perimeter = [16, 24, 35.2, 361]

test_square_area()
test_square_perimeter()