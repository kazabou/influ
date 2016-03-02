import networkx as nx
import copy


# novelty decay article sample graph...
pG = nx.DiGraph()

pG.add_edge(1,2)
pG.add_edge(1,3)
pG.add_edge(2,3)
pG.add_edge(3,4)
pG.add_edge(3,5)
pG.add_edge(3,6)
pG.add_edge(4,7)
pG.add_edge(2,8)
pG.add_edge(5,6)

pG[1][2]['weight'] = 0.8
pG[1][2]['delay'] = 2
pG[1][3]['weight'] = 0.7
pG[1][3]['delay'] = 2
pG[2][3]['weight'] = 0.1
pG[2][3]['delay'] = 1
pG[3][4]['weight'] = 0.3
pG[3][4]['delay'] = 3
# novelty decay article sample graph

def greedyAlgorithm(Graph, numberOfSeeds):
    
    seedSet = []
    maxCov = 0
    for i in range(1, numberOfSeeds+1):

        nodes = [x for x in Graph.nodes() if x not in seedSet]
        node = nodes[0] 
        for j in nodes:
            margCov = coverage(seedSet + [j], Graph) - coverage(seedSet, Graph)
            if margCov > maxCov:
                maxCov = margCov
                node = j
        maxCov = 0

        seedSet += [node]
    
    return seedSet


def coverage(listOfNodes, Graph):
    """
    find the number of edges that reach to nodes in the 
    graph but not to nodes in the list
    """
    coverage = len(listOfNodes)
    
    seen = []
    for i in listOfNodes:
        for j in Graph.neighbors(i):
            
            if j not in listOfNodes + seen:
                coverage += 1
                seen.append(j)

    return coverage

#print coverage([1,2], pG)
#print coverage([1,3], pG)
#
seedSet = greedyAlgorithm(pG, 3)

print seedSet, coverage(seedSet, pG)
