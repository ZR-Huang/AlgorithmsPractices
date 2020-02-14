def _quicksort_(nums, left, right) -> None:
    if left >= right:
        return
    
    pivot_index = partition(nums, left, right)
    _quicksort_(nums, left, pivot_index-1)
    _quicksort_(nums, pivot_index+1, right)


def partition(nums, start, end) -> int:
    l = r = start
    while r < end:
        if nums[r] <= nums[end]:    # choose the last element as pivot
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
        r += 1
    nums[l], nums[end] = nums[end], nums[l]
    return l

def quicksort(nums):
    _quicksort_(nums, 0, len(nums)-1)


numbers = [8, 4, 2, 2, 1, 7, 10, 5]
quicksort(numbers)
print(numbers)