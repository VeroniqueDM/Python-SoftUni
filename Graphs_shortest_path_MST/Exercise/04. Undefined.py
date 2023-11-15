from builtins import function
from collections import deque


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


nodes = int(input())
edges = int(input())
graph = []

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    graph.append(Edge(source, destination, weight))

start = int(input())
target = int(input())

distance = [float('inf')] * (nodes + 1)
parent = [None] * (nodes + 1)
distance[start] = 0

for _ in range(nodes - 1):
    updated = False
    # for first, second, weight in graph:
    #     if distance[first] == float('inf'):
    #     if new_distance< distance[second]:

    for edge in graph:
        if distance[edge.source] == float('inf'):
            continue
        new_distance = distance[edge.source] + edge.weight
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = edge.source
            updated = True
    if not updated:
        break

# Alternative solution with function:
# (still needs to check for negative cycle)
# def find_path(parent, node):
#     result = deque()
#     while node is not None:
#         result.appendleft(node)
#         node = parent[node]
#     return result
#
# path = find_path(parent, target)
# print(*path, sep=' ')

for edge in graph:
    new_distance = distance[edge.source] + edge.weight
    if new_distance < distance[edge.destination]:
        print('Undefined')
        break
# This another of the same loop from the main loop. This is done to check if this would still return a better path.
# If it does, this means we entered a negative cycle.


else:
    path=deque()
    node=target
    while node is not None:
        path.appendleft(node)
        node=parent[node]

    print(*path, sep=' ')
    print(distance[target])
