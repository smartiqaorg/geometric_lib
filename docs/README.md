# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

  ## Circle
```python
import math
'''
Модуль math предоствляет обширный функционал для проведения вычислений 
с вещественными числами(числами с плавающей точкой).
'''
def area(r):
    '''
    Принимает число, которое  является радиусом круга: r
    Возвращает площадь круга, вычисляя ее по формуле: π * r^2
    '''
    return math.pi * r * r
def perimeter(r):
    '''
    Принимает число, которое  является радиусом круга: r
    Возвращает периметр круга, вычисляя его по формуле: 2 * π * r
    '''
    return 2 * math.pi * r
```
### Example
```python
r = 2
print (f"Area = area(r)); Perimetr = {perimetr(r)}")


Area = 12.566370614359172; Perimeter = 12.566370614359172
'''
## Rectangle
'''python
def area(a, b):
    '''
    Принимает два числа, которые являются сторонами прямоугольника: a, b
    Возвращает площадь прямоугольника, вычисляя ее по формуле: a * b
    '''
    return a * b


def perimeter(a, b):
    '''
    Принимает два числа, которые являются сторонами прямоугольника: a, b
    Возвращает периметр прямоугольника, вычисляя его по формуле: 2 * (a + b)
    '''
    return 2 * (a + b)
```
### Example
```python
a = 3
b = 5
print (f"Area = fare(a, b)}; Perimetr = {perimetr(a, b)}")


Area = 15; Perimetr = 16
```
## Square
```python
def area(a):
    '''
    Принимает число, которое является стороной квадрата: a
    Возваращает площадь квадрата, вычисляя ее по формуле: a^2
    '''
    return a * a


def perimeter(a):
    '''
    Принимает число, которое является стороной квадрата: a
    Возваращает периметр квадрата, вычисляя его по формуле: 4 * a
    '''
    return 4 * a
```
### Example
```python
a = 2
print (f"Area = {area(a)}; Perimetr = {perimetr(a)}")


Area = 4; Perimetr = 8
```
## Triangle
```python
def area(a, h):
    '''
    Принимает два числа, одно из них является стороной треугольника, другое его высотой: a, h
    Возвращает площадь треугольника, вычисляя ее по формуле: (a * h) / 2
    '''
    return a * h / 2
def perimeter(a, b, c):
    '''
    Принимает три числа, которые являются сторонами треугольника: a, b, c
    Возвращает периметр треугольника, вычисляя его по формуле: a + b + c
    '''
    return a + b + c
```
### Example
```python
a = 3
b = 4
с = 5
h = 2
print (f"Area = {area(a, h)}; Perimetr = {perimetr(a, b, c)}")


Area = 3; Perimetr = 12
```
## Commit History
`
commit 0ea3156cdb629211698a9259f96ab69bc20447b4 (HEAD -> math)
Author: Валерий Николаевич Пряжников <144845869+SNDSG@users.noreply.github.com>
Date:   Wed Oct 4 18:24:19 2023 +0300

    File Declaration

commit 14d5be5a803065acc2eeac0f9b2552a8780b6361 (origin/main, origin/HEAD, main)
Author: SN <valerapryazhnikov@gmail.com>
Date:   Thu Sep 14 23:20:49 2023 +0300

    fixed misstake in rectangle

commit 3cf835514c8388fdaeb8f340dc0d29e0cb04712e
Author: SN <valerapryazhnikov@gmail.com>
Date:   Thu Sep 14 22:15:34 2023 +0300

    Rectangle was created

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added
`
