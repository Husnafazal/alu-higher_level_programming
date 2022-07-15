#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) > 0:
        return max(my_list)
        my_list.sort()
        return my_list[-1]
    else:
        return None
