from queue import PriorityQueue
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


pq = PriorityQueue()
pq.put((-1, target_node))

# distance = [float('-inf')] * len(graph)
distance = {}
for node in vertices:
    distance[node] = float('-inf')

distance[target_node] = 1

parent = {}
for node in vertices:
    parent[node] = None
parent[target_node + '2']= None
visited_target = 0
while not pq.empty():
    max_distance, node = pq.get()

    for edge in graph[node]:

        child = edge.second
        new_distance = -max_distance * edge.weight
        if new_distance> distance[child]:
            distance[child] = new_distance
            if child == target_node:
                parent[target_node + '2'] = node
            else:
                parent[child] = node
                pq.put((-new_distance, child))
        if child == target_node:
            visited_target += 1
            if visited_target == 2:
                parent[target_node + '2'] = node
                distance[target_node + '2'] = new_distance

                break

is_possible = False
if distance[target_node] >1:
    is_possible = True

print(is_possible)


path = deque()
node = target_node + '2'
while node is not None:
    path.appendleft(node)
    node = parent[node]
if is_possible:
    path[-1] = target_node

    print(*path, sep=" ")
else:
    for idx in range(len(path)-1):
        res = f'{distance[path[idx]]:.3f}'
        print(f'{path[idx]}: {res}')
