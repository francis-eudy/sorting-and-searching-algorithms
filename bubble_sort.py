#!/venv/bin/python


def bubble_sort(list_):
    last_element_index = len(list_) - 1
    # passes of bubble sort = N
    for pass_ in range(last_element_index, 0, -1):
        # iterate over remaining unsorted elements
        for j in range(pass_):
            # compare elements
            if list_[j] > list_[j+1]:
                # swap elements
                list_[j], list_[j+1] = list_[j+1], list_[j]
    return list_
