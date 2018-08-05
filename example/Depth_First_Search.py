"""
Created Time: Jul.29 2018

@author: Zhangrong.Huang
"""

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
        

def depth_first_search(graph, vertex):
    """
    use depth first search algorithm
    param:
        graph(type: Class Graph)
        vertex(type: str): the start vertex in graph searching
    """
    
    graph.discoveried[vertex]=True # Label this vertex
    print(vertex)
    
    adjacency_vertice = graph.adjacency(vertex) # get the adjacency vertice
    
    for vert in adjacency_vertice:
        if vert not in graph.discoveried:
            depth_first_search(graph, vert)


if __name__=="__main__":         
    g = {'A':['B','C','E'],
            'B':['A','D','F'],
            'C':['A','G'],
            'D':['B'],
            'E':['A','F'],
            'F':['B','E'],
            'G':['C']}
    G = Graph(g)

    depth_first_search(G, 'A')