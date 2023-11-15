from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


def find_root(parent, node):
    while node != parent[node]:
        node=parent[node]
    return node


neighbourhoods = int(input())
edges = int(input())
lightnings = int(input())

graph = []
[graph.append([]) for _ in range(neighbourhoods)]
max_node = float('-inf')
edges_list = []
for _ in range(edges):
    first, second, weight = [int(x) for x in input().split()]
    edge = Edge(first, second, weight)
    graph[first].append(edge)
    graph[second].append(edge)
    edges_list.append(edge)
    max_node = max(first, second, weight)
damage = [0] * neighbourhoods
for lightning in range(1,lightnings):
    line = input().split()
    neighbourhood = int(line[0])
    power = int(line[1])
    tree = set()
    tree.add(neighbourhood)
    pq = PriorityQueue()
    damage[neighbourhood] += power
    for edge in graph[neighbourhood]:
        pq.put(edge)
    while not pq.empty():
        min_edge = pq.get()
        non_tree_node = None
        if min_edge.first not in tree and min_edge.second in tree:
            non_tree_node = min_edge.first
        elif min_edge.first in tree and min_edge.second not in tree:
            non_tree_node = min_edge.second
        if non_tree_node is None:
            continue

        tree.add(non_tree_node)
        for edge in graph[non_tree_node]:
            pq.put(edge)


# parent = [num for num in range(max_node+1)]
#
# def find_root(parent, node):
#     while node != parent[node]:
#         node=parent[node]
#     return node
#
# forest =[]
# for edge in sorted(edges_list, key=lambda e: e.weight):
#     first_node_root =find_root(parent, edge.first)
#     second_node_root =find_root(parent, edge.second)
#     if first_node_root != second_node_root:
#         parent[first_node_root]=second_node_root
#         forest.append(edge)
#
# print(graph)
# print([e.weight for e in forest])
