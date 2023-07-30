import sys

def print_arguments(args):
    num_arguments = len(args) - 1

    print("Number of argument(s):", num_arguments, end=' ')
    print("argument" if num_arguments == 1 else "arguments", end=' ')
    print(":" if num_arguments > 0 else ".", end='\n')

    for i in range(1, num_arguments + 1):
        print(i, ":", args[i])

if __name__ == "__main__":
    print_arguments(sys.argv)
