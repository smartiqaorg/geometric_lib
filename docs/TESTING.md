# ***Geometric Lib Testing***

## Goals and objectives of testing

- Сhecking *functionality* of functions
- Validation check on **correct** geometric values

## Description of the product being tested

- The product must contain functions for calculating areas and perimeters for triangle, square, circle and rectangle
- The product is **not** required to contain verification of the validity of the transmitted data
- The product must calculate areas and perimeters *arithmetically correctly* using the *correct formulas*

## Test area

1. **circle.py**
    - function *area(r)*
    - function *perimeter(r)*
2. **rectangle.py**
    - function *area(a, b)*
    - function *perimeter(a, b)*
3. **square.py**
    - function *area(a)*
    - function *perimeter(a)*
4. **triangle.py**
    - function *area(a, h)*
    - function *perimeter(a, b, c)*

## Testing strategy

| type                        | selected                                                                                                    |
|-----------------------------|-------------------------------------------------------------------------------------------------------------|
| Test Levels by detalization | **Unit** testing                                                                                            |
| Types of testing            | Evaluate the **functional characteristics** of software quality: completeness, correctness, appropriateness |
| Types of functional testing | Functional **correctness** testing                                                                          |
| Test methods                | **Black-box** testing                                                                                       |
| Testing Techniques          | Boundary value analysis, Use Case Testing                                                                   |

## Acceptance Criteria

Functions must **correctly count** and **return** values, taking **correct geometric values**

## Expected results

When testing, **discrepancies** with the expected result will be **output** to the console. Or the verdict is **OK** if all tests
are passed.
