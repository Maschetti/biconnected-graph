import random
import networkx as nx

def testGraph():
    return [[1, 2],
            [0, 2, 3],
            [0, 1, 4, 5],
            [1, 6, 7],
            [2, 5, 8],
            [2, 4, 8],
            [3, 7, 9],
            [3, 6, 10],
            [4, 5],
            [6, 10],
            [7, 9]
        ]

def visit_edge(origin, destiny):
    return None

def DFS_(graph, node, TD, TT, father, t):
    t[0] += 1
    TD[node] = t[0]

    for v in graph[node]:
        if TD[v] == 0:
            father[v] = node
            DFS_(graph, v, TD, TT, father, t)
        elif (TT[v] == 0) and father[node] != v:
            visit_edge(node, v)
    
    t[0] += 1
    TT[node] = t[0]

def DFS(graph):
    t = [0]
    TD = []
    TT = []
    father = []
    for i in range(len(graph)):
        TD.append(0)
        TT.append(0)
        father.append(None)
    
    for i in range(len(graph)):
        if TD[i] == 0:
            DFS_(graph, i, TD, TT, father, t)
    
    return father, TD, TT

def random_graph_generator(v):
    graph = nx.random_tree(v)

    number_edges = random.randint(0, v * (v - 1) // 2 - v * 0.3)

    for _ in range(number_edges):
        # Choose a random edge from the existing graph
        edge = random.choice(list(graph.edges()))
        
        # Choose a random node not in the current edge
        new_node = random.choice([node for node in range(v) if node not in edge])
        
        # Add the new edge to the graph
        graph.add_edge(edge[0], new_node)

    # Return the adjacency list representation of the graph
    return [node for node, edges in enumerate(graph)]


def createRandomGraph(v):
    graph = [[] for _ in range(v)]
    min = int(v)
    max = int((v * (v - 1)) / 2)
    number_edges = random.randint(min, max + 1) * 0.2

    flag = 0

    while flag < number_edges:
        origin = random.randrange(0, v)
        destiny = random.randrange(0, v)

        if origin != destiny:
            if destiny not in graph[origin]:
                graph[origin].append(destiny)
                graph[destiny].append(origin)
                flag += 1
    
    # assure the graph is connected
    father, TD, TF = DFS(graph)

    for line in graph:
        print(line)

    roots = [i for i, x in enumerate(father) if x == None]
    for i in range(len(roots) - 1):
        graph[roots[i]].append(roots[i + 1])
        graph[roots[i + 1]].append(roots[i])

    return graph 

def filter_subsets(list_of_lists):
    result = []

    while list_of_lists:
        sub = list_of_lists.pop(0)

        isSub = False
        for l in list_of_lists:
            if set(sub).issubset(set(l)):
                isSub = True
                break
        
        for r in result:
            if set(sub).issubset(set(r)):
                isSub = True
                break

        if not isSub:
            result.append(sub)
    return result

def dfs(graph, start, node, visited, path, cycles):
    visited[node] = True
    path.append(node)
    
    for neighbor in graph[node]:
        if neighbor == start:
            cycle = sorted(path)

            if cycle not in cycles:
                cycles.append(cycle)
        elif not visited[neighbor]:
            dfs(graph, start, neighbor, visited, path, cycles)
    
    path.pop()
    visited[node] = False

def find_cycles(graph):
    cycles = []
    for node in range(len(graph)):
        visited = [False for node in graph]
        dfs(graph, node, node, visited, [], cycles)
    
    cycles = filter_subsets(cycles)
    
    return cycles

if __name__ == '__main__':
    v = 50
    graph = random_graph_generator(v)
    print(graph)
    
    # print(find_cycles(graph))


    
