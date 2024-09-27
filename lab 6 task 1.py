def bfs(graph, start):
    visited = set()
    visited.add(start)
    result = []
    current_level = [start]

    while current_level:
        next_level = []
        for node in current_level:
            result.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    next_level.append(neighbor)
        current_level = next_level

    return result

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs_result = bfs(graph, 'A')
print("BFS Traversal:", bfs_result)
