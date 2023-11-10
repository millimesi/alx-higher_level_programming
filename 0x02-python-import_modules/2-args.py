#!/usr/bin/python3
import sys

if __name__ == "__main__":
    print("{}".format(len(sys.argv) -1), end=" ")
    if len(sys.argv) - 1 == 1:
        print("argument", end="")
    else:
        print("arguments", end="")
    if len(sys.argv) -1 == 0:
        print(".")
    else:
        print(":")
    for i in range(1,len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
