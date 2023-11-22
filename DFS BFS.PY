def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def bfs(graph, start_node):
    visited = []
    queue = [start_node]
    visited.append(start_node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph.get(m, []):
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Get user inputs for creating the graph
graph = {}
num_nodes = int(input("Enter the number of nodes in the graph: "))

for _ in range(num_nodes):
    node = input("Enter the node: ")
    neighbors_input = input("Enter neighbors (comma-separated): ")
    neighbors = neighbors_input.split(',') if neighbors_input else []
    graph[node] = neighbors

start_node = input("Enter the starting node for traversals: ")

print("\nDepth-First Search:")
visited_dfs = set()
dfs(visited_dfs, graph, start_node)

print("\nBreadth-First Search:")
bfs(graph, start_node)
