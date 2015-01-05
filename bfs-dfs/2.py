def dfs(graph, start, visited):
    if visited is None:
        visited = set()
    visited.add(start)
    #print visited
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited



graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print dfs(graph,'A',None)


##Another method to construct dfs
