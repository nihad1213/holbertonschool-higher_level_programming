#!/usr/bin/python3

def common_elements(set_1, set_2):
    common_element = {}

    for i in set_1:
        if i in common_element:
            common_element[i] += 1
        else:
            common_element[i] = 1
 
    for i in set_2:
        if i in common_element:
            common_element[i] += 1
        else:
            common_element[i] = 1

    common_element_ = [i for i in common_element if common_element[i] == 2]
    if len(common_element_) > 0:
        return common_element_
    else:
        return []
