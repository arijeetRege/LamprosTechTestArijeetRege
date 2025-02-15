# Arijeet Rege, Faculty of Technology and Engineering, The Maharaja Sayajirao University of Baroda
# Q2 : Graph traversal, done by Depth First Search OR DFS
def dftraversal(mygraph, node, visited):
    if node not in visited:  # checking if we have visited the node
        print(node, end=" ~>> ")  # Printing the node
        visited.add(node)  # Marking it as visited
        # Recursively visiting all unvisited neighbors
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
# Set to track visited nodes, to avoid cycling
visited = set()
# Perform DFS starting from node 'A'
print("DFS Traversal: ")
dftraversal(mygraph, 'A', visited)
