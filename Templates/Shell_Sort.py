def shell_sort(arr):
    length = len(arr)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            j = i
            curr = arr[i]
            while j - gap >= 0 and curr < arr[j-gap]:
                arr[j] = arr[j-gap]
                j = j - gap
            arr[j] = curr
        gap //= 2
    return arr

if __name__ == '__main__':
    arr = [3, 8, 1, 4, 7, 5, 6, 10]
    print(shell_sort(arr))