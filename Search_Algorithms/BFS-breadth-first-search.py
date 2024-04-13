# to be able to use "deque", I import 'collections'
import collections

# "graph" is a dictionary. We'll be applying this code into the graph.
# "root" is our starting node!
def bfs(graph, root):
	#"visited" is created to store where we've visited :)
    #"queue" is created to store which nodes we'll visit.
    #the 'root' is the first node we've visited, so...
    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:
        # I remove the node from the queue and send it to the "vertex"
        vertex = queue.popleft()
        # I wanted to print which node I've removed.
        print(str(vertex) + " ", end="")

		# To travel all the nodes which are neighbour of "vertex" node
        for neighbour in graph[vertex]:
            # If not visited,
            if neighbour not in visited:
                #mark it as "visited"
                visited.add(neighbour)
                #and add the neighbour to the "queue".
                queue.append(neighbour)


if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)
