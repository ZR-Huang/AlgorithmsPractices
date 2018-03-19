"""
this script is for counting the inversion of a given list
2018-03-19 15:55
@author:ZR-Huang
@email:hzr951110@gmail.com
"""

def SortAndCount(array,length):
    if length == 1:
        return (array, 0)
    else:
        left = array[:int(length/2)]
        right = array[int(length/2):]

        (B, X) = SortAndCount(left,int(length/2))
        (C, Y) = SortAndCount(right,int(length/2))
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
        

array = [5,4,1,8,7,2,6,3]
sortedArray, invNum = SortAndCount(array,len(array))
print("test1:",sortedArray,"the number of inversion:",invNum)
array = [5,4,1,9,8,7,2,6,3]
sortedArray, invNum = SortAndCount(array,len(array))
print("test1:",sortedArray,"the number of inversion:",invNum)