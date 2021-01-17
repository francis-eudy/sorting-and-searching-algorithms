def shell_sort(list_):
    distance = len(list_) // 2
    while distance > 0:
        for i in range(distance, len(list_)):
            temp = list_[i]
            j = i

            while j >= distance and list_[j - distance] > temp:
                list_[j] = list_[j - distance]
                j = j - distance
            list_[j] = temp
        distance = distance // 2
    return list_
