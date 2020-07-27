from queue import Queue

adjacency_list = {
"A":["B","D"],
"B":["A","C"],
"C":["B"],
"D":["A","E","F"],
"E":["D","F","G"],
"F":["D","E","H"],
"G":["E","H"],
"H":["G","F"]
}

#bfs code
visited = {}
level = {} #distance dictionary
parent = {}
bfs_traversal_output = []
queue = Queue()

for node in adjacency_list.keys():
     visited[node] = False
     parent[node] = None
     level[node] = -1 #infinity

source_node = "A"
visited[source_node] = True
level[source_node] = 0
queue.put(source_node)

while not queue.empty():
    u = queue.get()
    bfs_traversal_output.append(u)

    for vertex in adjacency_list[u]:
        if not visited[vertex]:
            visited[vertex] = True
            parent[vertex] = u
            level[vertex] = level[u] + 1
            queue.put(vertex)
print(bfs_traversal_output)


#shortest path of from any nodes from source node

vertex = "G"
path = []
while vertex is not None:
    path.append(vertex)
    vertex = parent[vertex]
path.reverse()
print(path)
