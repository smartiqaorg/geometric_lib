def area(a, h):
    '''
        Accepts triangle height and base side, returns triangle area.

            Parameters:
                a (int) : base side of a triangle
                b (int) : height of a triangle

            Returns:
                a * h / 2 (int) : triangle area

            Example:
                input: 5 10
                output: 25.0
        '''
    return a * h / 2

def perimeter(a, b, c):
    '''
        Accepts triangle sides, returns triangle perimeter.

            Parameters:
                a (int) : side a of a triangle
                b (int) : side b of a triangle
                c (int) : side c of a triangle
            Returns:
                a + b + c : perimeter (int)
        '''
    return a + b + c