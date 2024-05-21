#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = set(my_list)

    sum = 0

    for i in range(0, len(new_list)):
        sum = sum + new_list[i]
