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



def initializing_depth_first_search(graph:list[list[int]],list_of_discovery_time:list,
                                    list_of_end_time:list,list_of_fathers:list,time:int,
                                    time_of_death:int) -> tuple[list,list,list]:
    ''' 
        This function has a purpose to find articulation points in a Graph and test 
        their connectivity after the removal of each vertex

        Parameters:
            graph = This parameter is a list that contain each adjacency list of each
            vertex in a graph.

        Return: 
            articulations = return the vertex that are articulations, which means,
            a vertex that if it will be removed the graph pass to be disconnected 
    '''
    for vertex in range(len(graph)):
        list_of_discovery_time[vertex]=-1
    for vertex in range(len(graph)):
        if list_of_discovery_time[vertex] == -1:
            list_of_fathers[vertex] = vertex
            depth_first_search(graph,vertex,list_of_discovery_time,
                               list_of_end_time,list_of_fathers,time,time_of_death)
        
    return list_of_discovery_time,list_of_end_time,list_of_fathers

def depth_first_search(graph: list[list[int]],vertex:int,list_of_discovery_time:list,
                       list_of_end_time:list,list_of_fathers:list,time:int,
                       time_of_death:int) -> tuple[list,list,list]:
    
    time+=1
    list_of_discovery_time[vertex] = time
    
    for adjacent in graph[vertex]:
        if list_of_discovery_time[vertex]==-1:
            list_of_fathers[adjacent] = vertex
            depth_first_search(graph,adjacent, list_of_discovery_time,
                               list_of_end_time,list_of_fathers,time,time_of_death)
    time_of_death+=1
    list_of_end_time[vertex] = time_of_death

    return  list_of_discovery_time,list_of_end_time,list_of_fathers


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