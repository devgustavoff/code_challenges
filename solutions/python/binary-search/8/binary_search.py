def find(search_list, value):

    search_list = sorted(search_list)
    
    left = 0
    right = len(search_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if search_list[mid] == value:
            return mid
        elif value > search_list[mid]:
            left = mid + 1
        elif value < search_list[mid]:
            right = mid - 1
    else:
        raise ValueError("value not in array")