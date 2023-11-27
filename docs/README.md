# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Документация по следующим файлам:
1. circle.py
2. square.py
3. rectangle.py
4. triangle.py

## circle.py
__Area__
-
Компилятор принемает число r, возводит его в квадрат и умножает на ПИ, таким образом получая площадь круга

_Пример_

r = 10; S = 10 * 10 * 3,14 = 314

__Perimetr__

Компилятор принемает число r, умножает его на два и на ПИ, таким образом получая периметр круга

_Пример_

r = 10; P = 10 * 2 * 3,14 = 62,8

## square.py
__Area__

Компилятор принимает на вход число, умножают его само на себя и получает площадь

_Пример_

a = 10; S = 10 * 10 = 100

__Perimetr__

Компилятор принимает на вход число, умножает его на 4 и получает периметр

_Пример_

a = 10; P = 10 * 4 = 40

## rectangle.py
__Area__

Компилятор принимает два числа, обозначающих стороны прямоугольника и перемножает их, получая площадь
_Пример_

a = 10, b = 5; S = 10 * 5 = 50

__Perimetr__

Компилятор принимает два числа, обозначающих стороны прямоугольника, затем складывает их и умножает на два, таким образом получаем периметр

_Пример_

a = 10, b = 5; P = 2 * (10 + 5) = 30

## triangle.py

__Area__

Компилятор получает два числа - длину оснований и высоту треугольника. По формуле площади треугольника находим его площадь

_Пример_

a = 10, h = 5; S = 10 * 5 / 2 = 25

__Perimetr__

Компилятор получает три числа - длину всех сторон треугольника. По формуле периметра треугольника находим его периметр

_Пример_

a = 10, b = 5, c = 3; P = 10 + 5 + 3 = 18

## История изменения проекта с хешами комитов

**commit a2015ce88ecc5ad55e6410eadc553baf0d1f9e38 (origin/main, origin/HEAD)**
Author: daniil3006 <daniil.stank@gmail.com>
Date:   Wed Sep 13 15:08:12 2023 +0300

    Внесены изменения в файл rectangle.py

**commit 0cb687184952ce556315401ba2d9957c805c7a14**
Author: daniil3006 <daniil.stank@gmail.com>
Date:   Wed Sep 13 15:02:01 2023 +0300

    Был добавлен новый файл

**commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (upstream/main, upstream/HEAD)**
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

**commit 8ba9aeb3cea847b63a91ac378a2a6db758682460**
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

**ccommit e2377b12d96cdf82416cfbe8aae38e36864f595d (origin/main, origin/HEAD)**
Author: daniil3006 <144243377+daniil3006@users.noreply.github.com>
Date:   Wed Nov 15 12:27:41 2023 +0300

    создан файл с unit тестами
