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
~~~
```python

import math
''' Модуль math предоставляет обширный функционал для работы с числами '''

def area(r):
    ''' число r принимает значение радиуса круга
        функция возвращает r в квадрате, 
        умноженное на число pi, т.е. площадь круга'''
    return math.pi * r * r


def perimeter(r):
    ''' число r принимает значение радиуса круга
        git   функция возвращает удвоенное произведение
       радиуса круга (r) на число pi, т.е. периметр круга '''
    return 2 * math.pi * r
```
~~~
***Пример вызова***
~~~
```python
r = 6
print("Area = ", area(r))
print("Perimeter = ", perimeter(r))
```

```markdown
*input:* r = 6
*output:* Area:=113.04 Perimeter:=37.699104
```
~~~
### rectangle.py

***Программа***
~~~
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
~~~
***Пример вызова***
~~~
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
~~~
### square.py

***Программа***
~~~
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
~~~
***Пример вызова***
~~~
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
~~~
### triangle.py

***Программа***
~~~
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
~~~
***Пример вызова***
~~~
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
~~~

## история изменения проекта с хэшами коммитов
| Автор              | Дата                             | Хэш                                        | Комментарий                         |
|--------------------|----------------------------------|--------------------------------------------|-------------------------------------|
| ssandaa            | Wed Nov 15 23:12:18 2023 +0300   | 6da9b3a9e58ab85dc0ad20d2ebe17db58b785b7b   | test: added tests for triangle      |
| ssandaa            | Wed Nov 15 23:11:43 2023 +0300   | 5554e41c003e530eff1bfb3243e9568d943ff0a6   | test: added tests for square        |
| ssandaa            | Wed Nov 15 23:11:17 2023 +0300   | b04bd9c6dfb6e55b1099936070f942dda3935f5    | test: added tests for rectangle     |
| ssandaa            | Wed Nov 15 23:10:10 2023 +0300   | d38677240c78b6605505bb9ea53a60fffa88ce71   | test: added tests for circle        |
| ssandaa            | Wed Nov 15 22:50:13 2023 +0300   | 4225c1531bd0eeff9daa8207d02d2487b70a70ce   | 4 unittests have been added         |
| ssandaa            | Wed Oct 4 01:26:11 2023 +0300    | e0a536566922b2a67e87ddaf2049e40ad983c1dc   | general description of the solution |
| ssandaa            | Wed Oct 4 00:33:00 2023 +0300    | 2c39fd30c9555c78603d18ac59a538b53b8e53d3   | added documentation to triangle.py  |
| ssandaa            | Wed Oct 4 00:32:11 2023 +0300    | 623b387b9c99d44620d5314d47923c03cf4c9e0a   | added documentation to square.py    |
| ssandaa            | Wed Oct 4 00:30:44 2023 +0300    | c1485d6e8f6cd831a3298019962efaf3f0960fb3   | added documentation to rectangle.py |
| ssandaa            | Wed Oct 4 00:28:26 2023 +0300    | f64475df0b87ec1d0300ab52ca2748e843d4f76e   | added documentation to circle.py    |
| ssandaa            | Sat Sep 16 23:11:21 2023 +0300   | b03f070a9193a2b46f4060bbe0a622e96f1629a9   | correted the mistake rectangle.py   |
| ssandaa            | Sat Sep 16 22:48:48 2023 +0300   | f9a0010b40648c5bb8ebec25b487196e0218dcfa   | add triangle.py                     |
| ssandaa            | Sat Sep 16 22:42:23 2023 +0300   | 83b2df4cee24fafed0ce89bc6091b2ef4a26ba23   | add rectangle.py                    |
| smartiqa           | Thu Mar 4 14:55:29 2021 +0300    | d078c8d9ee6155f3cb0e577d28d337b791de28e2   | L-03: Docs added                    |
| smartiqa           | Thu Mar 4 14:54:08 2021 +0300    | 8ba9aeb3cea847b63a91ac378a2a6db758682460   | L-03: Circle and square added       |


## UnitTest
#### Всего сделано 32 теста: 24 успешных, 8 неуспешных

### Circle.py
###### correct tests
- area()
~~~
input: 5
output: 78.53981633974483
~~~
~~~
input: 5.5
output: 95.03317777109123
~~~
~~~
input: 0
output: 0
~~~
- perimeter()
~~~
input: 5
output: 31.41592653589793
~~~
~~~
input: 5.5
output: 34.55751918948772
~~~
~~~
input: 0
output: 0
~~~
###### uncorrect tests
- area()
~~~
input: -5
output: 78.53981633974483
expected: the radius cannot be negative
~~~
- perimeter()
~~~
input: -5
output: -31.41592653589793
expected: the radius cannot be negative
~~~

### Reactangle.py
###### correct tests
- area()
~~~
input: 4,5
output: 20
~~~
~~~
input: 4.5, 5.5
output: 24.75
~~~
~~~
input: 4,0
output: 0
~~~
- perimeter()
~~~
input: 4,5
output: 18
~~~
~~~
input: 4.5, 5.5
output: 20.0
~~~
~~~
input: 4,0
output: 8
~~~
###### uncorrect tests
- area()
~~~
input: 4, -5
output: -20
expected: Стороны прямоугольника не могут быть отрицательными
~~~
- perimeter()
~~~
input: 4, -5
output: -2
expected: Стороны прямоугольника не могут быть отрицательными
~~~

### Square.py
###### correct tests
- area()
~~~
input: 4
output: 16
~~~
~~~
input: 4.5
output: 20.25
~~~
~~~
input: 0
output: 0
~~~
- perimeter()
~~~
input: 4
output: 16
~~~
~~~
input: 4.5
output: 18.0
~~~
~~~
input: 0
output: 0
~~~
###### uncorrect tests
- area()
~~~
input: -4
output: 16
expected: the side of the square cannot be negative
~~~
- perimeter()
~~~
input: -4
output: -16
expected: the side of the square cannot be negative
~~~

##### Triangle.py
###### correct tests
- area()
~~~
in: 4,5
out: 10.0
~~~
~~~
in: 4.5, 5.5
out: 12.375
~~~
~~~
in: 4,0
out: 0
~~~
- perimeter()
~~~
in: 4, 5, 6
out: 15
~~~
~~~
in: 4.5, 5.5, 6.5
out: 16.5
~~~
~~~
in: 4, 0, 5.5
out: 8.5
~~~
###### uncorrect tests
- area()
~~~
in: 4, -5
out: -10.0
expected: the base and height cannot be negative
~~~
- perimeter()
~~~
in: 4, 5, -6
out: 3
expected: the base and height cannot be negative
~~~
## autotests success:
- all tests: 32
- tests with errors: 8
- tests without errors: 24
~~~
tests with errors - 8/32 = 25%
tests without errors - 24/32 = 75%
~~~