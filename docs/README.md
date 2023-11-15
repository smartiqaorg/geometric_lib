## General description of the solution
__In the course of work, the files rectangle.py and triangle.py
were added to the existing files circle.py and square.py
containing functions for calculating the area and perimeter of figures.
Also in the rectangle.py file an error in the formula has been corrected 
Next, comments containing a description of how the functions work were 
added to the files rectangle.py, triangle.py, square.py.__

---
## Description of functions with examples of calls

## Circle.py
### Function calculating area
###### "Takes a number r and returns the result of squaring it and multiplying it by pi"
    in: 8
    out: 201,06...
def area(r):<br/>
return math.pi * r * r <br/>
### Function calculating perimeter
###### "Takes a number r and returns the result of multiplying it by 2 and multiplying it by pi"
def perimeter(r):<br/>
return 2 * math.pi * r <br/>

    in: 9
    out: 55,54...
---

## Rectangle.py
### Function calculating area
###### "Takes numbers a and b and returns the result of their multiplication"
    in: 4 8
    out: 32
def area(a, b):<br/>
return a*b <br/>
### Function calculating perimeter
###### "Takes numbers a and b and returns the result of their addition and multiplication by 2"
def area(a, b):<br/>
return (a+b)*2 <br/>
    
    in: 4 8
    out: 24
---

## Square.py
### Function calculating area
###### "Takes the number a and returns the result of squaring"
    in: 5
    out: 25
def area(a):<br/> 
return a*a <br/>
### Function calculating perimeter
###### "Takes the number a and returns the result of multiplying it by 4"
def area(a): <br/> 
return 4*a <br/>

    in: 5
    out: 20
---

## Triangle.py
### Function calculating area
###### "Takes numbers a and h and returns the result of their multiplication divided by 2"
    in: 4 10
    out: 7
def area(a, h):<br/>  
return (a*h)/2 <br/>
### Function calculating perimeter
###### "Takes numbers a, b, c and returns the result of their addition"
def area(a, b, c):<br/>
return a+b+c <br/>
    
    in: 4 8 6
    out: 18
---

## Project change history with commit hashes (except for the last entry)
- commit 192d2ca98dc06bdc29dc0a8d2239f821baba0c76
Author: Бушков Никита М3119 <408338@niuitmo.ru>
Date:   Sun Sep 17 21:04:45 2023 +0300
```
add new file rectangle.py
```
- commit 7a31d7e7c7fbb385b31bf79bb4e5fb0f21f89cd3 (HEAD -> new_features_408338, origin/main, origin/HEAD, main)
Author: Бушков Никита М3119 <408338@niuitmo.ru>
Date: Sun Sep 17 21:07:31 2023 +0300
```
fix: fix error in file rectangle.py
```
- commit 4b93d66d38931f75c56f5683e6f47031b41bd140
Author: Бушков Никита М3119 <408338@niuitmo.ru>
Date:   Sat Sep 30 20:33:20 2023 +0300
```
docs: added comment for file rectangle.py
```
- commit 2870cb6b529ac3aca2f23da14adae7199d074521
Author: Бушков Никита М3119 <408338@niuitmo.ru>
Date:   Sat Sep 30 20:48:08 2023 +0300
```
docs: added comment for file square.py
```
-  commit bb906daa65b5f93132edba9d93893e71637ae6aa (HEAD -> documentation_408338, origin/documentation_408338)
Author: Бушков Никита М3119 <408338@niuitmo.ru>
Date:   Sat Sep 30 21:01:59 2023 +0300
```
docs: added comment for file triangle.py
```
- commit 51a67d533f492a6ccad1d08f7b0edbab63218031 (HEAD -> tests_408338)
Author: Bushkov Nikita <408338@niuitmo.ru>
Date: Wed Nov 15 22:45:56 2023 +0300
```
test: added tests for triangle
```
- commit a4a1c3bbbb636a024af7bdfc5fe699cb028459e9
Author: Bushkov Nikita <408338@niuitmo.ru>
Date: Wed Nov 15 22:45:24 2023 +0300
```
test: added tests for square
```
- commit f739551abdcce365ce12352f7e38791537fe451d
Author: Bushkov Nikita <408338@niuitmo.ru>
Date: Wed Nov 15 22:44:40 2023 +0300
```
test: added tests for rectangle
```
- commit cb8579723c62b1a0db356f31dcd24aae7564237b
Author: Bushkov Nikita <408338@niuitmo.ru>
Date: Wed Nov 15 22:44:05 2023 +0300
```
test: added tests for circle
```
---
## Names of automated testing
- circle_test
- rectangle test
- square test
- triangle test
## Automated testing results
- Number of tests - 24
- Number of successful tests - 8
- Number of failed tests - 16


