# Geometric Shapes Library

This Python project is a simple geometric shapes library that provides functions to calculate the area and perimeter 
of four common shapes: Rectangle, Square, Circle, and Triangle.

## Rectangle

### Functions

#### `area(length, width)`
Calculates the area of a rectangle given its length and width.

#### `perimeter(length, width)`
Calculates the perimeter of a rectangle given its length and width.

**Example:**

```python
from rectangle import area, perimeter

length = 5
width = 3

rectangle_area = area(length, width)
rectangle_perimeter = perimeter(length, width)

print(f"Rectangle Area: {rectangle_area}")
print(f"Rectangle Perimeter: {rectangle_perimeter}")
```
## Square

### Functions

#### `area(side_length)`
Calculates the area of a square given the length of its sides.

#### `perimeter(side_length)`
Calculates the perimeter of a square given the length of its sides.

**Example:**

```python
from square import area, perimeter

side_length = 4

square_area = area(side_length)
square_perimeter = perimeter(side_length)

print(f"Square Area: {square_area}")
print(f"Square Perimeter: {square_perimeter}")
```
## Circle

### Functions

#### `area(radius)`
Calculates the area of a circle given its radius.

#### `perimeter(radius)`
Calculates the perimeter of a circle given its radius.

**Example:**

```python
from circle import area, perimeter

radius = 5

circle_area = area(radius)
circle_perimeter = perimeter(radius)

print(f"Circle Area: {circle_area}")
print(f"Circle Circumference: {circle_perimeter}")
```
## Triangle

### Functions

#### `area(base, height)`
Calculates the area of a triangle given its base and height.

#### `perimeter(side1, side2, side3)`
Calculates the perimeter of a triangle given the lengths of its three sides.

**Example:**

```python
from triangle import area, perimeter

base = 6
height = 8
side1 = 3
side2 = 4
side3 = 5

triangle_area = area(base, height)
triangle_perimeter = perimeter(side1, side2, side3)

print(f"Triangle Area: {triangle_area}")
print(f"Triangle Perimeter: {triangle_perimeter}")
```
# Commit History

| Hash      | Commit comment                                   |
|-----------|--------------------------------------------------|
| 8ba9aeb3c | L-03: Circle and square added                    |
| d078c8d9e | L-03: Docs added                                 |
| b9831c8ba | Added file rectangle.py                          |
| e731ca9fe | Fixed mistake rectangle.py                       |
| 598605be6 | Added comments to functions                      |
| 6b376c8d4 | Edited comments in functions                     |
| 69fbaf9b4 | Added manual testing and Unittests for each file |