# test_script.py

def add_numbers(a, b):
    # Variable name 'sum' is a built-in function, better to avoid
    sum = a + b
    return sum

def greet(name):
    # Missing function docstring (Pylint warning)
    print(f"Hello {name}")

if __name__ == "__main__":
    result = add_numbers(5, 3)
    greet("Michael")
    print(result)  # This will print the sum
