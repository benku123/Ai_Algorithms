def dfs(graph, start, visited):
    visited.add(start)
    graph[start] = set(graph[start]) # to use operand -
    print(start)
    for inner_node in graph[start] - visited:
        dfs(graph, inner_node, visited)
    return 
dfs(graph, '1', set())