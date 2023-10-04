# Documentation

## Math formulas

### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = (ah)/2

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Общее описание решения
Решение состоит из трех этапов:
1. Функция получает число(числа), которые являются длиной тех или иных элементов фигуры.
2. С полученным числом(числами) выполняются математические операции согласно формулам, с помощью которых вычисляется площадь или периметр фигуры.
3. Программа возвращает результат вычислений.

## Описание каждой функции с примерами вызовов

***Программа***

### circle.py

```python

import math
''' Модуль math предоставляет обширный функционал для работы с числами '''

def area(r):
    ''' число r принимает значение радиуса круга
        функция возвращает r в квадрате, умноженное на число pi, т.е. площадь круга'''
    return math.pi * r * r


def perimeter(r):
    ''' число r принимает значение радиуса круга
      git   функция возвращает удвоенное произведение радиуса круга (r) на число pi, т.е. периметр круга '''
    return 2 * math.pi * r
```

***Пример вызова***

```python
r = 6
print("Area = ", area(r))
print("Perimeter = ", perimeter(r))
```

```markdown
*input:* r = 6
*output:* Area:=113.04 Perimeter:=37.699104
```

### rectangle.py

***Программа***

```python
def area(a, b):
    ''' переменные a и b принимают значения сторон прямоугольника
        функция возвращает произведение a и b, т.е. площадь прямоугольника'''
    return a * b

def perimeter(a, b):
    ''' переменные a и b принимают значения сторон прямоугольника
        функция возвращает удвоенную сумму a и b, т.е. периметр прямоугольника'''
    return 2*(a + b)
```

***Пример вызова***

```python 
a = 5
b = 6
print("Area = ", area(a, b))
print("Perimeter = ", perimeter(a, b))
```

```markdown
*input:* 
a = 5
b = 6
*output:*
Area = 30
Perimeter = 22
```

### square.py

***Программа***

```python

def area(a):
    ''' переменная a принимает значение стороны квадрата
        функция возвращает a в квадрате, т.е. плозадь квадрата'''
    return a * a


def perimeter(a):
    ''' переменная а принимает значение стороны квадрата
        функция возвращает a, умноженное на 4, т.е. периметр квадрата'''
    return 4 * a
```

***Пример вызова***

```python
a = 9
print("Area = ", area(a))
print("Perimeter = ", perimeter(a))
```

```markdown
*input:* 
a = 9
*output:* 
Area = 36 
Perimeter = 24
```

### triangle.py

***Программа***

```python
def area(a, h):
    '''переменные a и h принимают занчения второны и высоты треугольника
        функция возвращает произведение a и h, деленное на 2, т.е. площадь треугольника'''
    return a * h / 2

def perimeter(a, b, c):
    ''' переменные a,b и c принимают значение сторон треугольника
    Возвращает сумму a,b и c, т.е. периметр треугольника'''
    return a + b + c 
```
***Пример вызова***

```python
a = 3
b = 4
c = 5
h = 4
print("Area = ", area(a, h))
print("Perimeter = ", perimeter(a, b, c))
```

```markdown
*input:* 
a = 3
b = 4
c = 5
h = 4
*output:*
Area = 6
Perimeter = 12
```

## история изменения проекта с хэшами коммитов

commit e0a536566922b2a67e87ddaf2049e40ad983c1dc
Author: ssandaa <oziniek.art@mail.ru>
Date:   Wed Oct 4 01:26:11 2023 +0300

    general description of the solution

commit 2c39fd30c9555c78603d18ac59a538b53b8e53d3
Author: ssandaa <oziniek.art@mail.ru>
Date:   Wed Oct 4 00:33:00 2023 +0300

    added documentation to triangle.py

commit 623b387b9c99d44620d5314d47923c03cf4c9e0a
Author: ssandaa <oziniek.art@mail.ru>
Date:   Wed Oct 4 00:32:11 2023 +0300

    added documentation to square.py

commit c1485d6e8f6cd831a3298019962efaf3f0960fb3
Author: ssandaa <oziniek.art@mail.ru>
Date:   Wed Oct 4 00:30:44 2023 +0300

    added documentation to rectangle.py

commit f64475df0b87ec1d0300ab52ca2748e843d4f76e
Author: ssandaa <oziniek.art@mail.ru>
Date:   Wed Oct 4 00:28:26 2023 +0300

    added documentation to circle.py

commit b03f070a9193a2b46f4060bbe0a622e96f1629a9 (new_features_314041, main)
Author: ssandaa <oziniek.art@mail.ru>
Date:   Sat Sep 16 23:11:21 2023 +0300

    correted the mistake rectangle.py

commit f9a0010b40648c5bb8ebec25b487196e0218dcfa
Author: ssandaa <oziniek.art@mail.ru>
Date:   Sat Sep 16 22:48:48 2023 +0300

    add triangle.py

commit 83b2df4cee24fafed0ce89bc6091b2ef4a26ba23
Author: ssandaa <144237596+ssandaa@users.noreply.github.com>
Date:   Sat Sep 16 22:42:23 2023 +0300

    add rectangle.py

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added





