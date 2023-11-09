# Math formulas for positive integers, realised in lib
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah/2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2 * (a + b)
- Square: P = 4a
- Triangle: P = a + b + c

# Files with descriptions of functions and examples
## [circle.py](https://github.com/tamerland05/geometric_lib/blob/main/circle.py)
### area(r) : Get a Radius of circle and return his area.
example of call: area(10) = 314 -- same with -- S = 3,14 * 10^2 = 314 

### perimeter(r) : Get a Radius of circle and return his perimeter.
example of call: perimeter(10) = 68,2 -- same with -- P = 2 * 3,14 * 10 = 62,8

## [rectangle.py](https://github.com/tamerland05/geometric_lib/blob/main/rectangle.py)
### area(a, b) : Get height a and weight b of rectangle and return his area.
example of call: area(5, 4) = 20 -- same with -- S = a * b = 20

### perimeter(a, b) : Get height: a and weight: b of rectangle and return his perimeter.
example of call: perimeter(5, 4) = 18 -- same with -- R = 2 * (a + b) = 18

## [square.py](https://github.com/tamerland05/geometric_lib/blob/main/square.py)
### area(a, b) : Get side of square and return his area.
example of call: area(7) = 49 -- same with -- S = 7^2 = 49

### perimeter(a, b) : Get side of square and return his perimeter.
example of call: perimeter(7) = 28 -- same with -- P = 4 * 7 = 28

## [triangle.py](https://github.com/tamerland05/geometric_lib/blob/main/triangle.py)
### area(a, h) : Get side of triangle and height lowered onto her and return area.
example of call: area(2, 8) = 8 -- same with -- S = 2 * 8 / 2 = 8

### perimeter(a, b, c) : Get sides of triangle and return his perimeter.
example of call: perimeter(2, 3, 4) = 9 -- same with -- P = 2 + 3 + 4 = 9

# History of project with hashes
74e38b4931e5b59eda2f40231b80677cae13d581 (HEAD -> main, origin/main, origin/HEAD) all right, this is last commit

ab47decada28da763e91bd260485918a32eaac42 Error of calculating perimeter in rectangle.py was fixed

4eeae320f01baa3467584e9592ecd726b690bed9 Laba1 add rectangle.py

# Unit tests are available for the proposed features
You can find tests to check the correct operation of the declared functions on various data sets

[unittests_for_circle.py](https://github.com/tamerland05/geometric_lib/blob/main/unittests_for_circle.py)

[unittests_for_rectangle.py](https://github.com/tamerland05/geometric_lib/blob/main/unittests_for_rectangle.py)

[unittests_for_square.py](https://github.com/tamerland05/geometric_lib/blob/main/unittests_for_square.py)

[unittests_for_triangle.py](https://github.com/tamerland05/geometric_lib/blob/main/unittests_for_triangle.py)