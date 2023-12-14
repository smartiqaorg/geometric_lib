import argparse
import importlib
import inspect
import os
import sys


# Get the current file's directory path
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the path to the directory containing the potential modules
circle_module_path = os.path.join(current_dir, '../')
# Let the system know about this path
sys.path.append(circle_module_path)

# Mapping of functions to their required arguments - [argument_name, function_argument_name]
functions = {
    'circle': {
        'area': [['radius', 'r']],
        'perimeter': [['radius', 'r']]
    },

    'rectangle' : {
        'area': [['width', 'a'], ['height', 'b']],
        'perimeter': [['width', 'a'], ['height', 'b']]
    },

    'square' : {
        'area': [['length', 'a']],
        'perimeter': [['length', 'a']]
    },

    'triangle' : {
        'area': [['length', 'a'], ['height', 'h']],
        'perimeter': [['side1', 'a'], ['side2', 'b'], ['side3', 'c']]
    },
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run manual tests', allow_abbrev=False)

    # common required arguments
    parser.add_argument('module_name', help='Name of the module or class')
    parser.add_argument('function_name', help='Name of the function to test')

    # function arguments
    parser.add_argument('--radius', type=float)
    parser.add_argument('--width', type=float)
    parser.add_argument('--height', type=float)
    parser.add_argument('--length', type=float)

    parser.add_argument('--side1', type=float)
    parser.add_argument('--side2', type=float)
    parser.add_argument('--side3', type=float)

    # common optional arguments
    parser.add_argument('--expected', help="Expected result")

    non_func_args = ['module_name', 'function_name', 'expected']

    args = parser.parse_args()
    args_dict = vars(args)

    # Accessing parsed arguments
    module_name = args.module_name
    function_name = args.function_name

    if module_name not in functions or function_name not in functions[module_name]:
        print("Invalid module name or function name")
    else:
        required_args = {t[0] : t[1] for t in functions[module_name][function_name]}
        provided_args = {k: v for k, v in args_dict.items() if v is not None and k not in non_func_args}

        if set(required_args.keys()) != set(provided_args.keys()):
            print(f"Required arguments for '{function_name}' function are missing or invalid")
        else:
            function_args = {ra[1]: provided_args[ra[0]] for ra in required_args.items()}

            try:
                module = importlib.import_module(module_name)
                func = getattr(module, function_name)

                result = func(**function_args)
                print(f"Result of {module_name}.{function_name}: {result}")

                if (args_dict['expected'] is not None):
                    assertion_result = result == float(args_dict['expected'])
                    print(f"Assertion result({result} == {args_dict['expected']}): {assertion_result}")

            except ImportError:
                print(f"Module '{module_name}' not found")
            except AttributeError:
                print(f"Function '{function_name}' not found in '{module_name}'")