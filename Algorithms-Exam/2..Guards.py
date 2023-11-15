from collections import deque

nodes = int(input())
edges = int(input())

graph = {}

for idx in range(nodes+1):
    graph[idx] = []
def find_shortest_path(graph, source, destination):
    queue = deque([source])
    visited = {source}

    parent = {source: None}
    while queue:
        node = queue.popleft()
        if node == destination:
            break
        for child in graph[node]:
            if child in visited:
                continue
            queue.append(child)
            visited.add(child)
            parent[child] = node
    return parent


def find_path_size(parent, destination):
    size = 0
    node = destination
    while node is not None:
        node = parent[node]
        size += 1
    return size - 1


for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    # source_node = int(source)
    # destination_node = int(destination)
    # if source not in graph:
    #     graph[source] = []
    graph[source].append(destination)

beginning_node = int(input())
pairs = []

for node in graph:
    if node == beginning_node or node == 0:
        continue
    pairs.append((beginning_node, node))
unreachables = []
for beginning_node, node in pairs:
    parent = find_shortest_path(graph, beginning_node, node)
    if node not in parent:
        unreachables.append(node)
        continue

print(*unreachables, sep=' ')