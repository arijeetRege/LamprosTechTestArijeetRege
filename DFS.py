# Arijeet Rege, Faculty of Technology and Engineering, The Maharaja Sayajirao University of Baroda
# Q2 : Graph traversal, done by Depth First Search OR DFS
def dftraversal(mygraph, node, visited):
    if node not in visited:  # If the node has not been visited
        print(node, end=" ~>> ")  # Print the node
        visited.add(node)  # Mark it as visited
        # Recursively visit all unvisited neighbors
        for neighbor in mygraph[node]:
            dftraversal(mygraph, neighbor, visited)
# Graph representation using adjacency list. Use of dictionary
mygraph = {
    'A': ['B', 'C'],
    'B': ['A','C', 'D', 'E'],
    'C': ['B'],
    'D': ['B'],
    'E': ['B']
}
# Set to track visited nodes
visited = set()
# Perform DFS starting from node 'A'
print("DFS Traversal: ")
dftraversal(mygraph, 'A', visited)