import networkx as nx
from Paths import Paths


# novelty decay article sample graph...
pG = nx.DiGraph()

pG.add_edge(1,2)
pG.add_edge(1,3)
pG.add_edge(2,3)
pG.add_edge(3,4)

pG[1][2]['weight'] = 0.8
pG[1][2]['delay'] = 2
pG[1][3]['weight'] = 0.7
pG[1][3]['delay'] = 2
pG[2][3]['weight'] = 0.1
pG[2][3]['delay'] = 1
pG[3][4]['weight'] = 0.3
pG[3][4]['delay'] = 3
# novelty decay article sample graph


def makeTimePathDictionary(G, seeds):
    """ 
    create a dictionary that holds all the time values
    needed to walk through a path
    """

    pathObj = Paths()
    pathSet = pathObj.findAllPaths(pG, seeds)
    timePathD = dict()
    for path in pathSet:
        timePathD[path] = calculateTime(G, path)
    return timePathD


def calculateTime(G, path):
    time = 0
    for i in range(len(path) - 1):
        time += G[path[i]][path[i+1]]['delay']
    return time



def calculateInfluence(G, seeds):
    timePathD = makeTimePathDictionary(G, seeds)
    maxTime = max(timePathD.values())

    for i in range(maxTime+1)



makeTimePathDictionary(pG, [1])
