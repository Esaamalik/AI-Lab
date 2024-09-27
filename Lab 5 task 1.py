class Node:
    def __init__(self, value):
        self.value = value
        self.adjacent = []

    def add_edge(self, neighbor):
        self.adjacent.append(neighbor)


def dfs_with_stack(start_node):
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node.value, end=" ")
            visited.add(node)
            for neighbor in reversed(node.adjacent):
                if neighbor not in visited:
                    stack.append(neighbor)


node_A = Node('A')
node_B = Node('B')
node_C = Node('C')
node_D = Node('D')
node_E = Node('E')

node_A.add_edge(node_B)
node_A.add_edge(node_C)
node_B.add_edge(node_D)
node_B.add_edge(node_E)
node_C.add_edge(node_E)

dfs_with_stack(node_A)
