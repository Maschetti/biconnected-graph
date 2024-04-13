import random

NUMBER_OF_VERTEX = 7
list_of_discovery_time = [[] for _ in range(NUMBER_OF_VERTEX)]
list_of_fathers = [[] for _ in range(NUMBER_OF_VERTEX)]
list_of_end_time = [[] for _ in range(NUMBER_OF_VERTEX)]
lowest_preorder_number = [[] for _ in range(NUMBER_OF_VERTEX)]

time = 0
time_of_death = 0


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
        if list_of_discovery_time[adjacent]==-1:
            list_of_fathers[adjacent] = vertex
            depth_first_search(graph,adjacent, list_of_discovery_time,
                               list_of_end_time,list_of_fathers,time,time_of_death)
        time_of_death+=1
        list_of_end_time[vertex] = time_of_death

    return  list_of_discovery_time,list_of_end_time,list_of_fathers

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

def finding_articulations_in_graph(graph:list, end_list:list, discovery_list:list,
                                   father_list:list, lowest_pre_order_number:list) ->Union[list[int],None]:
    ''' 
        This function has a purpose to find articulation points in a Graph and
        test their connectivity after the removal of each vertex

        Parameters:
            graph : This parameter is a list that contain each adjacency list 
            of each vertex in a graph.
            end_list : List of end time built in depth_first_search method
            discovery_list : List of discovery time built in depth_first_search method
            father_list : List of father of each vertex built in depth_first_search method
            lowest_pre_order_number : List to accommodate the lower pre_order number of each vertex

        Return: 
            articulations : return the vertex that are articulations, which means,
            a vertex that if it will be removed the graph pass to be disconnected 
            None : return None in len(articulations) = 0
    '''
    articulations_local = []
    end_time_sorted =  [[] for _ in range(len(graph))]
    
    for vertex in range(len(graph)):
        end_time_sorted[end_list[vertex]] = vertex
    
    for vertex in range(len(graph)):
        vertex_auxiliary = end_time_sorted[vertex]
        lowest_pre_order_number[vertex_auxiliary] = discovery_list[vertex_auxiliary]
        for adjacent in graph[vertex_auxiliary]:
            if discovery_list[adjacent]<discovery_list[vertex_auxiliary]:
                if ( adjacent!=father_list[vertex_auxiliary]):
                    lowest_pre_order_number[vertex_auxiliary] = min_between_two_values(
                        lowest_pre_order_number[vertex_auxiliary],discovery_list[adjacent])
                else:
                    if father_list[adjacent]==vertex_auxiliary:
                        lowest_pre_order_number[vertex_auxiliary] = min_between_two_values(
                            lowest_pre_order_number[vertex_auxiliary],
                            lowest_pre_order_number[adjacent])
    
    for index, (preoder,lowest_preorder) in enumerate(zip(discovery_list,lowest_pre_order_number)):
        if preoder==lowest_preorder:
            articulations_local.append(index)
    
    return articulations_local if len(articulations_local)!=0 else None

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