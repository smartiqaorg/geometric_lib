import square

def test_square_area():
    for i in range(len(test_input)):

        if test_input[i] < 0:
            print(f"AREA TEST №{i + 1}: invalid value entered\n")

        elif square.area(test_input[i]) == test_answers_area[i] and test_input[i] >= 0:
            print(f"AREA TEST №{i + 1}: correct\n")

        else:
            print(f"AREA TEST №{i + 1}: calculation error\n")



def test_square_perimeter():
    for i in range(len(test_input)):

        if test_input[i] < 0:
            print(f"PERIMETER TEST №{i + 1}: invalid value entered\n")

        elif square.perimeter(test_input[i]) == test_answers_perimeter[i] and test_input[i] >= 0:
            print(f"PERIMETER TEST №{i + 1}: correct\n")

        else:
            print(f"PERIMETER TEST №{i + 1}: calculation error\n")




'''
    Данные для проверки площади и периметра test_input[a]:
        a - длина стороны квадрата
'''

test_input = [3, -99, 16.77, 0]

test_answers_area = [9, "error", 281.2329, 0]
test_answers_perimeter = [12, "error", 67.08, 0]

test_square_area()
test_square_perimeter()
