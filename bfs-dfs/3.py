def bfs_path(graph,start,end):
    queue = []
    queue.append(start)
    while queue:
        #print queue
        path = queue.pop(0)
        #print path
        node = path[-1]
        #print node
        if node == end:
            return path
        else:
            for adjacent in graph.get(node,[]):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        }

print bfs_path(graph,'1','11')

##bfs path for directed acyclic graph(DAG)
    
