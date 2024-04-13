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

def visit_edge(origin, destiny, cycles, father):
    new_cycle = [origin]
    while origin != destiny:
        new_cycle.append(father[origin])
        origin = father[origin]

    cycles.append(new_cycle)
    return None

def DFS_(graph, node, TD, TT, father, t, cycles):
    t[0] += 1
    TD[node] = t[0]

    for v in graph[node]:
        if TD[v] == 0:
            father[v] = node
            DFS_(graph, v, TD, TT, father, t, cycles)
        elif (TT[v] == 0) and father[node] != v:
            if cycles != None:
                visit_edge(node, v, cycles, father)
    
    t[0] += 1
    TT[node] = t[0]

def DFS(graph, cycles=None):
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
            DFS_(graph, i, TD, TT, father, t, cycles)

    return father, TD, TT

def random_graph_generator(v):
    graph = nx.random_tree(v)

    number_edges = random.randint(0, v * (v - 1) // 2 - v * 0.1)

    for _ in range(number_edges):
        edge = random.choice(list(graph.edges()))
        
        new_node = random.choice([node for node in range(v) if node not in edge])
        
        graph.add_edge(edge[0], new_node)

    graph = nx.to_dict_of_lists(graph)
    return [graph[i] for i in range(len(graph))]

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

def miss_edges(graph, cycles):
    for vertex, neighbors in enumerate(graph):
        for neighbor in neighbors:
            found = False
            for cycle in cycles:
                if vertex in cycle and neighbor in cycle:
                    found = True
                    break
            if not found:
                cycles.append([vertex, neighbor])


def join_cycles(list_cycles):
    result = []
    while list_cycles:
        cycle = list_cycles.pop(0)

        flag = False
        positions = []
        for idx, other_cycle in enumerate(list_cycles):
            common_elements = set(cycle).intersection(other_cycle)
            if len(common_elements) >= 2:
                flag = True
                cycle = list(set(cycle + other_cycle))
                positions.append(idx)

        if flag:
            new_list = [list_cycles[i] for i in range(len(list_cycles)) if i not in positions]
            list_cycles = new_list + [cycle]
        else:
            result.append(cycle)
    
    return result   

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

def method_one(graph):
    cycles = []
    TD, TT, father = DFS(graph, cycles)
    # cycles = join_cycles(cycles)
    # miss_edges(graph, cycles)
    return cycles
if __name__ == '__main__':
    v = 50
    graph = createRandomGraph(v)
    # graph = testGraph()
    print(method_one(graph))
    
