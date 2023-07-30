def pow(a, b):
    # Check for special cases when the exponent is 0 or 1
    if b == 0:
        return 1
    elif b == 1:
        return a

    # Handle the case when the base is negative and the exponent is positive
    if a < 0 and b > 0:
        return -pow(-a, b)

    # Handle the case when the base is positive and the exponent is negative
    if a > 0 and b < 0:
        return 1 / pow(a, -b)

    # Calculate a to the power of b using a loop
    result = 1
    for _ in range(b):
        result *= a

    return result
