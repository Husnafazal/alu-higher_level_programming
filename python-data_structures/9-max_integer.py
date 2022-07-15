#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) > 0:
        my_list.sort()
        print(max(my_list))
    else:
        return None
        
max_integer([1, 90, 2, 13, 34, 5, -13, 3])
