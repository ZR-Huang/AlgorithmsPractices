"""
@function:
    the implement of QuickSort.
    Compute the total number of comparisons used to sort the given input file by QuickSort.
"""
numberOfComparison = 0
def QuickSort(array, n, functionOfPivot):
    global numberOfComparison
    if n == 1:
        return array

    p, index = functionOfPivot(array, n)
    array, pIndex = Partition(array, p, index)
    left = array[:pIndex]
    right = array[pIndex + 1:]
    if left != []:
        numberOfComparison += len(left)-1
        array[:pIndex] = QuickSort(left, len(left), functionOfPivot)
    if right != []:
        numberOfComparison += len(right)-1
        array[pIndex + 1:] = QuickSort(right, len(right), functionOfPivot)

    return array

def Partition(array, p, index):
    # array[1:index+1] = array[:index]
    temp = array[0]
    array[0] = array[index]
    array[index] = temp

    array[0] = p
    i = 1
    for j in range(1, len(array)):
        if array[j] < p:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i += 1
    temp = array[0]
    array[0] = array[i-1]
    array[i-1] = temp

    return (array, i-1)

def ChoosePivot_First(array, n):
    return (array[0], 0)

def ChoosePivot_Last(array, n):
    return (array[-1], len(array)-1)

def ChoosePivot_MedianOfThree(array, n):
    firstValue = array[0]
    lastValue = array[-1]
    medianValue = array[int(len(array)/2) - 1]

    if firstValue < lastValue:
        if medianValue < firstValue:
            return (firstValue, 0)
        elif medianValue > lastValue:
            return (lastValue, len(array)-1)
        else:
            return (medianValue, int(len(array)/2) -1)
    else:
        if medianValue < lastValue:
            return (lastValue, len(array) -1)
        elif medianValue > firstValue:
            return (firstValue, 0)
        else:
            return (medianValue, int(len(array)/2) -1)

# array = [3,8,2,5,1,4,7,6]
array = []
with open("E:\Practice-of-Algorithm\Practice-of-Algorithm\Divide and Conquer Algorithm\QuickSort.txt",'r') as f:
    for line in f.readlines():
        array.append(int(line.strip()))
numberOfComparison += len(array)-1
# print(QuickSort(array, len(array), ChoosePivot_First))
# print(QuickSort(array, len(array), ChoosePivot_Last))
print(QuickSort(array, len(array), ChoosePivot_MedianOfThree))
print(numberOfComparison)