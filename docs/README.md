# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Документация

В проекте содержатся модули, которые позволяют совершать вычислительные действия по нахождению площади и периметра для определенных геометрических фигур.

---

## Модуль rectangle.py

### Функция area
Получает на вход десятичные два числа `a` и `b`, возвращает десятичное число произведение `a` на `b`.

##### Примеры работы с функцией
```python
[Python]
import rectangle

rectangle.area(2, 3) -> 6

rectangle.area(4, 10) -> 40
```

### Функция perimetr
Получает на вход десятичные числа `a` и `b`, возвращает десятичное число произведение числа 2 на сумму чисел `a` и `b`.

##### Примеры работы с функцией
```python
[Python]
import rectangle

rectangle.perimetr(4, 5) -> 18

rectangle.perimetr(10, 2) -> 24
```

## Модуль circle.py

### Функция area
Получает на вход десятичное число `r`, что явялется радиусом, возвращает произведение числа pi на `r` квадрат.

##### Примеры работы с функцией
```python
[Python]
import circle

circle.area(4) -> 50.24

circle.area(10) -> 314
```

### Функция perimetr
Получает на вход десятичное число r, что явялется радиусом, возвращает произведение числа 2 на r и число pi.

##### Примеры работы с функцией
```python
[Python]
import circle

circle.perimetr(5) -> 31.4

circle.perimetr(10) -> 62.8
```

## Модуль triangle.py

### Функция area
Получает на вход два десятичных числа `a`, `h`, возвращает произведение чисел `a` на `h` и частное от деления на 2.

##### Примеры работы с функцией
```python
[Python]
import triangle

triangle.area(4, 2) -> 4

triangle.area(5, 3) -> 7.5
```

### Функция perimetr
Получает на вход числа `a`, `b`, `c`, возвращает десятичное число сумму чисел `a`,`b`,`c`

##### Примеры работы с функцией
```python
[Python]
import triangle

triangle.perimetr(4, 3, 2) -> 9

triangle.perimetr(3, 1, 9) -> 13
```

## Модуль square.py

### Функция area
Получает на вход дестичное число `a`, возвращает десятичное число `a` квадрат.

##### Примеры работы с функцией
```python
[Python]
import square

square.area(4) -> 16

square.area(11) -> 121
```

### Функция perimetr
Получает на вход десятичное число `a`, возвращает десятичное число произведение числа 4 на число `a`.

##### Примеры работы с функцией
```python
[Python]
import square

square.perimetr(4) -> 16

square.perimetr(5) -> 20
```

