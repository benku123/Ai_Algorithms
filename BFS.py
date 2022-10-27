graph = {
  '1' : ['2', '3','4'],
  '2' : ['5'],
  '3' : ['6'],
  '4' : ['6'],
  '5' : ['7'],
  '6' : ['7'],
  '7' : []
}

visited = []

def bfs(graph, start):
    queue = [start]

    while len(queue) > 0:
        m = queue.pop(0)
        print(m)
        for node in graph[m]:
            if node not in visited:
                visited.append(node)
                queue.append(node)

bfs(graph, "1")




bfs(graph, "1")
print(visited)
