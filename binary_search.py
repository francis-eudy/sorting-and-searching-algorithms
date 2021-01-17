def binary_search(list_, item):
    """
    :param list_: list to be searched
    :param item: item to be searched for
    :return: boolean True if item in list else False
    """
    first = 0
    last = len(list_) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if list_(midpoint) == item:
            return True
        else:
            if item < list_[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return False
