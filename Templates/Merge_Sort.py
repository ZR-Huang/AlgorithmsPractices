def merge(left, right):
    tmp, i, j = [], 0, 0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            tmp.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            j += 1
    
    if i < len(left):
        tmp += left[i:]
    if j < len(right):
        tmp += right[j:]
    return tmp

def merge_sort(arr, l, r):
    if l == r:
        return arr[l:r+1]
    
    mid = l + (r-l) // 2
    left = merge_sort(arr, l, mid)
    right = merge_sort(arr, mid+1, r)

    res = merge(left, right)
    return res

arr = [8, 4, 2, 2, 1, 7, 10, 5]
print(merge_sort(arr, 0, len(arr)-1))