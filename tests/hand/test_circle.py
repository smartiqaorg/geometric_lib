import circle


def test_circle_area():
    for i in range(len(test_input)):
        if test_input[i] < 0:
            print(f"AREA TEST №{i + 1}: invalid value entered\n")

        if circle.area(test_input[i]) == test_answers_area[i] and test_input[i] >= 0:
            print(f"AREA TEST №{i + 1}: correct\n")

        elif circle.area(test_input[i]) != test_answers_area[i] and test_input[i] >= 0:
            print(f"AREA TEST №{i + 1}: calculation error\n")



def test_circle_perimeter():
    for i in range(len(test_input)):

        if test_input[i] < 0:
            print(f"PERIMETER TEST №{i + 1}: invalid value entered\n")

        elif circle.perimeter(test_input[i]) == test_answers_perimeter[i] and test_input[i] >= 0:
            print(f"PERIMETER TEST №{i + 1}: correct\n")

        elif circle.perimeter(test_input[i]) != test_answers_perimeter[i] and test_input[i] >= 0:
            print(f"PRIMETER TEST №{i + 1}: calculation error\n")



'''
    Данные для проверки площади и периметра test_input = [r]:
        r - радиус окружности
                                                '''

test_input = [8, 9.31, -15, 0]
test_answers_area = [201.06192982974676, 272.30099900181426, "error", 0.0]
test_answers_perimeter = [50.26548245743669, 58.49645520984195, "error", 0.0]

test_circle_area()
test_circle_perimeter()