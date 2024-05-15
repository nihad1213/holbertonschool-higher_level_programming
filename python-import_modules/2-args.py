#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    numberOfArguments = len(sys.argv) - 1
    if numberOfArguments == 0:
        print("0 arguments.")
    elif numberOfArguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(numberOfArguments))
    for i in range(numberOfArguments):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))

