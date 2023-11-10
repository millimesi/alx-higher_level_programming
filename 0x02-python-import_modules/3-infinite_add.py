#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv
    result = 0
    for i in range(1, len(args)):
        result += int(args[i])
    print(result)