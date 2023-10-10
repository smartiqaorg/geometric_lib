# Solution
## Math formulas Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = a*/2

## Math formulas Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a+b+c
___
# Function
<br> Предполагается, что все вводимые значения в числовом формате, больше `0` и данная фигура существуетю
## Circle.py:
```python
import math
def area(r):
    return math.pi * r * r

def perimeter(r):
    return 2 * math.pi * r
```
- Функция `area(r)` возвращает численное значение площади круга с радисусом ```r```.
<br> Example:
<br>`area(1) // 3.141592653589793`
<br>`area(3) // 28.274333882308138`
<br>`area(1/math.sqrt(math.pi)) // 0.9999999999999999`
- Функция `perimeter(r)` возвращает численное значение периметра круга с радисусом ```r```.
<br> Example:
<br>`perimeter(1) // 6.283185307179586`
<br>`perimeter(3) // 18.84955592153876`
<br>`perimeter(1/math.pi) // 2.0`

## Rectangle.py:
```python
def area(a, b):
    return a * b

def perimeter(a, b):
    return 2*(a + b)
```
- Функция `area(a, b)` возвращает численное значение площади прямоугольника с длиннами ```a,b```.
<br> Example:
<br>`area(1, 3) // 3`
<br>`area(2/3, 6) // 4.0`
<br>`area(math.sqrt(2), 13*math.sqrt(2)) // 26.000000000000007`
- Функция `perimeter(a, b)` возвращает численное значение периметра прямоугольника с длиннами ```a,b```.
<br> Example:
<br>`perimeter(1, 3) // 8`
<br>`perimeter(2/3, 6) // 13.333333333333334`
<br>`perimeter(math.sqrt(2), 13*math.sqrt(2)) // 39.59797974644667 `

## Square.py:
```python
def area(a):
    return a * a

def perimeter(a):
    return 4 * a
```
- Функция `area(a)` возвращает численное значение площади квадарата со сторонной ```a```.
<br> Example:
<br>`area(3) // 9`
<br>`area(0.5) // 0.25`
<br>`area(math.sqrt(2)) // 2.0000000000000004`
- Функция `perimeter(a)` возвращает численное значение периметра квадарата со сторонной ```a```.
<br> Example:
<br>`perimeter(3) // 12`
<br>`perimeter(0.5) // 2.0`
<br>`perimeter(math.sqrt(2)) // 5.656854249492381 `

## Triangle.py:
```python
def area(a, h):
    return a * h / 2 
def perimeter(a, b, c):
    return a + b + c
```
- Функция `area(a, h)` возвращает численное значение площади треугольника со стороной ```a``` и высотой ```h```.
<br> Example:
<br>`area(1, 1) // 0.5`
<br>`area(0.5, 8) // 2.0`
<br>`area(4, 5) // 10.0`
- Функция `perimeter(a, b, c)` возвращает численное значение периметра треугольника со сторонами ```a, b, c```.
<br> Example:
<br>`perimeter(13, 8, 11) // 32`
<br>`perimeter(6, 6, 4.5) // 16.5`

___
# Commits
```
commit 5b42f25577b3f6fbd6474322488f851d0943fb46 (HEAD -> main)
Author: Daniil <DarkWizardJax@gmail.com>
Date:   Mon Sep 18 23:33:05 2023 +0300

    corrected rectangle and added triangle

commit 1be7222ac29a52ba0ffadda147d516339b11f203
Author: Daniil <DarkWizardJax@gmail.com>
Date:   Mon Sep 18 23:21:33 2023 +0300

    new file rectangle

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added
```
