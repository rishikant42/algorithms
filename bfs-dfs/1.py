def dfs(graph,start):
    visited = set()
    stack = [start]
    while stack:
        #print stack
        vertex = stack.pop()
        #print vertex
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex]-visited)
    return visited

def bfs(graph,start):
    visited = set()
    queue = [start]
    while queue:
        #print queue
        vertex = queue.pop(0)
        #print vertex
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex]-visited)
    return visited

def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        return path
    for next in graph[start] - set(path):
        return dfs_paths(graph, next, goal, path + [next])

graph = {'A': set(['B', 'C']),
         'B': set(['A','D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print dfs(graph,'A')

print bfs(graph,'A')

print dfs_paths(graph,'A','F')
