# Pseudocode (recursive implementation)
#Start by putting any one of the graph's vertices on top of a stack.
#Take the top item of the stack and add it to the visited list.
#Create a list of that vertex's adjacent nodes. Add the ones which aren't in the visited list to the top of the stack.
#Keep repeating steps 2 and 3 until the stack is empty.


# DFS(G, u)
#    u.visited = true
#    for each v ∈ G.Adj[u]
#        if v.visited == false
#            DFS(G, v)

# init() {
#    For each u ∈ G
#        u.visited = false
#    For each u ∈ G
#        DFS(G, u)
# }


#when the function is called, if there is not any statement whether it is visited or not, the default value will be None.
def dfs(graph, start, visited=None):
    if visited is None:
        # it will be used to save the nodes we've visited
        visited = set()
    # Add the current node to the visited set.
    visited.add(start)

    # Print the current node, indicating it has been visited.
    print(start)

    # Iterate over each adjacent node of the current node that hasn't been visited yet.
    for next in graph[start] - visited:
        # Recursively call DFS for the adjacent node.
        dfs(graph, next, visited)
    # Return the set of visited nodes.
    return visited

# The graph is represented as a dictionary where keys are nodes and values are sets of adjacent nodes.
graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}
# Start DFS traversal from node '0'.
dfs(graph, '0')