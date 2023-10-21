from collections import deque

def bfs(start, graph):
    visited = [False] * (len(graph) + 1)
    max_distance = 0
    max_node = 0

    queue = deque()
    queue.append((start, 0))
    visited[start] = True

    while queue:
        node, distance = queue.popleft()

        if distance > max_distance:
            max_distance = distance
            max_node = node

        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, distance + weight))

    return max_node, max_distance

def tree_diameter(graph):
    node1, _ = bfs(1, graph)
    
    node2, diameter = bfs(node1, graph)
    
    return diameter

n = int(input())
tree_graph = [[] for _ in range(n + 1)]

for i in range(n):
    data = list(map(int, input().split()))
    node = data[0]
    data = data[1:-1]  
    for j in range(0, len(data), 2):
        tree_graph[node].append((data[j], data[j + 1]))

diameter = tree_diameter(tree_graph)
print(diameter)
