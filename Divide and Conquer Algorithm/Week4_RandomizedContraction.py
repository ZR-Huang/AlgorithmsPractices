import time
import random

# adjacencyList = [
#     ('1',['2','3']),
#     ('2',['1','3','4']),
#     ('3',['1','2','4']),
#     ('4',['2','3'])
# ]
adjacencyList = []
with open(r"E:\\Practice-of-Algorithm\\Practice-of-Algorithm\Divide and Conquer Algorithm\\kargerMinCut.txt") as f:
    for line in f.readlines():
        temp = list(line.strip().split('\t'))
        adjacencyList.append([temp[0],temp[1:]])


def GetRandomEdge():
    global adjacencyList
    startPointIndex = random.randint(0, len(adjacencyList) - 1)
    startPoint = adjacencyList[startPointIndex][0]
    adjList = adjacencyList[startPointIndex][1]
    endPointIndex = random.randint(0, len(adjList) - 1)
    endPoint = adjList[endPointIndex]
    return (startPointIndex, startPoint, endPointIndex, endPoint, adjList)

def GetIndex(L, target, mode):
    if mode == 'ALLTable':
        for index, i in enumerate(L):
            if i[0] == target:
                return index
    elif mode == 'VectexAdj':
        for index, i in enumerate(L):
            if i == target:
                return index

def Contract(startPointIndex, startPoint, endPointIndex, endPoint, adjList):
    global adjacencyList
    # 遍历所有与startPoint邻接的点
    # 将邻接点的邻接列表中的所有startPoint改成endPoint
    for item in adjList: 
        itemIndex = GetIndex(adjacencyList, item, 'ALLTable')
        for index, i in enumerate(adjacencyList[itemIndex][1]):
            if i == startPoint:
                adjacencyList[itemIndex][1][index] = endPoint
    
    # 将startPoint邻接点（除endPoint外）都添加到endPoint邻接点列表中
    endPointRowIndex = GetIndex(adjacencyList, adjList[endPointIndex], 'ALLTable')
    for item in adjList:
        if item != endPoint:
            adjacencyList[endPointRowIndex][1].append(item)
            

def DeleteSelfLoop():
    global adjacencyList
    temp = adjacencyList
    for rowIndex, row in enumerate(temp):
        key = row[0]
        l = row[1]
        # for index, item in enumerate(l):
        #     if key == item:
        #         adjacencyList[rowIndex][1].pop(index)
        newL = list(filter(lambda x: x!= key, l))
        adjacencyList[rowIndex][1] = newL


def KargerMinCut():
    global adjacencyList
    while len(adjacencyList) > 2:
        # print(adjacencyList)
        startPointIndex, startPoint, endPointIndex, endPoint, adjList = GetRandomEdge()
        # print(startPoint,endPoint)
        Contract(startPointIndex, startPoint, endPointIndex, endPoint, adjList)
        adjacencyList.pop(startPointIndex)
        DeleteSelfLoop()
        
    DeleteSelfLoop()
    # print(adjacencyList)
    return len(adjacencyList[0][1])


minimum = 999999999
print(KargerMinCut())

