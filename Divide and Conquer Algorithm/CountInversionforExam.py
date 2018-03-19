"""
this script is for counting the inversion of a given list
2018-03-19 15:55
@author:ZR-Huang
@email:hzr951110@gmail.com
"""

def SortAndCount(array):
    if len(array) == 1:
        return (array, 0)
    else:
        left = array[:int(len(array)/2)]
        right = array[int(len(array)/2):]

        (B, X) = SortAndCount(left)
        (C, Y) = SortAndCount(right)
        (D, Z) = CountSplitInv(B,C)
    #print(B, C, D)
   # print(X,Y,Z)
    return  (D, X+Y+Z)

def CountSplitInv(B,C):
    i = 0
    j = 0
    sortedArray = []
    invNum = 0

    for k in range(len(B) + len(C)):
        if i < len(B) and  j < len(C):
            if B[i] < C[j]:
                sortedArray.append(B[i])
                i += 1
            elif B[i] >C[j]:
                sortedArray.append(C[j])
                j += 1
                invNum += (len(B) - i)
            else:
                sortedArray.append(B[i])
                sortedArray.append(C[j])
                i += 1
                j += 1
        elif i == len(B):
            sortedArray.append(C[j])
            j+=1
        elif j == len(C):
            sortedArray.append(B[i])
            i+=1
    
    return (sortedArray, invNum)

'''
array = [5,4,1,8,7,2,6,3,13,9,10,15,12,11,14,20,19,16,18,17]
sortedArray, invNum = SortAndCount(array)
print("test1:",sortedArray,"the number of inversion:",invNum)    
'''
array = []
with open("IntegerArray.txt",'r') as f:
    for line in f.readlines():
        array.append(int(line.strip()))

sortedArray, invNum = SortAndCount(array)
print(sortedArray,invNum)
