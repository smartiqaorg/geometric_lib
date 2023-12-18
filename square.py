
def area(a):
    '''
    Accepts square side (int), returns square area (int).

        Example:
            input: 10
            output: 100
    '''
    if a >= 0:
        return a * a
    return 'incorrect input'
    return a * a


def perimeter(a):
    '''
    Accepts square side (int), returns square perimeter (int).

        Example:
            input: 10
            output: 40
    '''
    if (a == int(a) or a == float(a)) and a >= 0:
        return 4 * a
    return 'incorrect input'
    return 4 * a
print(perimeter(-1))
