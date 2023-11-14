# Geometric Lib
## Description
Geometric lib is a library, which сontains tools for mathematical calculations in your projects, such as calculating the area and perimeter of geometric shapes.
## Math formulas
### _Area_
 - Circle: S = πR²
 - Rectangle: S = ab
 - Square: S = a²
### _Perimeter_
 - Circle: P = 2πR
 - Rectangle: P = 2a + 2b
 - Square: P = 4a
## Description of functions

### _Circle_
#### 1. Area
`area(r)`

This function calculates the area of a circle based on the given radius.
Parameters: 
- `r` (float): The radius of the circle.
```python
def area(r):  
    return math.pi * r * r
````
Where:
- `r` - given radius
- `math.pi` - math constant
#### 2.  Perimeter
`perimeter(r) `

This function calculates the perimeter of a circle based on the given radius.
Parameters: 
- `r` (float): The radius of the circle.
```python
def perimeter(r):  
    return 2 * math.pi * r
````
Where:
`r` - given radius
`math.pi` - math constant

### _Rectangle_
#### 1. Area
`area(a, b)`

This function calculates the area of a rectangle based on its length `a` and width `b`.
Parameters: 
-  `a` (float): The length of the rectangle.
 -  `b` (float): The width of the rectangle.
```python
def area(a, b):   
    return a * b
````
Where:
`a` - given length
`b` - given width
#### 2.  Perimeter
`perimeter(a, b)`

This function calculates the perimeter of a rectangle based on its length `a` and width `b`.
Parameters: 
-  `a` (float): The length of the rectangle.
 -  `b` (float): The width of the rectangle.
```python
def perimeter(a, b):   
    return (a + b) * 2
````
Where:
`a` - given length
`b` - given width

### _Square_
#### 1. Area
`area(a)`

This function calculates the area of a square based on the length of its side `a`.
Parameters: 
- `a` (float): The length of a side of the square.
```python
def area(a):  
    return a * a
````
Where:
a - given side
#### 2. Perimeter
`perimeter(a)`

This function calculates the perimeter of a square based on the length of its side `a`.
Parameters: 
- `a` (float): The length of a side of the square.
```python
def perimeter(a):  
    return 4 * a
````
Where:
a - given side

### _Triangle_
#### 1. Area
`area(a, h)`

 This function calculates the area of a triangle based on its base length `a` and height `h`. 
 Parameters: 
 -  `a` (float): The length of the base of the triangle. 
 -  `h` (float): The height of the triangle.
```python
def perimeter(a):  
    return 4 * a
````
Where:
a - given base
h - given height

#### 2. Perimeter
#### `perimeter(a, b, c)`

Description: This function calculates the perimeter of a triangle based on its side lengths `a`, `b`, and `c`.

Parameters:

-   `a` (float): The length of one side of the triangle.
-   `b` (float): The length of another side of the triangle.
-   `c` (float): The length of the third side of the triangle.

```python
def perimeter(a, b, c):   
    return a + b + c
````
Where:
a - first given side
b - second given side
c - third given side

 ## Examples of using functions
 ### _Circle_
