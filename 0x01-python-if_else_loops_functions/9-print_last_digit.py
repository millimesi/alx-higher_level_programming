#!/usr/python3
def print_last_digit(number):
    if number < 0:
        reminder = (-1 * number) % 10
    else:
        reminder = number % 10
    print(f"{reminder}", end="")
    return reminder
