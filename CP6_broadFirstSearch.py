from collections import deque

graph = {}
graph['you'] = ['alice','bob','claire']
graph['bob'] = ['anuj','peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom','jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

def personIsSeller(name):
    return name[-1] == 'm'

def broadFirstSearch(name):
    searchQueue = deque()
    searchQueue += graph[name]
    searched = {}
    # searched = []
    while searchQueue:
        person = searchQueue.popleft()
        if not searched.get(person):
        # if not person in searched:
            print('\n','check--', person)
            if personIsSeller(person):
                print('\n',person, '--is a mango seller!')
                return True
            else:
                searchQueue += graph[person]
                searched[person] = True
                # searched.append(person)
    return False

broadFirstSearch(name='you')
