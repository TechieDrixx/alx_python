for first_digits in range(0, 10):
    for last_digits in range( first_digits + 1, 10):
        print("{:d}{:d}".format(first_digits, last_digits), end=", " if last_digits < 9 else "\n")
