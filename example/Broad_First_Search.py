"""
Created Time: Aug.5 2018

@author: Zhangrong.Huang
"""

from collections import deque

class Graph():
    """
    define the class of Graph
    """
    

    def __init__(self, graph_map):
        """
        param:
            graph_map(type:dict): the map used to store graph
        """
        self.graph_map =graph_map
        self.discoveried = {}
        
    
    def adjacency(self, vertex):
        """
        param:
            vertex(type:str): the vertex in graph

        return:
            self.graph_map[vertex](type:list): the adjacency vertice of given vertex
        """
        return self.graph_map[vertex]
        
search_q = deque()

def broad_first_search(graph, vertex):
    """
    use broad first search algorithm
    param:
        graph(type: Class Graph)
        vertex(type: str): the start vertex in graph searching
    """
    global search_q
    
    graph.discoveried[vertex]=True # Label this vertex
    print(vertex)
    
    search_q += graph.adjacency(vertex) # get the adjacency vertice
    
    while search_q:
        new_vertex = search_q.popleft()

        if new_vertex not in graph.discoveried:
            search_q += graph.adjacency(new_vertex)
            graph.discoveried[new_vertex] =True
            print(new_vertex)




if __name__=="__main__":         
    g = {'A':['B','C','E'],
            'B':['A','D','F'],
            'C':['A','G'],
            'D':['B'],
            'E':['A','F'],
            'F':['B','E'],
            'G':['C']}
    G = Graph(g)

    broad_first_search(G, 'A')