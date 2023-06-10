def divisible_by_2(my_list=[]):
    """A function that finds all multiples of two in a list"""

    for i in my_list:
        if i % 2 == 0:
            return True
        else:
            return False
