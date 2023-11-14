# Geometric Lib

<div align="center">
<img src="https://img.shields.io/badge/PYTHON-black?style=for-the-badge&logo=python&logoColor=gold"/><img src="https://img.shields.io/badge/LINUX-black?style=for-the-badge&logo=linux&logoColor="/><img src="https://img.shields.io/badge/GIT-black?style=for-the-badge&logo=git&logoColor=orange"/><img src="https://img.shields.io/badge/GITHUB-black?style=for-the-badge&logo=GitHub&logoColor=white"/><img src="https://img.shields.io/badge/VSC-black?style=for-the-badge&logo=Visual Studio Code&logoColor=007ACC"/>
</div>

<p></P>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
![GitHub Issues](https://img.shields.io/github/issues/RuslanKoynov/geometric_lib.svg)
![GitHub Pull Requests](https://img.shields.io/github/issues-pr/RuslanKoynov/geometric_lib.svg)
![Stars](https://img.shields.io/github/stars/RuslanKoynov/geometric_lib.svg)

</div>

## Description
Geometric Lib is a powerful and convenient library for working with geometric data in your project. It provides a set of tools and functions for performing various operations with geometric shapes


## Math formulas
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = $ah \over 2$

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

## Description of functions and example of working with them:

### Circle:
- Area:
    The area(`r`) function calculates the area of a circle given its radius `r`. It uses the mathematical constant `π` (`pi`) to perform the calculation using the formula: 
    
    `Area = π * r^2`

    Where:
    - `Area` is the area of the circle.
    - `π` (`pi`) is a mathematical constant approximately equal to 3.14159.
    - `r` is the radius of the circle.

    Example of usage:

    ```python
    from circle import area as circle_area_def

    radius = 5.0
    circle_area = circle_area_def(radius)
    print(circle_area)
    ```

- Perimeter:
    The `perimeter(r)` function calculates the perimeter (circumference) of a circle given its radius r. It uses the mathematical constant π (pi) to perform the calculation using the formula: 
    
    `Perimeter = 2 * π * r`

    Where:

    - `Perimeter` is the perimeter (circumference) of the circle.
    - `π` (`pi`) is a mathematical constant approximately equal to 3.14159.
    - `r` is the radius of the circle.

    Example of usage:

    ```python
    from circle import perimeter as circle_perimeter_def

    radius = 5.0
    circle_perimeter = circle_perimeter_def(radius)
    print(circle_perimeter)
    ```

### Rectangle:
- Area:
    The `area(a, b)` function calculates the area of a rectangle given its two side lengths, `a and b`. It uses the formula:

    `Area = a * b`

    Where:
    - `Area` is the area of the rectangle.
    - `a` is the length of one side of the rectangle.
    - `b` is the length of the other side of the rectangle.

    Example of usage:

    ```python
    from rectangle import area as rectangle_area_def

    a, b = 5, 10
    rectangle_area = rectangle_area_def(a, b)
    print(rectangle_area)
    ```

- Perimeter:
    The `perimeter(a, b)` function calculates the perimeter of a rectangle given its two side lengths, a and b. 
    It uses the formula:

    `Perimeter = 2 * (a + b)`

    Where:
    - `Perimeter` is the perimeter of the rectangle.
    - `a` is the length of one side of the rectangle.
    - `b` is the length of the other side of the rectangle.

    Example of usage:

    ```python
    from rectangle import perimeter as rectangle_perimeter_def

    a, b = 5, 10
    rectangle_perimeter = rectangle_perimeter_def(a, b)
    print(rectangle_perimeter)
    ```

### Square:
- Area:
    The `area(a)` function calculates the area of a square given the length of one of its sides, a. It uses the formula:

    `Area = a * a`

    Where:
    - Area is the area of the square.
    - a is the length of one side of the square.

    Example of usage:

    ```python
    from square import area as square_area_def

    a = 10
    square_area = square_area_def(a)
    print(square_area)
    ```

- Perimeter:
    The `perimeter(a)` function calculates the perimeter of a square given the length of one of its sides, a. 
    It uses the formula:

    `Perimeter = 4 * a`

    Where:
    - `Perimeter` is the perimeter of the square.
    - `a` is the length of one side of the square.

    Example of usage:

    ```python
    from square import perimeter as square_perimeter_def

    a = 10
    square_perimeter = square_perimeter_def(a)
    print(square_perimeter)
    ```

### Triangle:
- Area:
    The `area(a, h)` function calculates the area of a triangle given its base length a and height h. 
    It uses the formula:

    `Area = (a * h) / 2`

    Where:
    - `Area` is the area of the triangle.
    - `a` is the length of the base of the triangle.
    - `h` is the height of the triangle, measured perpendicular to the base.

    Example of usage:

    ```python
    from triangle import area as triangle_area_def

    a, h = 10, 6
    triangle_area = triangle_area_def(a, h)
    print(triangle_area)
    ```

- Perimeter:
    The `perimeter(a, b, c)` function calculates the perimeter of a triangle given the lengths of its three sides, a, b, and c. 
    It uses the formula:

    `Perimeter = a + b + c`

    Where:
    - `Perimeter` is the perimeter of the triangle.
    - `a, b, and c` are the lengths of the three sides of the triangle.

    Example of usage:

    ```python
    from triangle import perimeter as triangle_perimeter_def

    a, b, c = 3, 4, 5
    triangle_perimeter = triangle_perimeter_def(a, b, c)
    print(triangle_perimeter)
    ```

### Commits hash:
```git
commit d63c6092f20da2eb5bad31a1d723b74be55658d9 (HEAD -> main, origin/main, orig
in/HEAD)
Author: k6zma <k6zma@yandex.ru>
Date:   Tue Nov 14 23:06:29 2023 +0300

    made big reffub in test script

commit 0a6a6e36041061a35510e6d1f0bb504374258fed
Author: k6zma <k6zma@yandex.ru>
Date:   Tue Nov 14 21:57:37 2023 +0300

    added verbose information in tests

commit 16d9cb066335fb545426f32d39b6910b8c713e20
Author: k6zma <k6zma@yandex.ru>
Date:   Tue Nov 14 21:29:39 2023 +0300

    added temp simple tests for project

commit c432a600feda5b3115c4afb7344ae3d7f57bbb75
Author: k6zma <k6zma@yandex.ru>
Date:   Sun Oct 1 14:53:55 2023 +0300

    added project description to README.md

commit ae1ad44300e543e8c5d79d62c379f87cd4b401a6
Author: k6zma <k6zma@yandex.ru>
Date:   Sun Oct 1 14:48:09 2023 +0300

    Added description for each function

commit 8b4cb5fdeff9987a90e17218f3200e9ecc925566
Author: k6zma <k6zma@yandex.ru>
Date:   Sun Oct 1 08:29:37 2023 +0300

    added triangle.py

commit d8b97bf3090e0db08b68c9164425b06530d9798e
Author: 408508_mikhail <k6zma@yandex.ru>
Date:   Wed Sep 6 21:04:03 2023 +0300

    fixed error in rectangle.py

commit e9e678a27aa5c502fa40a08837cfc23fc4bcc03d
Author: 408508_mikhail <k6zma@yandex.ru>
Date:   Wed Sep 6 21:01:23 2023 +0300

    added new file (rectangle.py)

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added
```