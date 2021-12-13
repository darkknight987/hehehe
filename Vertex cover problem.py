from collections import defaultdict
class Graph:
    def __init__(self):
        self.vertex_names = set()
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.vertex_names.update({u, v})

    def printVertexCover(self):
        visited = {vert: False for vert in self.vertex_names }
        for vert in self.vertex_names:
            if not visited[vert]:
                for adj in self.graph[vert]:
                    if not visited[adj]:
                        visited[adj] = True
                        visited[vert] = True
                        break
        for vert in visited:
            if visited[vert]:
                print(vert, end = ' ')
g = Graph()
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 3)
# g.addEdge(3, 4)
# g.addEdge(4, 5)
# g.addEdge(5, 6)
# g.addEdge(2, 3)
# g.addEdge(2, 4)
g.addEdge('a', 'b')
g.addEdge('b', 'c')
g.addEdge('c','d')
g.addEdge('c','e')
g.addEdge('e','f')
g.addEdge('d','f')
g.addEdge('d', 'g')
g.printVertexCover()