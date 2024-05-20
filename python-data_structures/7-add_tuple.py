#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list1 = list(tuple_a)
    list2 = list(tuple_b)

    for i in range(2):
        list1.append(0)
        list2.append(0)

    sum_1 = list1[0] + list2[0]
    sum_2 = list1[1] + list2[1]

    tuple_c = (sum_1, sum_2)

    return tuple_c

