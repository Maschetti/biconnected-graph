import random

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

    for line in graph:
        print(line)

    roots = [i for i, x in enumerate(father) if x == None]
    for i in range(len(roots) - 1):
        graph[roots[i]].append(roots[i + 1])
        graph[roots[i + 1]].append(roots[i])

    return graph 

def findCycle(graph, TD, TT, start, node):
    for n in graph[node]:
        if TD[n] <= TD[start] and TT[n] >= TT[start]:
            return True
        if TD[node] == TD[n] + 1:
            findCycle(graph, TD, TT, start, n)

    return False

def hasCicle(graph, TD, TT, node1, node2):
    if TD[node1] < TD[node2]:
        start = node1
        destiny = node2
    else:
        start = node2
        destiny = node1

    return findCycle(graph, TD, TT, start, destiny)
    
if __name__ == '__main__':
    v = 500
    graph = testGraph()
    father, TD, TT = DFS(graph)

    if hasCicle(graph, TD, TT, 0, 7):
        print("ACHOU")
    else:
        print("nao achou")
