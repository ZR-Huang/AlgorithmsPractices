# -*-coding:utf-8 -*-

# 在数组中查找最小元素的索引
def findSmallest(arr):
    smallest = arr[0]   # 存储最小的值
    smallestIndex = 0   # 存储最小元素的索引
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallestIndex = i
    return smallestIndex

# 选择排序
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallestIndex = findSmallest(arr=arr)
        newArr.append(arr.pop(smallestIndex))
    return newArr

Arr = [5, 3, 6, 2, 10]
print(selectionSort(Arr))
