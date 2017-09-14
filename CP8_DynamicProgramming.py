# 动态规划背包问题

# 旅游行程最优化数据
# items = ['W','G','N','B','S']
# itemsValue = {'W':7, 'G':6, 'N':9, 'B':9, 'S':8}
# itemsWeight = {'W':1, 'G':1, 'N':2, 'B':4, 'S':1}
# packageWeight = 4

# 野营背包最优化数据
# %%
items = ['water', 'book', 'food', 'jacket', 'camera']
itemsValue = {'water': 10, 'book': 3, 'food': 9, 'jacket': 5, 'camera': 6}
itemsWeight = {'water': 3, 'book': 1, 'food': 2, 'jacket': 2, 'camera': 1}
packageWeight = 6

# %%


def display(arr):
    for i in range(len(arr)):
        print('\n', arr[i])


def getMaxValue(a, b):
    if a < b:
        return (b, 1)
    else:
        return (a, 0)


def solve():
    # 小包裹的最细粒度取决于各物品最小重量
    granularity = min(itemsWeight.values())
    # 列数 = 包裹最大容量 / 最细粒度 + 1
    columnNum = packageWeight / granularity + 1
    # 行数 = 物品数目 + 1
    rowNum = len(items) + 1
    dp = [[0 for i in range(int(columnNum))] for i in range(int(rowNum))]
    # 创建一个对应的表格，来记录计算中的物品选择
    dpItems = [[[] for i in range(int(columnNum))] for i in range(int(rowNum))]

    for item, row in zip(items, range(1, len(items)+1)):
        for j in range(1, packageWeight+1):
            print('\n', 'item:', item, 'row:', row, 'j:', j)
            if j < itemsWeight[item]:
                dp[row][j] = dp[row-1][j]
                dpItems[row][j] = dpItems[row-1][j]
            else:
                maxValue, flag = getMaxValue(dp[row-1][j], dp[row-1][j-itemsWeight[item]]+itemsValue[item])
                dp[row][j] = maxValue
                if flag == 1:
                    dpItems[row][j] = dpItems[row-1][j-itemsWeight[item]] + [item]
                else:
                    dpItems[row][j] = dpItems[row-1][j]

            display(dp)
            display(dpItems)
    print('\n', 'maxValue:', dp[-1][-1], 'result:', dpItems[-1][-1])


solve()
# %%
