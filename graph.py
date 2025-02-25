from collections import defaultdict

graph = defaultdict(list)

graph['A'].extend(['B', 'C'])
graph['B'].extend(['A', 'D', 'E'])
graph['C'].extend(['A', 'F'])
graph['D'].append('B')
graph['E'].extend(['B', 'F'])
graph['F'].extend(['C', 'E'])

for node, neighbours in graph.items():
    print(f"{node} is connected to: {neighbours}")

no_of_nodes = 0
no_of_edges = 0

for node, neighbours in graph.items():
    no_of_nodes += 1
    for neighbour in neighbours:
        no_of_edges += 1

no_of_edges //= 2

print("No of nodes :", no_of_nodes)
print("No of edges :", no_of_edges)

from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = []
    result = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            result.append(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
    return result

print(bfs(graph, 'A'))

def dfs(graph, start):
    stack = [start]
    visited = []
    result = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            result.append(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    stack.append(neighbour)
    return result

print(dfs(graph, 'A'))