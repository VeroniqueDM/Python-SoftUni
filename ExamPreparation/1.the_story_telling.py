from audioop import reverse


def dfs(node, graph, visited, result):
    if node in visited:
        return
    visited.add(node)
    for child in graph[node]:
        dfs(child, graph, visited, result)
    result.append(node)


graph = {}

while True:
    line = input()
    if line == 'End':
        break
    node, children_str = [x.strip() for x in line.split('->')]
    children = children_str.split()
    graph[node] = children

visited = set()
result = []

for node in graph:
    dfs(node, graph, visited,result)

print(*list(reversed(result)), sep=" ")
