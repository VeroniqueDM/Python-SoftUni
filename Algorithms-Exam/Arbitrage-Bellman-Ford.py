from collections import deque


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


edges = int(input())

graph = {}

vertices = []
for _ in range(edges):
    first, second, weight_str = input().split()
    if first not in vertices:
        vertices.append(first)
    if second not in vertices:
        vertices.append(second)
    weight = float(weight_str)
    if first not in graph:
        graph[first] =[]
    edge = Edge(first, second, weight)
    graph[first].append(edge)


target_node = input()

distance = {}
for node in vertices:
    distance[node] = float('-inf')

distance[target_node] = 1

parent = {}
for node in vertices:
    parent[node] = None


for _ in range(len(vertices) - 1):
    updated = False
    for node in graph:
        for edge in graph[node]:
            if distance[edge.first] == float('inf'):
                continue
            new_distance = distance[edge.first] + edge.weight
            if new_distance < distance[edge.second]:
                distance[edge.second] = new_distance
                parent[edge.second] = edge.first
                updated = True
        # UPDATED IS ONLY USED TO OPTIMIZE THE ALGORITHM
        if not updated:
            break


for node in graph:
    for edge in graph[node]:
        new_distance = distance[edge.first] + edge.weight
        if new_distance < distance[edge.second]:
            print('Negative Cycle Detected')
            break

else:
    path=deque()
    node=target_node

    while node is not None:
        path.appendleft(node)
        node=parent[node]

    print(*path, sep=' ')
    print(distance[target_node])