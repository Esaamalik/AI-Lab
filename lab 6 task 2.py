class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


def bfs(start_node):
    visited = set()
    queue = [start_node]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node.value, end=" ")
            visited.add(node)
            queue.extend(node.children)


# Example usage
root = Node('A')
child_b = Node('B')
child_c = Node('C')
child_d = Node('D')
child_e = Node('E')

root.add_child(child_b)
root.add_child(child_c)
child_b.add_child(child_d)
child_b.add_child(child_e)

bfs(root)
