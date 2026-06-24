"""This module solved the binary search exercism"""
def find(search_list, value):
    """This function is a binary search algorithm."""

    search_list = sorted(search_list)
    
    left = 0
    right = len(search_list) - 1

    while left <= right:
        mid = (left + right) // 2

        if search_list[mid] == value:
            return mid
        
        if value > search_list[mid]:
            left = mid + 1
        elif value < search_list[mid]:
            right = mid - 1
    
    raise ValueError("value not in array")