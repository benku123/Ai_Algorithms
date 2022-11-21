from queue import PriorityQueue


def ucs(root, goal):
    queue = PriorityQueue()
    queue.put((0, [root]))

    while not queue.empty():
        pair = queue.get()
        current = pair[1][-1]
        if current.label == goal:
            return pair[1]
        for edge in current.children:
            new_path = list(pair[1])
            new_path.append(edge.destination)
            queue.put((pair[0] + edge.cost, new_path))
