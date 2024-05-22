#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    copy_dic = a_dictionary.copy()
    for i, j in copy_dic.items():
        copy_dic[i] = j * 2
    return copy_dic
