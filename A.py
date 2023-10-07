import sys

def create_graph(inst:str):
    string = inst.split('\n')
    n_cities = int(string[0])
    neigh = string[1:]

    graph = {}

    for n in range(n_cities):
        ne = neigh[n].split(' ')
        graph[n] = [int(ne[0]),int(ne[1]),int(ne[2])]

    return graph

def count_tetrahedrons(graph):
    num_tetrahedrons = 0
    n_cities = len(graph)

    for city1 in range(n_cities):
        for city2 in range(city1 + 1, n_cities):
            for city3 in range(city2 + 1, n_cities):
                for city4 in range(city3 + 1, n_cities):
                    if (city2 in graph[city1] and
                        city3 in graph[city1] and
                        city4 in graph[city1] and
                        city3 in graph[city2] and
                        city4 in graph[city2] and
                        city4 in graph[city3]):
                        num_tetrahedrons += 1

    return num_tetrahedrons

def run():
    graph = create_graph(sys.stdin.readline().strip())
    tetrahedron_count = count_tetrahedrons(graph)
    print(tetrahedron_count)

run()
