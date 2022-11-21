def bfs(graph, init):
    visited = []
    queue = []
    visited.append(init)
    queue.append(init)
    while queue:
        s = queue.pop(0)
        print (s, end = " -> ")
        for node in graph[s]:
            if node not in visited:
                visited.append(node)
                queue.append(node)
    print("None")

bfs(graph, '1')