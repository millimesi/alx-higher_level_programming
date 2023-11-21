#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    div = 0
    new = []
    i = 0
    while i < list_length:
        try:
            div = my_list_1[i] / my_list_2[i]
            new.append(div)
            i += 1
        except TypeError:
            i += 1
            div = 0
            new.append(div)
            print("wrong type")
        except ZeroDivisionError:
            i += 1
            div = 0
            new.append(div)
            print("division by 0")
        except IndexError:
            div = 0
            new.append(div)
            i += 1
            print("out of range")
        finally:
            if i == list_length:
                return new
