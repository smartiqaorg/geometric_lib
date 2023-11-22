import triangle


def test_triangle_area():
    for i in range(len(test_input_area)):
        if triangle.area(test_input_area[i][0], test_input_area[i][1]) == test_answers_area[i]:
            print(f"AREA TEST №{i + 1}")
            print(f"INPUT:  {test_input_area[i][0]} {test_input_area[i][1]}")
            print(f"TRUE: {test_answers_area[i]} = {test_answers_area[i]}\n")
        else:
            print(f"AREA TEST №{i + 1}")
            print(f"INPUT: {test_input_area[i][0]} {test_input_area[i][1]}")
            print(f"FALSE: {triangle.area(test_input_area[i][0], test_input_area[i][1])} != {test_answers_area[i]}\n")


def test_triangle_perimeter():
    for i in range(len(test_input_perimeter)):
        if triangle.perimeter(test_input_perimeter[i][0], test_input_perimeter[i][1], test_input_perimeter[i][2]) == \
            test_answers_perimeter[i]:
            print(f"PERIMETER TEST №{i + 1}")
            print(f"INPUT: {test_input_perimeter[i][0]} {test_input_perimeter[i][1]} {test_input_perimeter[i][2]}")
            print(f"TRUE: {test_answers_perimeter[i]} = {test_answers_perimeter[i]}\n")
        else:
            print(f"PERIMETER TEST №{i + 1}")
            print(f"INPUT: {test_input_perimeter[i][0]} {test_input_perimeter[i][1]} {test_input_perimeter[i][2]}")
            print(f"FALSE: {triangle.perimeter(test_input_perimeter[i][0], test_input_perimeter[i][1], test_input_perimeter[i][2])} != {test_answers_perimeter[i]}\n")

'''
    Данные для проверки площади [a, h]:
        a - длина стороны треугольника
        h - длина высоты треугольника
                                        '''

test_input_area = [[3, 6], [7, 12], [3, 4], [12, 8]]
test_answers_area = [9, 42, 6, 48]


'''
    Данные для проверки периметра [a, b, c]:
        a, b, c - длины сторон треугольника
                                                '''

test_input_perimeter = [[3, 4, 5], [45, 38, 59], [2, 4, 3.12], [12.2, 15, 14.8]]
test_answers_perimeter = [12, 142, 9.21, 42]


test_triangle_area()
test_triangle_perimeter()