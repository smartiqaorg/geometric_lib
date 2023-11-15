
# Описание работы программ
- Каждая программа представляет из себя набор функций , отвечающих за вычисление площади и периметра данной фигуры.
- На вход программа получает некоторое количество аргументов.
- На выходе пользователь получает периметр или площадь для данной фигуры.

# Код программы с примерами вывода.
## Circle 
- Код на языке Python
```python
import math


def area(r):
    '''
    возвращает площадь круга
	На вход подается число r:
	На выходе получаем площадь круга
    '''
	
    return math.pi * r * r


def perimeter(r):
    '''
	Возращает длину круга
		На вход подается число r
		На выходе получают длину круга.
   '''
    return 2 * math.pi * r
```
### Пример работы программы 
```
print(area(5))
print(perimeter(10))
```
```
78.53981633974483
62.83185307179586
```

## Rectangle
- Код на языке Python
```python
def area(a, b):
'''
Выводит площадь прямоугольника.
	На вход получает 2 числа.
	На выходе выдает произведение этих чисел - площадь прямоугольника.
''' 
    return a * b 

def perimeter(a, b):
'''
Выводит периметр прямоугольника.
	На вход получает 2 числа.
	На выходе выдает сумму этих чисел , умноженную на 2 - периметр.
''' 
    return (a + b)*2
```
### Пример работы программы 
```
print(area(5 , 7))
print(perimeter(10 , 15))
```
```
35
50
```
## Square
- Код на языке Python
```python

def area(a):
'''
Выводит площадь квадрата.
	На вход получает число a.
	На выходе выводит его произведение само на себя - площадь.
'''
    return a * a


def perimeter(a):
'''
Выводит периметр квадрата.
	На вход получает число a.
	На выходе выдает его произведение на 4 - периметр.
'''
    return 4 * a
```
### Пример работы программы 
```
print(area(5))
print(perimeter(10))
```
```
25
40
```

## Triangle
- Код на языке Python
```python
def area(a, h):
'''
Выводит площадь треугольника.
	На вход получает два числа a , h - сторону и высоту.
	На выходе выводит их произведение , деленное на 2 - площадь.
''' 
    return a * h / 2 

def perimeter(a, b, c):
'''
Выводит периметр треугольника.
	На вход получает 3 числа - стороны треугольника.
	На выходе выводит их сумму - периметр.
''' 
    return a + b + c
```
### Пример работы программы 
```
print(area(5 , 9))
print(perimeter(3 , 4 , 5))
```
```
22.5
12
```

# Вывод истории изменений проекта с хэшами коммитов
```
b97fbd8 (HEAD -> main) added documentation to the file
ce6445c added documentation to the file
95226ed added documentation to the file
de6f714 added documentation to the file
2e63cdb (origin/main, origin/HEAD) this is end
6d6ffeb error was fixed
6491bb3 im create a new file
d078c8d L-03: Docs added
8ba9aeb L-03: Circle and square added
```

# Unit Tests
- Unit test for circle : [UnitTEST Circle](https://github.com/NizamutdinovEmir/geometric_lib/blob/main/testcircle.py)
- Unit test for rectangle : [UnitTEST Rectangle](https://github.com/NizamutdinovEmir/geometric_lib/blob/main/testrectangle.py)
- Unit test for square : [UnitTEST Square](https://github.com/NizamutdinovEmir/geometric_lib/blob/main/testsquare.py)
- Unit test for triangle : [UnitTEST Triangle](https://github.com/NizamutdinovEmir/geometric_lib/blob/main/testtriangle.py)

