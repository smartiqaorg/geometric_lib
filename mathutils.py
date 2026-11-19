def gcd(a,b):
    '''
    Вычисляет наибольший общий делитель двух чисел (алгоритм Евклида).

    Ввод: a (int) - число 1, b (int) - число 2
    Вывод: gcd (int) - наибольший общий делитель

    Пример использования:
    gcd(12,18) = 6
    '''
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a,b):
    '''
    Вычисляет наименьшее общее кратное двух чисел.

    Ввод: a (int) - число 1, b (int) - число 2
    Вывод: lcm (int) - наименьшее общее кратное

    Пример использования:
    lcm(4,6) = 12
    '''
    return abs(a * b) // gcd(a, b)

def factorial(n):
    '''
    Вычисляет факториал числа.

    Ввод: n (int) - число
    Вывод: factorial (int) - факториал числа n

    Пример использования:
    factorial(5) = 120
    '''
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def is_prime(n):
    '''
    Проверяет, является ли число простым.

    Ввод: n (int) - число
    Вывод: is_prime (bool) - True, если число простое, иначе False

    Пример использования:
    is_prime(7) = True
    '''
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True