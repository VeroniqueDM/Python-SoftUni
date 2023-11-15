nodes = int(input())
edges = int(input())

graph = []


def find_root(parent, node):
    while node != parent[node]:
        node=parent[node]
    return node


for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(' - ')]
    graph.append(( first, second, weight))

parent = [num for num in range(nodes)]
# every node is a tree initially
total_cost = 0
for first, second, weight in sorted(graph, key=lambda x: x[2] ):
    first_node_root =find_root(parent, first)
    second_node_root =find_root(parent, second)
    if first_node_root != second_node_root:
        parent[first_node_root]=second_node_root
        # this way the two trees get binded, become one

        total_cost += weight

        # print(first, second, weight)

print(f'Total cost: {total_cost}')