#### 1. Area
`area(r)`
```python 
from circle import area 
radius = 5 
circle_area = area(radius) 
print(f"The area of the circle with radius {radius} is {circle_area:.2f}")
```
#### 2.  Perimeter
`perimeter(r) `
```python
from circle import perimeter
radius = 5
circle_perimeter = perimeter(radius)
print(f"The perimeter of the circle with radius {radius} is {circle_perimeter:.2f}")
```
### _Rectangle_
#### 1. Area
`area(a, b)`
```python 
from rectangle import area 
length = 4 
width = 6 
rectangle_area = area(length, width) 
print(f"The area of the rectangle with length {length} and width {width} is {rectangle_area}")
```
#### 2.  Perimeter
`perimeter(a, b)`
```python
from rectangle import perimeter 
length = 4 
width = 6 
rectangle_perimeter = perimeter(length, width) 
print(f"The perimeter of the rectangle with length {length} and width {width} is {rectangle_perimeter}")
```
### _Square_
#### 1. Area
`area(a)`
```python
from square import area 
side = 4 
square_area = area(side) 
print(f"The area of the square with side length {side} is {square_area}")
```
#### 2. Perimeter
`perimeter(a)`
```python
from square import perimeter 
side = 4 
square_perimeter = perimeter(side) 
print(f"The perimeter of the square with side length {side} is {square_perimeter}")
```
### _Triangle_
#### 1. Area
`area(a, h)`
```python
from triangle import area 
base = 6 
height = 4 
triangle_area = area(base, height) 
print(f"The area of the triangle with base {base} and height {height} is {triangle_area}")
```
#### 2. Perimeter
#### `perimeter(a, b, c)`
```python
from triangle import perimeter 
side_a = 3 
side_b = 4 
side_c = 5 
triangle_perimeter = perimeter(side_a, side_b, side_c) 
print(f"The perimeter of the triangle with sides {side_a}, {side_b}, and {side_c} is {triangle_perimeter}")
```
## Commits and hash
```
* commit 6f3bb9892e7a460e8050737220d2b5742a5fc145 (HEAD -> main)
| Date:   Tue Oct 3 22:25:44 2023 +0300
|
|     Descriptions of all functions have been added
|
* commit 0b495f0cb770967fdd8db59cda19c25a3ed239c3 (origin/main, origin/HEAD)
| Date:   Sun Sep 10 15:31:05 2023 +0300
|
|     Fixed rectangle.py
|
* commit 961484b6351f6a4d9f079704755cb9f746e9eaf8
| Date:   Sun Sep 10 15:27:43 2023 +0300
|
|     Added rectangle.py
|
* commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
| Date:   Thu Mar 4 14:55:29 2021 +0300
|
|     L-03: Docs added
|
* commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
  Date:   Thu Mar 4 14:54:08 2021 +0300

      L-03: Circle and square added
 ```

## Testing

We use the `unittest` module to test the functions for calculating the area and perimeter of each shape.

### Tests code

#### 1. circle_test.py:
```python
import unittest
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_zero_radius(self):
        res_area = area(0)
        res_perimeter = perimeter(0)
        self.assertEqual(res_area, 0)
        self.assertEqual(res_perimeter, 0)

    def test_valid_radius(self):
        res_area = area(5)
        res_perimeter = perimeter(5)
        self.assertEqual(res_area, 78.54)
        self.assertEqual(res_perimeter, 31.42)

if __name__ == '__main__':
    unittest.main()
```
#### 2. rectangle_test.py:
```python
import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_zero_dimensions(self):
        res_area = area(0, 0)
        res_perimeter = perimeter(0, 0)
        self.assertEqual(res_area, 0)
        self.assertEqual(res_perimeter, 0)

    def test_valid_dimensions(self):
        res_area = area(4, 5)
        res_perimeter = perimeter(4, 5)
        self.assertEqual(res_area, 20)
        self.assertEqual(res_perimeter, 18)

if __name__ == '__main__':
    unittest.main()
```

#### 3. square_test.py:

```python
Copy code
import unittest
from geometric_lib.square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_zero_side(self):
        res_area = area(0)
        res_perimeter = perimeter(0)
        self.assertEqual(res_area, 0)
        self.assertEqual(res_perimeter, 0)

    def test_valid_side(self):
        res_area = area(3)
        res_perimeter = perimeter(3)
        self.assertEqual(res_area, 9)
        self.assertEqual(res_perimeter, 12)

if __name__ == '__main__':
    unittest.main()
```

#### 4. triangle_test.py:

```python
import unittest
from geometric_lib.triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_zero_sides(self):
        res_area = area(0, 0, 0)
        res_perimeter = perimeter(0, 0, 0)
        self.assertEqual(res_area, 0)
        self.assertEqual(res_perimeter, 0)

    def test_valid_sides(self):
        res_area = area(3, 4, 5)
        res_perimeter = perimeter(3, 4, 5)
        self.assertEqual(res_area, 6)
        self.assertEqual(res_perimeter, 12)

if __name__ == '__main__':
    unittest.main()
```
### Running Tests

To run all tests, execute the following command in the project's root directory:

```bash
python -m unittest discover -s tests -p "*_test.py"
```
### Test results
#### 1. circle_test.py:

```bash
Ran 2 tests in 0.001s
OK
```

#### 2. rectangle_test.py:

```bash
Ran 2 tests in 0.001s
OK
```

#### 3. square_test.py:

```bash
Ran 2 tests in 0.001s
OK
```

#### 4. triangle_test.py:

```bash
Ran 2 tests in 0.001s
OK
```

### Expected Results
* All tests pass successfully without errors.
* The functions for calculating area and perimeter return correct values.
* In case of passing invalid input data, the functions handle errors correctly.





    

