# Documentation
A library with useful functions related to geometrical figures
## Math formulas


>    |Figure|Area|Perimeter|
>    |--|--|--|
>    |Circle|πR²|2πR|
>    |Rectangle| ab|2a + 2b|
>    |Square| a²|4a|
>    |Triangle| sh| a + b + c|

## **Usages**
### **Circle**

---

- #### **area(r)** 
Returns area of a circle with radius **r**
```python
r = 5
print(area(r))
# 78.539..
```
- #### **perimeter(r)**
Returns circumference length of a circle with radius **r**
```python
r = 5
print(perimeter(r))
# 31.415...
```

### **Square**
---
- #### **area(a)** 
Returns area of a square with side **a**
```python
a = 5
print(area(a))
# 25
```
- #### **perimeter(a)**
Returns perimeter of a square with side **a**
```python
a = 5
print(perimeter(a))
# 20
```
### **Rectangle**
---
- #### **area(a, b)**
Returns area of a rectangle with sides **a** and **b**
```python
a = 5
b = 6
print(area(a, b))
# 30
```
- #### **perimeter(a, b)**
Returns perimeter of a rectangle with sides **a** and **b**
```python
a = 5
b = 6
print(perimeter(a, b))
# 22
```
### **Triangle**
- #### **area(s, h)**
Returns area of a triangle with side **s** and height **h**
```python
s = 5
h = 6
print(area(s, h))
# 15
```
- #### **perimeter(a, b, c)**
Returns perimeter of a triangle with sides **a**, **b** and **c**
```python
a = 5
b = 6
c = 7
print(perimeter(a, b, c))
# 18
```

# **Tests**

## 1. Goals and objectives of testing
The main goal of testing is to verify that the behavior of the written code corresponds to the expected behavior. It is required that the code successfully passes all tests.

## 2. Description of the product being tested
The behaviour of functions for calculating areas and perimeters of geometric figures should be tested. The functions should return a correct value or an error in case the input parameters are invalid.

## 3. Testing area
- ### Circle.py
    - **area(r)** - function for calculating the area of a circle with *radius* *r*
    - **perimeter(r)** - function for calculating the circumference of a circle with *radius* **r**

- ### Square.py
    - **area(a)** - function for calculating the area of a square with a given *side* length **a**
    - **perimeter(a)** - function for calculating the perimeter of a square with a given *side* length **a**
    
- ### Rectangle.py
    - **area(a, b)** - function for calculating the area of a rectangle with *sides* **a** and **b**
    - **perimeter(r)** - function for calculating the peremeter of a rectangle with *sides* **a** and **b**

- ### Triangle.py
    - **area(s, h)** - function for calculating the area of a triangle with a *side* length of **s** and a *height* length of **h** dropped onto it.
    - **perimeter(a, b, c)** - function for calculating the perimeter of a trinagle with a given *sides* lengths **a**, **b**, **c**

## 4. Testing strategy
Testing is performed using Unit tests in the form of functional testing.

It will be verified whether the values returned by the functions correspond to the expected ones and if exceptions are thrown if values given to the function are invalid (<= 0). 

A total of 3 tests are provided for each function with different input data. (Except for triangle perimeter function which has additional testing whether triangle with this sides is possible)

## 5. Acceptance criteria
All tests must be completed without errors

## 6. Expected results
Major part of tests would end with error, because not all features are currently implemented in functions

## **Commit history**
---
| Commit date | Hash | Features |
|--|--|---------|
|March 4 2021| 8ba9aeb3cea847b63a91ac378a2a6db758682460|Circle and square added|
|March 4 2021|d078c8d9ee6155f3cb0e577d28d337b791de28e2|Docs added|
|November 16 2023|b81dc7f9cf6074ed2e51d91770e5838d3f6128e5|feat: add rectangle perimeter and are functions|
|November 16 2023|50277728bf26f27c90100920dd13cdddd2c3451b|fix: error in perimeter function|
|November 16 2023|ad53b7b03b772487309c163af1385c8cb63332fe|docs: add documentation for all functions|
|November 16 2023|680aac7935f9788e1cce8eaa0ae49674b9541dda|docs: add documentation in README|
|November 24 2023|efb4a0d721c4237cb3e13b69b5e00f8f5b1df464|test: add tests for all modules|
|November 24 2023|docs: fix errors in functions declaration|docs: fix errors in functions declaration|

