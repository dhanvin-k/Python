import collections


def path(str):
    k = int(str[0])
    goal = str[k]
    node_list = str[1:k+1]
    connections = str[k+1:]
    graph = {i: [] for i in node_list}
    for item in connections:
        graph[item[0]].append(item[2])

    return bfs(graph, goal, "A")


def bfs(graph, goal, top):
    queue = [top]
    path = []
    while queue:
        node = queue.pop(0)
        path.append(node)
        if node == goal:
            return path
        children = graph[node]
        for child in children:
            if child in queue:
                children.remove(child)
        if len(children) == 0:
            path.pop()
            pass
        for child in children:
            queue.append(child)
    return path


print(path(["6", "A", "B", "C", "D", "E", "F",
            "A-B", "A-C", "B-C", "C-D", "D-F", "C-E"]))
