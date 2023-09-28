# Документация

В этой документации представлен обзор решения и описана каждая функция вместе с примерами использования.
## Математические формулы
| Фигура    | Площадь         | Периметр                  |
|-----------|-----------------|---------------------------|
| Circle    | S = πR²         | P = 2πR                   |
| Rectangle | S = ab          | P = 2a + 2b               |
| Square    | S = a²          | P = 4a                    |
| Triangle  | S = a/h         | P = a + b + c             |

## Общее описание решений

Решение состоит из нескольких модулей, вычисляющих периметр и площадь различных геометрических фигур.

## circle.py
hash:  4c8bbe09edf2f566d5cec64c729d222045d0e342
### area

Принимает радиус круга (r) и возвращает площадь круга.

```python
import math

def area(r):
    return math.pi * r * r
```
Пример использования
```python
input: 3
ouput: 28.274333882308138
```

### perimeter
Принимает радиус круга (r), длину окружности.

```python
def perimeter(r):
    return 2 * math.pi * r
```
Пример использования
```python
input: 3
ouput: 18.84955592153876
```
## rectangle.py
hash: 5d72e6fab0dd2f2bd59c550d6d75dd1a67023b5c
### area

Принимает длины сторон (a и b), возвращает площадь прямоугольника.

```python
def area(a, b): 
    return a * b
```
Пример использования
```python
input: 2, 3
ouput: 6
```

### perimeter
Принимает длины сторон (a и b), возвращает периметр прямоугольника.

```python
def perimeter(a, b): 
    return 2*(a + b)
```
Пример использования
```python
input: 2, 3
ouput: 10
```

## square.py
hash: d1aa71e4fdcef0ede58ffcefdef2d723dbb23257
### area

Принимает длину стороны (а), возвращает площадь квадрата.

```python
def area(a):
    return a * a
```
Пример использования
```python
input: 2
ouput: 4
```

### perimeter
Принимает длину стороны (а), возвращает периметр квадрата.

```python
def perimeter(a):
    return 4 * a
```
Пример использования
```python
input: 2
ouput: 8
```

## triangle.py
hash: 446b5ed864b763994894d62a9f02fe1865a85ec3
### area

Принимает длину стороны и высоту (a и h), возвращает площадь треугольника.

```python
def area(a, h): 
    return a * h / 2
```
Пример использования
```python
input: 5, 10
ouput: 25
```

### perimeter
Принимает длины сторон (a,b,c), возвращает периметр треугольника.

```python
def perimeter(a, b, c): 
    return a + b + c
```
Пример использования
```python
input: 1, 2, 3
ouput: 6
```
