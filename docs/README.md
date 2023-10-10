# Общее описание решения
Данный репозиторий содержит набор функций, позволяющих вычислять площадь и периметр круга, квадрата, прямоугольника.
# Функции
## Круг
```
def area(r):
    return math.pi * r * r
```   
Принимает число r - радиус круга. Возращает площадь крга, вычесленную по формуле Пи умноженное на квадрат радиуса.

```
def perimeter(r):
    return 2 * math.pi * r
```
Принимает число r - радиус круга. Возращает периметр крга, вычесленный по формуле 2 умноженное на Пи умноженное на радиуса.
## Прямоугольник
```
def area(a, b):
    return a * b
```
Принимает 2 числа a и b - стороны прямоугольника. Возращает площадь прямоугольниа - произведение a и b
```
def perimeter(a, b):  
    return (a + b) * 2
```
Принимает 2 числа a и b - стороны прямоугольника. Возращает периметр прямоугольниа - удвоенна сумма a и b
## Квадрат
```
def area(a):
    return a * a
```
Принимает число a - сторона квадрата. Возращает площадь квадрата - квадрат a
```
def perimeter(a):
    return 4 * a
```
Принимает число a - сторона квадрата. Возращает периметр квадрата - a умноженное на 4
## Треугольник
```
def area(a, h): 
    return a * h / 2 
```
Принимает 2 числа a и h - основание и высота треугольника. Возращает площадь треугольника - полупроизведение a и b
```
def perimeter(a, b, c): 
    return a + b + c 
```
Принимает 3 числа a,b,c - стороны треугольника. Возращает периметр треугольника - сумма a,b и c

# История изменения проекта с хешами комитов
```
commit 5084f6ea9682427a9ade202797cd41f1c70ed4ad (HEAD -> main, origin/main, origin/HEAD)
Author: Danial <danial.bapinaev@gmail.com>
Date:   Wed Sep 20 21:42:47 2023 +0300

    fixed error

commit a2a64c938ba750d449c1e273f59963df013e535a
Author: Danial <danial.bapinaev@gmail.com>
Date:   Wed Sep 20 21:23:33 2023 +0300

    rectangle file added

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added

```
# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
