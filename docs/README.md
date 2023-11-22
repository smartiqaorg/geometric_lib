# Общее описание решений
## Проект состоит из следующих файлов
- circle.py
- rectangle.py
- square.py
- triangle.py

# Описание функций
## Circle.py
### Area
- **S = πR²**
- Функция принимает число r - радиус круга
- Возвращает площадь круга
- ***Пример: v = 5, area(v) = 78.53981633974483***

### Perimeter
- **P = 2πR**
- Функция принимает число r - радиус круга
- Возвращает периметр круга
- ***Пример: v = 5, perimetr(v) = 31.41592653589793***


## Rectangle.py
### Area
- **S = ab**
- Функция принимает числа a и b - смежные стороны прямоугольника
- Возвращает площадь прямоугольника
- ***Пример: v = 5, m = 6, area(v, m) = 30***

### Perimeter
- **P = 2a + 2b**
- Функция принимает числа a и b - смежные стороны прямоугольника
- Возвращает периметр прямоугольника
- ***Пример: v = 5, m = 6, perimetr(v, m) = 22***


## Square.py
### Area
- **S = a²**
- Функция принимает число a - сторона квадрата
- Возвращает площадь квадрата
- ***Пример: v = 5, area(v) = 25***

### Perimeter
- **P = 4a**
- Функция принимает число a - сторона квадрата
- Возвращает периметр квадрата
- ***Пример: v = 5, perimetr(v) = 20***


## Triangle.py
### Area
- **Triangle: S = ah / 2**
- Функция принимает числа a и h - основание и высота треугольника
- Возвращает площадь треугольника
- ***Пример: v = 5, m = 3, area(v, m) = 7.5***

### Perimeter
- **P = a + b + c**
- Функция принимает числа a, b, c - стороны треугольника
- Возвращает периметр треугольника
- ***Пример: v = 5, m = 4, d = 2, perimetr(v, m, d) = 11***

# History of commits
commit f34f434e655451c66430908a9dc514de6d6ed565 (HEAD -> test, origin/main, origin/HEAD, main)
Author: wox-ty <korogu05@gmail.com>
Date:   Wed Sep 13 14:24:46 2023 +0300

>    fixed mistake in rectangle.py

commit 2240dfa703a7fe7c8795189eb654a0c8ee74acfd
Author: wox-ty <korogu05@gmail.com>
Date:   Wed Sep 13 14:23:45 2023 +0300

>   added triangle.py

commit 12d2050b86baf1aade659d1689155f5eb2888aa4
Author: wox-ty <korogu05@gmail.com>
Date:   Wed Sep 13 14:22:08 2023 +0300

>    added rectangle.py

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

>    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

>    L-03: Circle and square added
