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
## **Commit history**
---
| Commit date | Hash | Features |
|--|--|---------|
|March 4 2021| 8ba9aeb3cea847b63a91ac378a2a6db758682460|Circle and square added|
|March 4 2021|d078c8d9ee6155f3cb0e577d28d337b791de28e2|Docs added|
|November 16 2023|b81dc7f9cf6074ed2e51d91770e5838d3f6128e5|feat: add rectangle perimeter and are functions|
|November 16 2023|50277728bf26f27c90100920dd13cdddd2c3451b|fix: error in perimeter function|
|November 16 2023|ad53b7b03b772487309c163af1385c8cb63332fe|docs: add documentation for all functions|
