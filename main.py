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
    v = 40
    graph = createRandomGraph(v)

    for a in graph:
        if len(a) == 0:
            print("Grafo desconexo")