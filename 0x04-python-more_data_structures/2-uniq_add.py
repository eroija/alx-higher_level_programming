#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set()
    sum = 0

    for i in my_list:
        if i not in unique:
            sum += i
            unique.add(i)
    return sum
