for numbers in range(100):
    print("{:02}".format(numbers), end=", " if numbers < 99 else "\n")
