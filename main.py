import random

NUMBER_OF_VERTEX = 7
list_of_discovery_time = [[] for _ in range(NUMBER_OF_VERTEX)]
list_of_fathers = [[] for _ in range(NUMBER_OF_VERTEX)]
list_of_end_time = [[] for _ in range(NUMBER_OF_VERTEX)]
lowest_preorder_number = [[] for _ in range(NUMBER_OF_VERTEX)]

time = 0
time_of_death = 0


def initializing_depth_first_search(graph:list[list[int]]) -> None:
    ''' 
        This function has a purpose to find initializing the depth first search
        in a graph

        Parameters:
            graph = This parameter is a list that contain each adjacency list of each
            vertex in a graph. 
    '''
    for vertex in range(len(graph)):
        list_of_discovery_time[vertex]=-1
    for vertex in range(len(graph)):
        if list_of_discovery_time[vertex] == -1:
            list_of_fathers[vertex] = vertex
            depth_first_search(graph,vertex)
        

def depth_first_search(graph: list[list[int]],vertex:int) -> None:
    ''' 
        Performing the depth first search in graph building the 
        vectors of pre order, post order and fathers.
        

        Parameters:
            graph : This parameter is a list that contain each adjacency list 
            of each vertex in a graph.
    '''   
    global time,time_of_death
    
    list_of_discovery_time[vertex] = time
    time+=1
    
    for adjacent in graph[vertex]:
        if list_of_discovery_time[adjacent]==-1:
                list_of_fathers[adjacent] = vertex
                depth_first_search(graph,adjacent)
    
    list_of_end_time[vertex] = time_of_death
    time_of_death+=1
    

def min_between_two_values(value1:int,value2:int)->int:
    """
    This methods return the minimum between two values
    
    Parameters: 
        value1: integer to be compared 
        value2: integer to be compared 
    
    Return:
        the minimum value
    """    
    return value1 if value1<value2 else value2


def finding_articulations_in_graph(graph:list[list[int]]) -> None:
    ''' 
        This function has a purpose to find articulation points in a Graph and
        test their connectivity after the removal of each vertex

        Parameters:
            graph : This parameter is a list that contain each adjacency list 
            of each vertex in a graph.
    '''
    end_time_sorted =  [[] for _ in range(len(graph))]
    
    for vertex in range(len(graph)):
        end_time_sorted[list_of_end_time[vertex]] = vertex
    
    for vertex in range(len(graph)):
        vertex_auxiliary = end_time_sorted[vertex]
        lowest_preorder_number[vertex_auxiliary] = list_of_discovery_time[vertex_auxiliary]
        for adjacent in graph[vertex_auxiliary]:
            if list_of_discovery_time[adjacent]<list_of_discovery_time[vertex_auxiliary]:
                if ( adjacent!=list_of_fathers[vertex_auxiliary]):
                    lowest_preorder_number[vertex_auxiliary] = min_between_two_values(
                        lowest_preorder_number[vertex_auxiliary],list_of_discovery_time[adjacent])
                else:
                    if list_of_fathers[adjacent]==vertex_auxiliary:
                        lowest_preorder_number[vertex_auxiliary] = min_between_two_values(
                            lowest_preorder_number[vertex_auxiliary],
                            lowest_preorder_number[adjacent])
    
    

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
    NUMBER_OF_VERTEX = 7
    graph = createRandomGraph(NUMBER_OF_VERTEX)
    time = 0
    time_of_death = 0
    ## for all vertex inside the graph discovery time and finish time is 0
    list_of_discovery_time = [[] for _ in range(NUMBER_OF_VERTEX)]
    list_of_fathers = [[] for _ in range(NUMBER_OF_VERTEX)]
    list_of_end_time = [[] for _ in range(NUMBER_OF_VERTEX)]
    lowest_preorder_number = [[] for _ in range(NUMBER_OF_VERTEX)]

    discovery,end,fathers = initializing_depth_first_search(graph,list_of_discovery_time,list_of_end_time,
                                                            list_of_fathers,time,time_of_death)
    print(f'List of discovery time of each vertex:\n {discovery}\n')
    print(f'List of end time of each vertex:\n{end}\n')
    print(f'List of fathers of each vertex:\n{fathers}\n')
    
    articulations = finding_articulations_in_graph(graph,end,discovery,fathers,lowest_preorder_number)
    print(articulations)
    
    
    
    # for a in graph:
    #     if len(a) == 0:
    #         print("Grafo desconexo")