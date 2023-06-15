#!/usr/bin/python3
def weight_average(my_list=[]):
    """a function that returns the weighted average of all integers tuple"""
    if not my_list:
        return 0
    upper = [first * second for first, second in my_list]
    lower = [second for _, second in my_list]
    return sum(upper) / sum(lower)
