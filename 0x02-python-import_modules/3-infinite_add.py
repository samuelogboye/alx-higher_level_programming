#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = sys.argv[1:]

    sum = 0
    for i, arg in enumerate(argc, start=1):
        sum += int(arg)
    print(sum)
