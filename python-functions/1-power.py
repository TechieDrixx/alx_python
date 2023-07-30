def pow(a, b):
    # Initialize the result to 1 since anything raised to the power of 0 is 1
    result = 1
    
    # Handle the case when the exponent is negative
    if b < 0:
        a = 1 / a
        b = -b

    # Multiply a to the result 'b' times
    for _ in range(b):
        result *= a
        
    return result
