import triangle


def test_triangle_area():
    for i in range(len(test_input_area)):

        if test_input_area[i][0] < 0 or test_input_area[i][1] < 0:
            print(f"AREA TEST №{i + 1}: invalid value entered\n")

        elif triangle.area(test_input_area[i][0], test_input_area[i][1]) == test_answers_area[i] and test_input_area[i][0] >= 0 and test_input_area[i][1] >= 0:
            print(f"AREA TEST №{i + 1}: correct\n")

        else:
            print(f"AREA TEST №{i + 1}: calculation error\n")



def test_triangle_perimeter():
    for i in range(len(test_input_perimeter)):

        if test_input_perimeter[i][0] <= 0 or test_input_perimeter[i][1] <= 0 or test_input_perimeter[i][2] <= 0:
            print(f"PERIMETER TEST №{i + 1}: invalid value entered\n")

        elif triangle.perimeter(test_input_perimeter[i][0], test_input_perimeter[i][1], test_input_perimeter[i][2]) == test_answers_perimeter[i]:
            print(f"PERIMETER TEST №{i + 1}: correct\n")

        else:
            print(f"PERIMETER TEST №{i + 1}: calculation error\n")


'''
    Данные для проверки площади test_input_area[a, h]:
        a - длина стороны треугольника
        h - длина высоты треугольника
                                                        '''

test_input_area = [[3, 6], [-7, 12], [3.5, 6.8], [12.1, 8]]
test_answers_area = [9.0, "error", 11.9, 48.4]


'''
    Данные для проверки периметра test_input_perimeter[a, b, c]:
        a, b, c - длины сторон треугольника
                                                                '''

test_input_perimeter = [[4, 3, 5], [-12, 4, 8], [0, 98, 0], [9.766, 16, 9.01]]
test_answers_perimeter = [12, "error", "error", 34.775999999999996]


test_triangle_area()
test_triangle_perimeter()