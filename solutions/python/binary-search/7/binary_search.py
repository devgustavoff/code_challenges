def find(search_list, value):

    search_list = sorted(search_list)

    if value not in search_list:
        raise ValueError("value not in array")
    
    left = 0
    right = len(search_list) - 1
    target = 0

    while left <= right:
        mid = (left + right) // 2
        if search_list[mid] == value:
            target = mid
            break
        elif value > search_list[mid]:
            left = mid + 1
        elif value < search_list[mid]:
            right = mid - 1
    
    return target