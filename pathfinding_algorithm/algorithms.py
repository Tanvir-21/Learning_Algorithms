import json
from queue import Queue

#loading the graph

def load_graph(file_name):
    with open(file_name) as f:
        data = json.load(f)
        return data

#variables

queue = Queue() #inititalize a queue

def find_shortest_path_bfs(graph,start_point,end_point):
    #keep track all the path to be checked
    visited = []#list to keep track of visited nodes
    queue = [[start_point]]
    bfs_output = []

    #return path if the start goal is the end goal
    if start_point == end_point:
        return "Bro, you started at this point"

    if start_point not in graph.keys():
        print("Bro, please give a valid input")

    #keeps looping until all possible path have been explored
    while queue:
        #pop the first path from the queue
        path = queue.pop(0)
        #get the last node from the path
        node = path[-1]

        if node not in visited:
            neighbours = graph[node]
            #go through all the neighbours node and construct a new path and push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                #return the path if neighbour is the end_point
                if neighbour == end_point:
                    print(new_path)
                    return new_path
            #now mark the new node as explored
            visited.append(node)



    print("no such path is matching")

file = load_graph('dhakaexample.json')
find_shortest_path_bfs(file,"shewrapara","shymoli")
#finding complexity 
valuelist = []
for key, value in file.items():
    values =int(len(list(filter(None,value))))
    valuelist.append(values)
    #print(values)
key_count = len(file)

time_complexity = valuelist[1]+ key_count
print(time_complexity)
