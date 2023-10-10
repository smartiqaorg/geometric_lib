# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = (a*b*sin(ab))/2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Общее описание решения
В проекте *geometric_lib* представлены различные математический формулы для вычисления периметра и площади различных геометрических фигур, таких как:
* Круг (Circle)
* Прямоугольник (Rectangle)
* Квадрат (Square)
* Треугольник (Triangle)

Данный проект при помощи языка программирования **Python** позволяет при определенных входных данных вычислить площадь или периметр соответствующих фигур

## Описание работы функций файла *circle.py*
* **area(r)** - Функция нахождения площади круга: принимает число r, возвращает произведение квадрата r и числа pi. Пример вызова функции: **print(area(2))** ==> **12.566370614359172**
* **perimeter(r)** - Функция нахождения периметра круга: возвращает удвоенное произведение числа pi и r. Пример вызова функции: **print(perimeter(3))** ==> **18.84955592153876**

## Описание работы функций файла *rectangle.py*
* **area(a, b)** - Функция нахождения площади прямоугольника: принимает два числа a и b, возвращает произведение a и b. Пример вызова функции: **print(area(2, 5))** ==> **10**
* **perimeter(a, b)** - Функция нахождения периметра прямоугольника: принимает два числа a, b, возвращает удвоенную сумму чисел a и b. Пример вызова функции: **print(perimeter(4, 3))** ==> **14**

## Описание работы функций файла *square.py*
* **area(a)** - Функция нахождения плошади квадрата: принимает число a, возвращает квадрат числа a. Пример вызова функции: **print(area(3))** ==> **9**
* **perimeter(a)** - Функция нахождения периметра квадрата: принимает число a, возвращает произведение a и 4. Пример вызова функции: **print(perimeter(2))** ==> **8**

## Описание работы функций файла *triangle.py*
* **area(a, b, c)** - Функция нахождения плошади треугольника: принимает числа a, b - стороны треугольника, и c - угол между этими сторонами, возвращает половину произведения a, b и синуса угла c. Пример вызова функции: **print(area(2, 4, 30))** ==> **2**
* **perimeter(a, b, c)** - Функция нахождения периметра треугольника: принимает числа a, b, c - стороны треугольника, возвращает сумму a, b, c. Пример вызова функции: **print(perimeter(4, 3, 5))** ==> **12**

## История изменения проекта
commit 867b2ab9409b020161e149f4547be9e2e88607e2 (HEAD -> new_docs)
Author: Kseniiiiia <kseniia.pashkoff@gmail.com>
Date:   Tue Oct 10 18:42:56 2023 +0300

    Добавлена документация для файла triangle.py

commit 3d2defbc44ad6b9e80dfde068a2060349db67ba4
Author: Kseniiiiia <kseniia.pashkoff@gmail.com>
Date:   Tue Oct 10 18:42:01 2023 +0300

    Добавлена документация для файла square.py

commit 52828d86c4585b6c8fbb5197c6d1ef1aa47d910c
Author: Kseniiiiia <kseniia.pashkoff@gmail.com>
Date:   Tue Oct 10 18:41:20 2023 +0300

    Добавлена документация для файла rectangle.py

commit 0b49a5c6e9d15795fd5d9535c9cffb9656c576bb
Author: Kseniiiiia <kseniia.pashkoff@gmail.com>
Date:   Tue Oct 10 18:39:55 2023 +0300

    Добавлена документация для файла circle.py

commit 7980ba2bb82b412eda902c2ecdc055b1013a1ec0 (origin/new_features_409318, new, main)
Author: Kseniiiiia <kseniia.pashkoff@gmail.com>
Date:   Thu Sep 21 18:20:15 2023 +0300

    В файле rectangle.py исправлена ошибка

commit 2b374c509fdf145b6ecb0370208082a961ad1a01
Author: Kseniiiiia <kseniia.pashkoff@gmail.com>
Date:   Thu Sep 21 18:16:49 2023 +0300

    Добавлен новый файл triangle.py

commit 382378229fe16d4402b1c081acb026d4beb8b85c
Author: Kseniiiiia <kseniia.pashkoff@gmail.com>
Date:   Thu Sep 21 18:12:41 2023 +0300

    Добавлен новый файл

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added
(END)