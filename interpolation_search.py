def interpolation_search(list_, item):
    """
    :param list_: list to be searched
    :param item: element to be searched for
    :return: True if element is in list else False
    """
    idx0 = 0
    idxn = (len(list_) - 1)
    while idx0 < idxn and list_[idx0] <= item <= list_[idxn]:
        # Find the Mid Point
        mid = idx0 + int(((float(idxn - idx0) / (list_[idxn] - list_[idx0])) * (item - list_[idx0])))
        # Compare the value at the mid point with the search item value
        if list_[mid] == item:
            return True
        if list_[mid] < item:
            idx0 = mid + 1
    return False
