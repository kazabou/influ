import networkx as nx

graph = nx.DiGraph()

graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(2,3)
graph.add_edge(3,4)
graph.add_edge(3,5)
graph.add_edge(4,6)
graph.add_edge(5,6)


graph[1][2]['weight'] = 0.8
graph[1][2]['delay'] = 2
graph[1][3]['weight'] = 0.7
graph[1][3]['delay'] = 2
graph[2][3]['weight'] = 0.1
graph[2][3]['delay'] = 1
graph[3][4]['weight'] = 0.3
graph[3][4]['delay'] = 3
graph[3][5]['weight'] = 0.5
graph[3][5]['delay'] = 3
graph[4][6]['weight'] = 0.4
graph[4][6]['delay'] = 3
graph[5][6]['weight'] = 0.8
graph[5][6]['delay'] = 3




# to get the neighbors...
# print graph.neighbors(1)


def influence(graph, seed):
    """
    single pass belief propagation.
    """
    s = 0
    p = {}
    for node in graph.nodes():
        product = 1.0
        if node in seed:
            p[node] = 1
        else:
            for pred in graph.predecessors(node):
                product *= (1 - p[pred]*graph[pred][node]['weight'])
            p[node] = 1 - product
        s += p[node]
    return s


def naiveGreedy(graph, limit):
    S = []
    D = {}
    V = graph.nodes()
    while V:
        for u in V: 
            D[u] = influence(graph, S+[u]) - influence(graph, S)
        # get the key with the maximum value
        u = max(D, key=D.get)
        D = {}
        if len(S) +1 <= limit:
            S.append(u)
            V.remove(u)
        else:
            break
    return S


#print (seed = naiveGreedy(graph, 1)), calculateInfluence(graph, seed)
#print naiveGreedy(graph, 2)
#print naiveGreedy(graph, 3)
#print naiveGreedy(graph, 4)







def calculateInfluence(graph, seedSet):
    inf = len(seedSet)
    availableEdges = []
    for seed in seedSet:
        for neighb in graph.neighbors(seed):
            if neighb not in seedSet:
                availableEdges.append([seed, neighb])

#    for i in xrange(20):
#        if any

#    for edge in availableEdges:
#        print edge
#        print graph[edge[0]][edge[1]]['delay']
#
   
    






# calculateInfluence(graph, [1,2])
    
        


for i in xrange(1,4):
    seed = naiveGreedy(graph, i)
    print seed, influence(graph, seed)





