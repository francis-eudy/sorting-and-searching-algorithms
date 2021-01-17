def selection_sort(list_):
    for fill_slot in range(len(list_) - 1, 0, -1):
        max_index = 0
        for location in range(1, fill_slot + 1):
            if list_[location] > list_[max_index]:
                max_index = location
        list_[fill_slot], list_[max_index] = list_[max_index], list_[fill_slot]
    return list_
