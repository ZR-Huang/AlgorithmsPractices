def binary_search(start, end, arr, key):
    ret = -1 # if not find, return the index -1
    while start <= end:
        mid = start + ((end-start) >> 1) # if use traditional mean, it might overflows.
        if arr[mid] > key:
            start = mid + 1
        elif arr[mid] < key:
            end = mid + 1
        else:
            ret = mid
            break
    
    return ret