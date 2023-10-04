# Geometric.lib

## Description

Geometric Lib is a Python library designed for handling geometric data and calculations. It provides a set of convenient tools for working with various geometric shapes, such as circles, rectangles, triangles, and points, allowing users to perform calculations related to these shapes, including area calculations, perimeter calculations, and distance measurements between points. The library aims to simplify common geometric computations and make them easily accessible for developers working with geometric data in Python.

## Table of Contents
- [Math formulas](#mathformulas)
- [Geometric Shapes](#geometricshapes)
- [Example usage](#exampleusage)


## Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

provides a reference for the main functions available in the `geometric_lib` library. These functions allow you to work with geometric shapes and perform various calculations related to them.

## Geometric Shapes

### `Circle(radius)`

Creates a circle object with the specified radius.

**Parameters:**
- `radius` (float): The radius of the circle.

#### Methods:

- `area()`: Returns the area of the circle.
- `perimeter()`: Returns the perimeter of the circle.
```python
import math
def area(r):
    return math.pi * r * r
def perimeter(r):
    return 2 * math.pi * r
```
### `Rectangle(width, height)`

Creates a rectangle object with the specified width and height.

**Parameters:**
- `width` (float): The width of the rectangle.
- `height` (float): The height of the rectangle.

#### Methods:

- `area()`: Returns the area of the rectangle.
- `perimeter()`: Returns the perimeter of the rectangle.
```python
def area(a, b):
    return a * b
def perimeter(a, b):
    return 2 * (a + b)
```
### `Triangle`

### Area

The `area(a, h)` function calculates the area of a triangle given its base length `a` and height `h`. It uses the formula:

Where:

- `Area` is the area of the triangle.
- `a` is the length of the base of the triangle.
- `h` is the height of the triangle, measured perpendicular to the base.

**Example of usage:**

```python
from triangle import area as triangle_area_def

a, h = 10, 6
triangle_area = triangle_area_def(a, h)
print(triangle_area)
```
```python
Perimeter = a + b + c
```

## Example Usage

Here are some examples of how to use these functions:

```python
from geometric_lib.shapes import Circle, Rectangle
from geometric_lib.utils import distance

# Create a circle with a radius of 5
circle = Circle(5)
circle_area = circle.area()
circle_perimeter = circle.perimeter()

# Create a rectangle with width 4 and height 6
rectangle = Rectangle(4, 6)
rectangle_area = rectangle.area()
rectangle_perimeter = rectangle.perimeter()

# Calculate the distance between two points
point1 = (1, 2)
point2 = (4, 6)
distance_between_points = distance(point1, point2)
```
## Commits hashes:
```python
- 1st comit: d7f6500e3f60fabf6e5b34a775e32c7c2cc1f159
- 2nd commit: c36612c5975a3cd8fcfd2b06ed7c636efb725de1
- 3rd commit: 1b2700c19ba0af1b43d71865c85bcc18a0c1bc84 (new README)
