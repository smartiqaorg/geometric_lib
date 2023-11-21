 #Geometric Lib
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://camo.githubusercontent.com/fc8cea0dacea7dd19a09aacf06109ccfa5ed931fa471c0beffb5acacbaa39c33/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f505954484f4e2d626c61636b3f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d676f6c64">
  <source media="(prefers-color-scheme: light)" srcset="https://camo.githubusercontent.com/fc8cea0dacea7dd19a09aacf06109ccfa5ed931fa471c0beffb5acacbaa39c33/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f505954484f4e2d626c61636b3f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d676f6c64">
  <img alt="Shows an illustrated sun in light mode and a moon with stars in dark mode." src="https://camo.githubusercontent.com/fc8cea0dacea7dd19a09aacf06109ccfa5ed931fa471c0beffb5acacbaa39c33/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f505954484f4e2d626c61636b3f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d676f6c64">
</picture>

# Math formulas
В каждом из 4 файлов python содержатся функции, считающие площадь и периметр 4 фигур:
- круг
- прямоугольник
- квадрат
- треугольник

## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah / 2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Square: P = 4a
- Square: P = 4a
- Triangle: P = a + b + c

## Functions 
- ### circle.py
  - ##### area(r)

    Принимает число r - радиус круга, возвращает число возведенное в квадрат и домноженное на пи - площадь круга
    ```
    print(area(6))
    -> 113.04
    ```
  - ##### perimeter(r)
    
    Принимает число r - радиус круга,возвращает число домноженное на два и на пи - периметр круга
    ```
    print(perimeter(6))
    -> 37.68
    ```
- ### rectangle.py
  - ##### area(a,b)
    
    Принимает два числа a и b - стороны прямоугольника,возвращает произведение двух чисел - площадь прямоугольника
    ```
    print(area(4,5))
    -> 20
    ```
  - ##### perimeter(a,b)
    ```
    print(perimeter(4,5))
    -> 18
    ```
    
    Принимает два числа a и b - стороны прямоугольника,возращает сумму двух чисел домноженную на два
- ### triangle.py
  - ##### area(a,h)
    Принимает два числа a - сторона треугольника и h - высота, опущенная к стороне треугольника,
    возвращает произведение двух чисел деленное на два - площадь треугольника
    ```
    print(area(5,6))
    -> 15
    ```
  - ##### perimeter(a,b,c)
    Принимает три числа a, b, c - стороны трегольника,
    возвращает сумму трех чисел - периметр треугольника
    ```
    print(perimeter(6,7,8)
    -> 21
    ```
- ### square.py
  - ##### area(a)
    Принимает число a - сторону квадрата,
    возвращает квадрат числа - площадь квадрата
    ```
    print(area(5))
    -> 25
    ```
  - ##### perimeter(a)
    Принимает число a - сторону квадрата,
    возвращает число умноженное на четыре - периметр квадрата
    ```
    print(perimeter(5))
    -> 20
    ```
### Хеш коммитов:
| хеш коммита | автор коммита               | комментарий                   |
|-------------|-----------------------------|-------------------------------|
| 94b52e3     | gront <408507@edu.itmo.ru>  | comment to the cod            |
| 106df63     | gront <408507@edu.itmo.ru>  | the bug has been fixed        |
| 95efe91     | gront <408507@edu.itmo.ru>  | Add new file                  |
| d078c8d     | smartiqa <info@smartiqa.ru> | L-03: Docs added              |
| 8ba9aeb     | smartiqa <info@smartiqa.ru> | L-03: Circle and square added |