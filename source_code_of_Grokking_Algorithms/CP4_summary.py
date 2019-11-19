# -*- coding:utf-8 -*-

# 递归计算列表元素数
def count(arr):
    if not arr:     # 列表为空，对应布尔值为False
        return 0
    else:
        arr.pop()
        return 1 + count(arr=arr)

# 书上参考答案
def countAns(arr):
    if arr == []:
        return 0
    return list[0] + count(arr[1:])

# 递归计算列表总和
def summary(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr.pop()
    else:
        return arr.pop() + summary(arr=arr)

# 书上参考答案
def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])

# 递归求出列表中最大的数字
def findMax(arr):
    if len(arr) == 1:
        return arr.pop()
    else:
        maxValue = arr.pop()
        # print('\n','debug-------',maxValue)
        result = findMax(arr=arr)
        return maxValue if maxValue > result else result

# 书上参考答案
def max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    subMax = max(arr[1:])
    return arr[0] if arr[0] > subMax else subMax

array = [2, 4, 6, 3, 5, 10]
print('\n',u'列表元素个数：', count(arr=array[:]))
print('\n',u'列表求和结果：', summary(arr=array[:]))
print('\n',u'最大值：', findMax(arr=array[:]))
