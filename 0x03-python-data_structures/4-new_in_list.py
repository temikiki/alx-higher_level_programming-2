#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list[:]
    elif idx >= my_list:
        return my_list[:]
    else:
        new_list = my_list[:]
        my_list = element
        return my_list
