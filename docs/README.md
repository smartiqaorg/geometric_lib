# Geometric Lib

- ***Calculates the area and perimeter of geometric figures***

## Supports working with:
- circle
- rectangle
- square
- triangle

## Pay attention:
- supports working *ONLY* with positive integers
- in `my_unittest.py` you can find some Unit tests for functions in this library

## Errors you might get and their meaning:
- `Negative Length` means that you have entered negative value
- `Zero Length` means that you have entered zero value
- `Invalid Length` means that you have entered string value
- `Not Integer Length` means that you have entered float value


### 1) Circle
- `def area(r)` receives *the radius* of the circle and returns it's area, calculated by the formula **S = πR<sup>2</sup>**
    > import math \
     result = area(3) \
     print(result) \
  > \
  `28.274333882308138`
- `def perimeter(r)` receives *the radius* of the circle and returns it's perimeter, calculated by the formula **P = 2πR**
    > import math \
     result = perimeter(3) \
     print(result) \
  > \
  `18.84955592153876`

### 2) Rectangle
- `def area(a, b)` receives *the length of sides* of the rectangle and returns it's area, calculated by the formula **S = a * b**
    > result = area(2, 3) \
     print(result) \
  > \
  `6`
- `def perimeter(a, b)` receives *the length of sides* of the rectangle and returns it's perimeter, calculated by the formula **P = 2 * (a + b)**
    > result = perimeter(2, 3) \
     print(result) \
  > \
  `10`

### 3) Square
- `def area(a)` receives *the length of side* of the square and returns it's area, calculated by the formula **S = a<sup>2</sup>**
    > result = area(2) \
     print(result) \
  > \
  `4`
- `def perimeter(a)` receives *the length of side* of the square and returns it's perimeter, calculated by the formula **P = 4 * a**
    > result = perimeter(2) \
     print(result) \
  > \
  `8`

### 4) Triangle
- `def area(a, h)` receives *the length of the triangle base* and *it's height* and returns area, calculated by the formula **S = a * (h / 2)**
    > result = area(5, 4) \
     print(result) \
  > \
  `10`
- `def perimeter(a, b, c)` receives *the length of all triangle's sides*  and returns it's perimeter, calculated by the formula **P = a + b + c**
    > result = perimeter(1, 2, 3) \
     print(result) \
  > \
  `6`


## The history of this project can be tracked by the following commits:

- `update main.yml` *fa14ce8*
- `created main.yml` *8e6dabc*
- `unittests added, exeptions added` *9e89a27*
- `declaration updated` *0b2dc6f*
- `declaration for circle.py fixed, README.md updated` *f829ae1*
- `update README.md` *c6bcee7*
- `delete accidentally added .idea directory` *c743c70*
- `declaration of functions added and README.md` *a77ba4f*
- `README.md modified` *055f7bf*
- `mistake in rectangle.py fixed` *5bfe594*
- `mistake in rectangle.py fixed and new features triangle.py added` *9f08693*
- `new features rectangle.py added` *45f6c37* 
- `L-03: Docs added` *d078c8d* 
- `L-03: Circle and square added` *8ba9aeb*
