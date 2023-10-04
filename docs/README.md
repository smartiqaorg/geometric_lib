# Math formulas
## Area

  - Circle: S = πR²
    - Rectangle: S = ab
- Square: S = a²
- Triangle: S = (a*h)/2
  
```
  import math


def area(r):
    '''Принимает радиус r, возвращает площадь круга с радиусом r'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает радиус r, возвращает периметр круга с радиусом r'''
    return 2 * math.pi * r
```


## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Solution description : 
## Area

- Circle: Takes radius r, returns the product of r times r times pi. Example: takes r=4, returns 50.265482457...
- Rectangle: Takes sides a and b, returns the product of a and b. Example: takes a=3 and b=4, returns 12.
- Square: Takes side a, returns the product of a times a. Example: takes a=5, returns 25.
- Triangle: Takes side a and the height h, returns the half of the product of a times h. Example: takes a=2 and h=4, returns 4.

## Perimeter
- Circle: Takes radius r, returns the product of pi times a times 2.
- Rectangle: Takes sides a and b, returns the sum of a and b times 2.
- Square: Takes side a, returns the product of a times 4.
- Triangle: Takes three sides a, b and c, returns their sum.

# Example
## Area

- Circle: takes r=4, returns 50.265482457...
- Rectangle: takes a=3 and b=4, returns 12.
- Square: takes a=5, returns 25.
- Triangle: takes a=2 and h=4, returns 4.

## Perimeter
- Circle: takes r=4, returns 25.13274122871835
- Rectangle: takes a=3 and b=4, returns 14.
- Square: takes a=5, returns 20.
- Triangle: takes a=2, b=3 and c=4, returns 9.

# History of project changes with commit hashes

commit 02ed52f8ae03bd08c598edb7f14152d4505c2569 (origin/main, origin/HEAD, main)
Author: mirnih <milana.archakova.06@mail.ru>
Date:   Sat Sep 30 16:37:34 2023 +0300

    added triangle.py

commit fc6dcf18e42bb83a7d456d1534a9254f3fc5ebbf
Author: mirnih <milana.archakova.06@mail.ru>
Date:   Sat Sep 30 16:26:49 2023 +0300

    modified perimeter in rectangle.py

commit 93b02e49d3d9b0d0ae9edd522ac0638ac60fb380
Author: mirnih <milana.archakova.06@mail.ru>
Date:   Sat Sep 30 16:25:52 2023 +0300

    added rectangle.py

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added

02ed52f (origin/main, origin/HEAD, main) added triangle.py
fc6dcf1 modified perimeter in rectangle.py
93b02e4 added rectangle.py
d078c8d L-03: Docs added
8ba9aeb L-03: Circle and square added
