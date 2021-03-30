from math import sqrt

def area(a, b, c):
	p = (a + b + c) / 2
	return sqrt(p*(p-a)*(p-b)*(p-c))


def perimeter(a, b, c):
	return a + b + c
