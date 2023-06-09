#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = sys.argv[1:]

    if len(argc) == 0:
        print("0 arguments.")
    elif len(argc) == 1:
        print("1 argument:")
        print("1: {}".format(argc[0]))
    else:
        print("{} arguments:".format(len(argc)))
        for i, arg in enumerate(argc, start=1):
            print("{}: {}".format(i, arg))
