import rectangle


def test_rectangle_area():
    for i in range(len(test_input)):
        if rectangle.area(test_input[i][0], test_input[i][1]) == test_answers_area[i]:
            print(f"AREA TEST №{i + 1}")
            print(f"INPUT:  {test_input[i][0]} {test_input[i][1]}")
            print(f"TRUE: {test_answers_area[i]} = {test_answers_area[i]}\n")
        else:
            print(f"AREA TEST №{i + 1}")
            print(f"INPUT: {test_input[i][0]} {test_input[i][1]}")
            print(f"FALSE: {rectangle.area(test_input[i][0], test_input[i][1])} != {test_answers_area[i]}\n")


def test_rectangle_perimeter():
    for i in range(len(test_input)):
        if rectangle.perimeter(test_input[i][0], test_input[i][1]) == test_answers_perimeter[i]:
            print(f"PERIMETER TEST №{i + 1}")
            print(f"INPUT:  {test_input[i][0]} {test_input[i][1]}")
            print(f"TRUE: {test_answers_perimeter[i]} = {test_answers_perimeter[i]}\n")
        else:
            print(f"PERIMETER TEST №{i + 1}")
            print(f"INPUT: {test_input[i][0]} {test_input[i][1]}")
            print(f"FALSE: {rectangle.perimeter(test_input[i][0], test_input[i][1])} != {test_answers_perimeter[i]}\n")


'''
    Данные для проверки площади и периметра [a, b]:
        a - длины двух сторон 
        b - длина двух сторон
                                                    '''

test_input = [[5, 7], [8, 13], [1, 3]]
test_answers_area = [35, 104, 3]
test_answers_perimeter = [24, 34, 8]

test_rectangle_area()
test_rectangle_perimeter()