# Документация

### Данный проект содержит в себе некоторые математические функции для нахождения площади и периметра фигур. Данные библиотеки написаны на языке программирования Python

## Библиотеки

### 1. circle.py

+ #### Функция area из данной библиотеки получает на вход значение радиуса окружности и возвращает ее площадь по формуле `pi * r * r`

#### *Пример работы с функцией на языке Python*

```python
import circle

print(area(5)) -> 78.53981633974483
```

+ #### Функция perimeter из данной библиотеки получает на вход значение радиуса окружности и возвращает ее периметр по формуле `2 * pi * r`

#### *Пример работы с функцией на языке Python*

```python
import circle

print(perimeter(5)) -> 31.41592653589793
```

### 2. rectangle.py

+ #### Функция area из данной библиотеки получает на вход значения 2 различных сторон прямоугольника и возвращет его площадь по формуле `a * b`

#### *Пример работы с функцией на языке Python*

```python
import rectangle

print(area(4, 5)) -> 20
```

+ #### Функция perimeter из данной библиотеки получает на вход значения 2 различных сторон искомого прямоугольника и возвращает его периметр согласно формлу `(a + b) * 2`

#### *Пример работы с функцией на языке Python* 

```python
import rectangle 

print(perimeter(4, 5)) -> 18
```

### 3. square.py

+ #### Функция area из данной библиотеки получает на вход длинну стороны квадрата и возращает его площадь по формуле `a * a`

#### *Пример работы фунции на языке Python*

```python
import square

print(area(5)) -> 25
```

+ #### Функция perimeter из данной библиотеки получает на вход длинну стороны квадрата и возращает его площадь по формуле `4 * a`

#### *Пример работы фунции на языке Python*

```python
import square

print(perimeter(5)) -> 20
```

### 4. triangle.py
+ #### Функция area из данной библиотеки получает на вход высоту треуголльника и длинну стороны к которой проведена высота и возвваращает его площадь по формуле `a * h / 2`

#### *Пример работы фунции на языке Python*

```python
import triangle

print(area(4, 5)) -> 10
```

+ #### Функция area из данной библиотеки получает на вход длины трех сторон треугольниа и возвращает периметр по формуле `a + b + c`

#### *Пример работы фунции на языке Python*

```python
import triangle

print(perimeter(3, 4, 5)) -> 12
```

| Хеш коммита | Автор                                | Комментарий                              |
|-------------|--------------------------------------|------------------------------------------|
| 995e19b     | AkihiroKano graf.orlov2005@gmail.com | added comments to the code               |
| 6915a0d     | AkihiroKano graf.orlov2005@gmail.com | added comments to the code               |
| a0932cb     | AkihiroKano graf.orlov2005@gmail.com | added comments to the code               |
| 26a8e32     | AkihiroKano graf.orlov2005@gmail.com | added comments to the code               |
| 2a9fa9a     | AkihiroKano graf.orlov2005@gmail.com | (origin/main, origin/HEAD, main) changed |
| 7ecc455     | AkihiroKano graf.orlov2005@gmail.com | Added new file rectangle.py              |
| d078c8d     | smartiqa info@smartiqa.ru            | L-03: Docs added                         |
| 8ba9aeb     | smartiqa info@smartiqa.ru            | L-03: Circle and square added            |


## Unit tests

### 1. circle.py
```angular2html
Всего тестов: 10
Верно пройденых тестов: 10
Процент верных тестов: 100%
```
### 2. rectangle.py
```angular2html
Всего тестов: 10
Верно пройденых тестов: 10
Процент верных тестов: 100%
```
### 3. square.py
```angular2html
Всего тестов: 10
Верно пройденых тестов: 10
Процент верных тестов: 100%
```
### 4. triangle.py
```angular2html
Всего тестов: 10
Верно пройденых тестов: 10
Процент верных тестов: 100%
```