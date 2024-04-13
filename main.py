import random

NUMBER_OF_VERTEX = 7
list_of_discovery_time = [[] for _ in range(NUMBER_OF_VERTEX)]
list_of_fathers = [[] for _ in range(NUMBER_OF_VERTEX)]
list_of_end_time = [[] for _ in range(NUMBER_OF_VERTEX)]
lowest_preorder_number = [[] for _ in range(NUMBER_OF_VERTEX)]

time = 0
time_of_death = 0


def find_matching_positions(vector):
    
    """ 
        Find matching position in a vector. 
        The purpose is find if has more than one root in the depth first search 
        
        Parameters: 
            vector: represent the vector of father of each vertex
        
        Return:
            Return the roots of the forest
    """

    matching_positions = []

    # Iterate through the vector using enumerate to get both index and value
    for index, value in enumerate(vector):
        if value == index:
            matching_positions.append(index)

    return matching_positions
            
            
def remove_vertex_and_return_new_graph(graph: list[list[int]],vertex:int) -> list[list[int]]:
    """ 
        Create a new graph by removing a vertex and its incident edges
        
        Parameters: 
            graph: the original grap
            vertex: the vertex to be removed
        
        Return:
            The new graph after removal
    """
    
    
    new_graph = [neighbors[:] for neighbors in graph]
    new_graph[vertex] = []  
    
    for neighbor in graph[vertex]:
        new_graph[neighbor].remove(vertex)
    
    return new_graph


def number_of_connected_components(graph:list[list[int]]) -> int:
    """ 
        Make a depth_first_search in a graph and capture the vector of fathers
        
        Parameters: 
            graph: the graph to perform the search
            start: the root of the search
        
        Return:
            The number of connected components
    """    

    fathers = [-1 for _ in range(len(graph))]
    discovery = [-1 for _ in range(len(graph))]
    time2=0

    def dfs_recursive(graph, vertex,time2):
        
        time2+=1
        
        discovery[vertex] = time2
        
        for adjacent in graph[vertex]:
            if discovery[adjacent]==-1:
                    fathers[adjacent] = vertex
                    depth_first_search(graph,adjacent)
                    
    for vertex in range(len(graph)):
        if discovery[vertex] == -1:
            dfs_recursive(graph,vertex,time2)
            
    number_of_components = len(find_matching_positions(fathers))


    return number_of_components

            


def finding_articulations(graph: list[list[int]]) -> Tuple[list[int],int,list[int]]:
    """ 
        Make a depth_first_search in a graph and capture the vector of fathers
        
        Parameters: 
            graph: the graph to perform the search
            start: the root of the search
        
        Return:
            The number of connected components
    """        
    original_number_of_components = number_of_connected_components(graph)
    articulations = []
    number_of_components_after_removal_articulation = []
    
    for vertex in range(len(graph)):
        
        new_graph = remove_vertex_and_return_new_graph(graph,vertex)
         

        new_number_of_components = number_of_connected_components(new_graph)
        
        if(original_number_of_components!=new_number_of_components):
            articulations.append(vertex)
            number_of_components_after_removal_articulation.append(new_number_of_components)
    
    return articulations,original_number_of_components,number_of_components_after_removal_articulation

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
        This function has a purpose to find bridges in a Graph

        Parameters:
            graph : This parameter is a list that contain each adjacency list 
            of each vertex in a graph.
    '''    
    initializing_depth_first_search(graph)

    list_of_the_first_to_die =  [[] for _ in range(len(graph))]
    
    for vertex in range(len(graph)):
        list_of_the_first_to_die[list_of_end_time[vertex]] = vertex
    
    for vertex in range(len(graph)):
        
        vertex_that_died_firts = list_of_the_first_to_die[vertex]
        lowest_preorder_number[vertex_that_died_firts] = list_of_discovery_time[vertex_that_died_firts]
        
        for adjacent in graph[vertex_that_died_firts]:
            if list_of_discovery_time[adjacent]<list_of_discovery_time[vertex_that_died_firts]:
                if ( adjacent!=list_of_fathers[vertex_that_died_firts]):
                    lowest_preorder_number[vertex_that_died_firts] = min_between_two_values(list_of_discovery_time[adjacent],
                        lowest_preorder_number[vertex_that_died_firts])
            else:
                if list_of_fathers[adjacent]==vertex_that_died_firts:
                    lowest_preorder_number[vertex_that_died_firts] = min_between_two_values(lowest_preorder_number[adjacent],
                        lowest_preorder_number[vertex_that_died_firts])
    
    
def determine_if_graph_is_biconnected(graph:list[list[int]]) -> bool:
    
    ''' 
        This function has a purpose to determine if a graph is edge biconnected or not using Tarjan's Algorithm

        Parameters:
            graph : This parameter is a list that contain each adjacency list 
            of each vertex in a graph.
    '''    
    finding_articulations_in_graph(graph)
    
    for vertex in range(len(graph)):
        if ((lowest_preorder_number[vertex]==list_of_discovery_time[vertex])
            and (list_of_fathers[vertex]!=vertex)):
            return False
    
    roots = 0
    for vertex in range(len(graph)):
        if list_of_fathers[vertex]==vertex: roots+=1
        if roots>1:
            return False
    
    return True 
    
    
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

    #graph = createRandomGraph(NUMBER_OF_VERTEX)
    graph= [[1],[0, 2, 6],[1, 3, 6],[2, 4, 5],[3, 5],[3, 4],[1, 2]]
    #resposta
    #      v   0  1  2  3  4  5  6
    # pre[v]   0  1  2  3  4  5  6
    # post[v]  6  5  4  2  1  0  3
    # lo[v]    0  1  1  2  3  3  1
    # ebc[v]   2  1  1  0  0  0  1
    
    #graph=[[2, 3],[8],[0, 3, 8],[0, 2, 8],[7, 9, 10],[6, 9],[5, 9],[4, 10],[1, 2, 3, 10],[4, 5, 6],[4, 7, 8]]
        
        #resposta    
        #  v      a  b  c  d  e  f  g   h  i  j  k
        # pre[v]  0  4  1  2  6  9  10  7  3  8  5
        # post[v] 10 0  9  8  5  3  2   1  7  4  6
        # lo[v]   0  4  0  0  5  8  8   5  1  8  5
        
    #initializing_depth_first_search(graph)

    

    # print(f'Graph is biconnected or not?\n {determine_if_graph_is_biconnected(graph)}\n')
    # print(f'List of discovery time of each vertex:\n {list_of_discovery_time}\n')
    # print(f'List of end time of each vertex:\n{list_of_end_time}\n')
    # print(f'List of fathers of each vertex:\n{list_of_fathers}\n')
    # print(f'List of lowest pre order number:\n{lowest_preorder_number}\n')
    
    articulations,original_number_of_components,components_after_removal = finding_articulations(graph)
    print(f'{articulations}\n')
    print(f'{original_number_of_components}\n')
    print(f'{components_after_removal}\n')
