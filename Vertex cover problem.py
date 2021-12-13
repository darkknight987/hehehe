from collections import defaultdict
from random import randrange

class Graph:
    def __init__(self):
        self.graph_dict = defaultdict(list)
        
    def add_edge(self, node1, node2):
        self.graph_dict[node1].append(node2)

    def get_vertex_cover(self):
        edges = [(vert1, vert2) for vert1 in self.graph_dict for vert2 in self.graph_dict[vert1]]
        vertex_cover = []
        while edges:
            curr_edge = edges.pop(randrange(len(edges)))
            vertex_cover.extend(curr_edge)
            edges[:] = [edge for edge in edges if curr_edge[0] not in edge and curr_edge[1] not in edge]
        return vertex_cover


graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'E')
graph.add_edge('E', 'F')
graph.add_edge('E', 'D')
graph.add_edge('C', 'D')
graph.add_edge('D', 'F')
graph.add_edge('D', 'G')

print("\nVertex cover:\n", graph.get_vertex_cover())
