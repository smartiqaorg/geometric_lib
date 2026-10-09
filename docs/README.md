# Geometric Lib Documentation

## General Description
This project is a Python library for calculating the area and perimeter of various geometric shapes: circles, rectangles, squares, and triangles. It was built as part of the "Software Development Tools" course to practice Git version control and documentation.

## Function Descriptions

### Circle (circle.py)
- `area(r)`: Returns the area of a circle with radius `r`. Example: `area(5)` returns `78.54`.
- `perimeter(r)`: Returns the perimeter of a circle with radius `r`. Example: `perimeter(5)` returns `31.42`.

### Rectangle (rectangle.py)
- `area(a, b)`: Returns the area of a rectangle with sides `a` and `b`. Example: `area(5, 10)` returns `50`.
- `perimeter(a, b)`: Returns the perimeter of a rectangle with sides `a` and `b`. Example: `perimeter(5, 10)` returns `30`.

### Square (square.py)
- `area(a)`: Returns the area of a square with side `a`. Example: `area(5)` returns `25`.
- `perimeter(a)`: Returns the perimeter of a square with side `a`. Example: `perimeter(5)` returns `20`.

### Triangle (triangle.py)
- `area(a, h)`: Returns the area of a triangle with base `a` and height `h`. Example: `area(5, 10)` returns `25`.
- `perimeter(a, b, c)`: Returns the perimeter of a triangle with sides `a`, `b`, `c`. Example: `perimeter(3, 4, 5)` returns `12`.

## Change History
- `8ba9aeb` - L-03: Circle and square added
- `a46f978` - Added new file rectangle.py
- `b1eec2d` - Added new file triangle.py
- `ddbccc3` - Fixed the bug in the perimeter calculation