# 创建整个图的散列表
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['end'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['end'] = 5
graph['end'] = {}

infinity = float('inf')

# 创建开销表
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['end'] = infinity

# 创建存储父节点的散列表
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['end'] = None

# 用于记录已经处理过的节点的列表
processed = []
def findLowestCostNode(costs):
    lowestCost = float('inf')
    lowestCostNode = None
    for node in costs: # 遍历所有的节点
        cost = costs[node]
        if cost < lowestCost and node not in processed: # 如果当前节点的开销更低且未处理过
            lowestCost = cost
            lowestCostNode = node
    return lowestCostNode

def dijkstra():
    # 再未处理的节点中找出开销最小的节点
    node = findLowestCostNode(costs)
    # 这个while循环在所有节点都被处理过后结束
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        # 遍历当前节点的所有邻居
        for n in neighbors.keys():
            newCost = cost + neighbors[n]
            if costs[n] > newCost: # 如果经当前节点前往该邻居更近
                costs[n] = newCost # 就更新该邻居的开销
                parents[n] = node # 同时将该邻居的父节点设置为当前节点
        processed.append(node) # 将当前节点标记为处理过
        node = findLowestCostNode(costs) # 找出接下来要处理的节点，并循环
    print('\n',u'到终点的最短路径代价为：',costs['end'])
    # 遍历输出路径
    print('\n',u'到终点的最短路径为：')
    print('end')
    parent = parents['end']
    while(parent != 'start'):
        print('<--'+parent)
        parent = parents[parent]
    print('<--start')

dijkstra()
