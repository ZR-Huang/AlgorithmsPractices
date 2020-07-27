'''
找出包含文件数最多的路径

题目描述：
你是一位系统管理员，手里有一份包含合法文件夹绝对路径及文件绝对路径的列表，
你的任务是找出该列表中包含文件数目最多的文件夹路径（如果有多个结果，需要
全部输出，并按照字母顺序进行排序）。文件夹和文件路径都是Linux风格，
即用/分割，在路径上只会包括字母，/，.和..，其中.表示此层目录，..表示上层
目录，文件后缀只包含.txt格式。例如，/a和/a/b是合法的文件夹路径，/a/b.txt是
合法的文件路径，空字符串和/不是合法的路径。

输入描述：
第一行表示路径的个数N，后面N行每一行代表一个路径，输入的路径中至少会包含一个
文件路径。

输出描述：
输出符合条件的文件夹路径，每行一个，如果没有符合条件的文件夹输出字符串null。

示例1:
输入：
5
/a
/a/./b/test.txt
/c/d
/c/e
/e/c/f
输出：
/a

示例2:
输入：
4
/a
/a/b/test.txt
/a/b/test2.txt
/a/b/../test3.txt
输出：
/a

示例3:
输入：
2
/a/file1.txt
/a//file2.txt
输出：
null


Score: 70%
'''

N = int(input())
# N = 5
pathes = []
# pathes = ['/a', '/a/./b/test.txt', '/c/d', '/c/d', '/e/c/f']

for _ in range(N):
    pathes.append(input())

fileCounter = {}
maximum = 0
for path in pathes:
    if path == '' or path == '/':
        continue
    dirs = path.strip().split('/')
    dirs.pop(0)
    dot_dot_index = -1
    for i in range(len(dirs)):
        if dirs[i]=='..':
            dot_dot_index = i
            break
    
    if dirs[-1].endswith(".txt"):
        for i in range(1, len(dirs)):
            pathContainFile = dirs[:i]
            if dot_dot_index>=0 and i > dot_dot_index:
                pathContainFile.pop(dot_dot_index)
                pathContainFile.pop(dot_dot_index-1)
            if '.' in pathContainFile:
                pathContainFile.remove('.')
            key = '/'.join(pathContainFile)
            if key not in fileCounter:
                fileCounter[key] = 1
            else:
                fileCounter[key] += 1
            maximum = max(fileCounter[key], maximum)

# fileCounter = sorted(fileCounter, key=lambda key: fileCounter[key], reverse=True)
res = []
for key, value in fileCounter.items():
    if value == maximum:
        res.append('/'+key)
for elem in res:
    print(elem)
            