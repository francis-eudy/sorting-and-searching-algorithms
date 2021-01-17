def merge_sort(list_):
    if len(list_) > 1:
        mid = len(list_) // 2
        left = list_[:mid]
        right = list_[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(list_, left, right)
    return list_


def merge(merge_list, left, right):
    idx, left_idx, right_idx = 0, 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merge_list[idx] = left[left_idx]
            left_idx += 1
        else:
            merge_list[idx] = right[right_idx]
            right_idx += 1
        idx += 1

    while left_idx < len(left):
        merge_list[idx] = left[left_idx]
        idx += 1
        left_idx += 1

    while right_idx < len(right):
        merge_list[idx] = right[right_idx]
        idx += 1
        right_idx += 1
    return merge_list
