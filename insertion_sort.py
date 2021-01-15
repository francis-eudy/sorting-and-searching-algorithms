#!/venv/bin/python

def insertion_sort(list_):
    # iterate over all elements
    for i in range(1, len(list_)):
        j = i - 1
        # insert current element into correct index
        current_element = list_[i]
        while (list_[j] > current_element) and (j >= 0):
            # loop breaks at 0 index or if current element > element to index - 1
            list_[j+1] = list_[j]
            j = j - 1
        list_[j+1] = current_element
    return list_
