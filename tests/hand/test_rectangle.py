import rectangle


def test_rectangle_area():
    for i in range(len(test_input)):

        if test_input[i][0] < 0 or test_input[i][1] < 0:
            print(f"AREA TEST №{i + 1}: invalid value entered\n")

        elif rectangle.area(test_input[i][0], test_input[i][1]) == test_answers_area[i]:
            print(f"AREA TEST №{i + 1}: correct\n")

        else:
            print(f"AREA TEST №{i + 1}: calculation error\n")


def test_rectangle_perimeter():
    for i in range(len(test_input)):

        if test_input[i][0] <= 0 or test_input[i][1] <= 0:
            print(f"AREA TEST №{i + 1}: invalid value entered\n")

        elif rectangle.perimeter(test_input[i][0], test_input[i][1]) == test_answers_perimeter[i]:
            print(f"PERIMETER TEST №{i + 1}: correct\n")

        else:
            print(f"PERIMETER TEST №{i + 1}: calculation error\n")


'''
    Данные для проверки площади и периметра [a, b]:
        a - длины двух сторон 
        b - длина двух сторон
                                                    '''

test_input = [[5, -7], [8, 13.5], [1, 3], [0, 89]]
test_answers_area = ["error", 108.0, 3, 0]
test_answers_perimeter = [24, 43.0, 8, 0]

test_rectangle_area()
test_rectangle_perimeter()
