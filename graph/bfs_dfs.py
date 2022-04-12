from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):

        queue = [s]

        visited = [s]

        while(queue):

            s = queue.pop(0)
            print(s, end=' ')

            for neighbour in self.graph[s]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.append(neighbour)

    def DFSUtil(self, s, visited):
        visited.append(s)
        print(s, end=' ')

        for neigbour in self.graph[s]:
            if neigbour not in visited:
                self.DFSUtil(neigbour, visited)

    def DFS(self, s):
        visited = []
        self.DFSUtil(s, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.BFS(2)
print("\n")
g.DFS(2)
print("\n")
