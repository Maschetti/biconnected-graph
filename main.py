import random

def createRandomGraph(v):
    graph = [[] for _ in range(v)]
    min = int(v)
    max = int((v * (v - 1)) / 2)
    number_edges = random.randint(min, max + 1)
    number_edges = 40

    flag = 0

    while flag < number_edges:
        origin = random.randrange(0, v)
        destiny = random.randrange(0, v)

        if origin is not destiny:
            if destiny not in graph[origin]:
                graph[origin].append(destiny)
                graph[destiny].append(origin)
                flag += 1
    
    # assure the graph is connected
    father, TD, TF = DFS(graph)
    roots = [i for i, x in enumerate(father) if x == None]
    for i in range(len(roots) - 1):
        graph[roots[i]].append(roots[i + 1])
        graph[roots[i + 1]].append(roots[i])

    return graph 

def visit_edge(origin, destiny):
    return None

def DFS_(graph, node, TD, TT, father, t):
    t = t + 1
    TD[node] = t

    for v in graph[node]:
        if TD[v] == 0:
            father[v] = node
            DFS_(graph, v, TD, TT, father, t)
        elif (TT[v] == 0) and not (father[node] == v):
            visit_edge(node, v)
    
    t = t + 1
    TT[node] = t

def DFS(graph):
    t = 0
    TD = []
    TT = []
    father = []
    for i in range(len(graph)):
        TD.append(0)
        TT.append(0)
        father.append(None)
    
    while 0 in TD:
        index = TD.index(0)
        DFS_(graph, index, TD, TT, father, t)
    
    return father, TD, TT


def DFS_search(graph, origin, destiny):
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

def method_one(graph):
    groups = []

    nodes_found = [False for v in graph]

    while False in nodes_found:
        node = nodes_found.index(False)

        cut = [node]
        for n in graph[node]:
            if len(cut) < 2:
                cut.append(n)
            else:
                path = DFS_search(graph, node, n)



    
if __name__ == '__main__':
    v = 40
    graph = createRandomGraph(v)
