#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    argc = sys.argv[1:]

    if len(argc) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>.")
        exit(1)
    else:
        a = int(argc[0])
        b = int(argc[2])
        if argc[1] == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
            exit(0)
        elif argc[1] == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
            exit(0)
        elif argc[1] == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
            exit(0)
        elif argc[1] == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
