

def find(lst, x):
    """
    Function that finds the index of element x in list lst recursively. If x is not in lst, it returns -1
    :param lst: list
    :param x: element that needs to be found
    :return: integer representing the index of x in lst, or -1 if x not in lst
    """
    if not lst:
        return -1
    if lst[0] == x:
        return 0
    else:
        y = find(lst[1:], x)
        return 1 + y if y > -1 else -1


a = [1, 2, 3, 4, 5, 6, 7, 8]
print(find(a, 7))
