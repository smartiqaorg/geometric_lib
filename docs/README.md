# Geometric Library

This Python code defines a library of functions for calculating the area and perimeter of various geometric shapes. It includes calculations for circles, rectangles, squares and triangles.

## Functions

## Circle Calculations

### `area(r)`
Calculates the area of a circle.
* **Parameters:** r: The radius of the circle (a numerical value).
* **Returns:** The area of the circle (a numerical value).
* **Example:**
  import math
  area_of_circle = area(5)
  print(f"The area of a circle with radius 5 is: {area_of_circle}")
  # Output: The area of a circle with radius 5 is: 78.53981633974483

### `perimeter(r)`
Calculates the perimeter (circumference) of a circle.
* **Parameters:** r: The radius of the circle (a numerical value).
* **Returns:** The perimeter of the circle (a numerical value).
* **Example:**
  perimeter_of_circle = perimeter(5)
  print(f"The perimeter of a circle with radius 5 is: {perimeter_of_circle}")
  # Output: The perimeter of a circle with radius 5 is: 31.41592653589793

## Square Calculations

### `area(a)`
Calculates the area of a square.
* **Parameters:** a: The length of one side of the square (a numerical value).
* **Returns:** The area of the square (a numerical value).
* **Example:**
  area_of_square = area(5)
  print(f"The area of a square with sides of 5 is: {area_of_square}")
  # Output: The area of a square with sides of 5 is: 25

### `perimeter(a)`
Calculates the perimeter of a square.
* **Parameters:** a: The length of one side of the square (a numerical value).
* **Returns:** The perimeter of the square (a numerical value).
* **Example:**
  perimeter_of_square = perimeter(5)
  print(f"The perimeter of a square with sides of 5 is: {perimeter_of_square}")
  # Output: The perimeter of a square with sides of 5 is: 20

## Rectangle Calculations

### `area(a, b)`
Calculates the area of a rectangle.
* **Parameters:** a: The length of the rectangle, b: The width of the rectangle.
* **Returns:** The area of the rectangle.
* **Example:**
  area_of_rectangle = area(5, 10)
  print(f"The area of a rectangle with sides 5 and 10 is: {area_of_rectangle}")
  # Output: The area of a rectangle with sides 5 and 10 is: 50

### `perimeter(a, b)`
Calculates the perimeter of a rectangle.
* **Parameters:** a: The length of the rectangle, b: The width of the rectangle.
* **Returns:** The perimeter of the rectangle.
* **Example:**
  perimeter_of_rectangle = perimeter(5, 10)
  print(f"The perimeter of a rectangle with sides 5 and 10 is: {perimeter_of_rectangle}")
  # Output: The perimeter of a rectangle with sides 5 and 10 is: 30

## Triangle Calculations

### `area(a, h)`
Calculates the area of a triangle.
* **Parameters:** a: The base of the triangle, h: The height of the triangle.
* **Returns:** The area of the triangle.
* **Example:**
  area_of_triangle = area(5, 10)
  print(f"The area of a triangle with base 5 and height 10 is: {area_of_triangle}")
  # Output: The area of a triangle with base 5 and height 10 is: 25

### `perimeter(a, b, c)`
Calculates the perimeter of a triangle.
* **Parameters:** a, b, c: The lengths of the three sides of the triangle.
* **Returns:** The perimeter of the triangle.
* **Example:**
  perimeter_of_triangle = perimeter(3, 4, 5)
  print(f"The perimeter of a triangle with sides 3, 4, 5 is: {perimeter_of_triangle}")
  # Output: The perimeter of a triangle with sides 3, 4, 5 is: 12
  Documentation Completed