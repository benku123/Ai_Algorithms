
def IDS(initial :str, mx_depth :int, goal :str):
    for elem in graph[initial]:
        counter = mx_depth
        while counter > 0:
            if goal == elem:
                return True
            elif elem not in graph or graph[elem] == []:
                break

            elem = graph[elem][0]
            counter -= 1
    return False


goal = "7"
mx_depth = 4

print(IDS("1", mx_depth, goal))
