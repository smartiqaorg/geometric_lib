# **Лабораторная работа №2** 
Проект содержит файлы типа py, каждый из которых вычисляет площадь и периметр отдельной фигуры, всего их 4.  
1. Круг
2. Прямоугольник
3. Квадрат 
4. Треугольник

## **Формулы**
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

## **Описание решения и функции файла cyrcle.py**
```cpp
import math

def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r
```
- Этот код вычисляет площадь и периметр круга.

### Описание и пример вызова функции area
```cpp
def area(r):
    return math.pi * r * r
```
 - Функция возвращает площадь круга.  
Пример: r = 10, возвращает ~314

### Описание и пример вызова функции perimeter
```cpp
def perimeter(r):
    return 2 * math.pi * r
```
 - Функция возвращает длину окружности.  
Пример: r = 10, возвращает ~62

## **Описание решения и функции файла rectangle.py**
```cpp
def area(a, b):
    return a * b

def perimeter(a, b):
    return 2*(a + b)
```
- Этот код вычисляет площадь и периметр прямоугольника.

### Описание и пример вызова функции area
```cpp
def area(a, b):
    return a * b
```
 - Функция возвращает площадь прямоугольника.
Пример: a = 5, b = 2, возвращает 10.

### Описание и пример вызова функции perimeter
```cpp
def perimeter(a, b):
    return 2*(a + b)
```
 - Функция возвращает периметр прямоугольника.  
Пример: a = 10, b =5,  возвращает 30.

## **Описание решения и функции файла square.py**
```cpp
def area(a):
    return a * a


def perimeter(a):
    return 4 * a
```
- Этот код вычисляет площадь и периметр квадрата.

### Описание и пример вызова функции area
```cpp
def area(a):
    return a * a
```
 - Функция возвращает площадь квадрата.  
Пример: a = 5, возвращает 25.

### Описание и пример вызова функции perimeter
```cpp
def perimeter(a):
    return 4 * a
```
 - Функция возвращает периметр прямоугольника.  
Пример: a = 10  возвращает 40.

## **Описание решения и функции файла triangle.py**
```cpp
def area(a, h):
    return a * h / 2

def perimeter(a, b, c):
    return a + b + c
```
- Этот код вычисляет площадь и периметр треугольника.

### Описание и пример вызова функции area
```cpp
def area(a, h):
    return a * h / 2
```
 - Функция возвращает площадь треугольника.  
Пример: a = 5, h = 10, возвращает 25.

### Описание и пример вызова функции perimeter
```cpp
def perimeter(a, b, c):
    return a + b + c
```
 - Функция возвращает периметр треугольника.  
Пример: a = 5, b = 7, c = 8,  возвращает 20.

## История изменения проекта с хешами комитов (кроме последней записи):
| Hash коммита | Описание |
|-|-|
|8ba9aeb| L-03: Circle and square added|
|d078c8d | L-03: Docs added|
|00641e2| feat: add calc for a rectangle|
|5f42811| feat: add a calc for a triangle|
|00b082c| fix: fix a calс in rectangle.py|
|f446c1c| docs: new comments for circle.py|
|d4d85df| docs: new comments for rectangle.py|
|7b0cef6| docs new comments for square.py|
|39b617a| docs: new comments for triangle.py|
