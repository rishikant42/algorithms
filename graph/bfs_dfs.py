from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = {k: False for k in self.graph.keys()}

        queue = [s]

        visited[s] = True

        while(queue):

            s = queue.pop(0)
            print(s, end=' ')

            for i in self.graph[s]:
                if visited[i] is False:
                    queue.append(i)
                    visited[i] = True

    def DFS(self, s):
        visited = {k: False for k in self.graph.keys()}
        stack = [s]

        visited[s] = True

        while(stack):
            s = stack.pop()

            print(s, end=' ')

            for i in self.graph[s]:
                if visited[i] is False:
                    stack.append(i)
                    visited[i] = True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.BFS(2)
# g.DFS(2)
