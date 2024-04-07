import random

def BFS(graph, origin, destiny):
    frontier = [[origin]]
    visited = []

    while frontier:
        path = frontier.pop(-1)

        if path[-1] == destiny:
            return path
        
        for v in graph[origin]:
            if not v in visited:
                frontier.append(path + [v])
                visited.append(v)
    
    return None

# def method_one(graph):



def initializing_depth_first_search(graph:list[list[int]], visited:list[int] ,vertex:int) -> None:
    ''' 
        This function has a purpose to find articulation points in a Graph and test their connectivity after the removal of each vertex

        Parameters:
            graph = This parameter is a list that contain each adjacency list of each vertex in a graph.

        Return: 
            articulations = return the vertex that are articulations, which means, a vertex that if it will be removed the graph pass to be disconnected 
    '''
    time = 0
    ## for all vertex inside the graph discovery time and finish time is 0
    list_of_discovery_time = []
    list_of_fathers = []
    list_of_end_time = []
    
    while len(list_of_discovery_time) != len(graph):
        
        
        depth_first_search(0,time,list_of_discovery_time,list_of_end_time,list_of_fathers,graph)    
        
        # if vertex not in visited:
        #     visited.append(vertex)
        #     for neighbour in graph[vertex]:
        #         depth_first_search(graph,visited,neighbour)


def depth_first_search(vertex:int, time:int, discovery_time:list, end_time:list, fathers:list, graph: list[list[int]])->None:
    time += 1
    discovery_time[vertex] = time
    for parents in graph[vertex]:
        if discovery_time[parents]==0:
            fathers[parents] = vertex
            depth_first_search(parents,time,discovery_time,end_time,fathers,graph)
        elif end_time[parents]==0 and parents!=fathers[vertex]:
                n
    time +=1
    end_time[vertex] = time

        

def finding_articulations_in_graph(graph :list) ->list[int]:
    ''' 
        This function has a purpose to find articulation points in a Graph and teste their connectivity after the removal of each vertex

        Parameters:
            graph = This parameter is a list that contain each adjacency list of each vertex in a graph.

        Return: 
            articulations = return the vertex that are articulations, which means, a vertex that if it will be removed the graph pass to be desconexed 
     
    '''
    articulations = []



    return articulations

def createRandomGraph(v):
    graph = [[] for _ in range(v)]
    min = int(v)
    max = int((v * (v - 1)) / 2)
    number_edges = random.randint(min, max + 1)

    flag = 0
    while flag < number_edges:
        origin = random.randrange(0, v)
        destiny = random.randrange(0, v)

        if origin is not destiny:
            if destiny not in graph[origin]:
                graph[origin].append(destiny)
                graph[destiny].append(origin)
                flag += 1
    
    return graph 

if __name__ == '__main__':
    v = 10
    graph = createRandomGraph(v)


    for a in graph:
        if len(a) == 0:
            print("Grafo desconexo")