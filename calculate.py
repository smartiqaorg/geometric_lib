import circle
import square
import triangle
import rectangle


figs = ['circle', 'square', 'triangle', 'rectangle']
funcs = ['perimeter', 'area']
sizes = {'area-triangle': 3, 'perimeter-triangle': 3,
		 'area-rectangle': 2,'perimeter-rectangle': 2}

def calc(fig, func, size):
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 3 for triangle, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)



