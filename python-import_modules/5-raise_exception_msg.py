def divide_numbers(a, b):
    if b == 0:
        raise_exception_msg("Cannot divide by zero!")
    return a / b

try:
    result = divide_numbers(10, 0)
except NameError as e:
    print("Error:", e)
