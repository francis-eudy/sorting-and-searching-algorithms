def linear_search(list_, item):
    """
    :param list_: list to be searched
    :param item: item to be searched for
    :return: boolean True if item in list, else False
    """
    idx = 0
    while idx < len(list_):
        if list_[idx] == item:
            return True
        else:
            idx += 1
    return False
