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
    """
    we need to calculate the influence as time passes.
    To do this we need to get the paths that their 
    delay matches the "current time". Then to calculate 
    the influence we need to "traverse" the path to check
    the probabilities.
    """
    timePathD = makeTimePathDictionary(G, seeds)
    maxTime = max(timePathD.values())
    probDic = {} # probability for every node
    for node in seeds:
        probDic[node] = 1
    activateTries = {}
    activateTriesPairs = set()
    for time in xrange(maxTime+1):
        # for path which value is equal to the current time
        for path in [p for p in timePathD if timePathD[p] == time]:
            print path
            # pathProb = 1
            # for i in xrange(len(path)-1):
            #     pathProb *= probDic[path[i]] * G[path[i]][path[i+1]]['weight']
            pathProb = probDic[path[-2]] * G[path[-2]][path[-1]]['weight']

            if path[-1] not in  probDic:
                activateTries[path[-1]] = 1
                activateTriesPairs.add((path[-2],path[-1]))
                probDic[path[-1]] = pathProb
            else:
                if (path[-2], path[-1]) not in activateTriesPairs:
                    activateTries[path[-1]] += 1
                    activateTriesPairs.add((path[-2],path[-1]))
                    probDic[path[-1]] += (1 - probDic[path[-1]])*pathProb*(0.3**(activateTries[path[-1]] - 1))
                    #probDic[path[-1]] += (1 - probDic[path[-1]])*probDic[path[-2]]*(0.3**(activateTries[path[-1]] - 1))

            print probDic


    influence = sum(probDic.values())
    return influence

#
print calculateInfluence(pG, [1])
# print calculateInfluence(pG, [1,2])
# print calculateInfluence(pG, [1,2,3])



def getAllPaths(graph, seedSet, targetNode):
    """
    :param graph:
    :param seedSet:
    :param targetNode:
    :return:
    """

    for seed in seedSet:
        for path in nx.all_simple_paths(pG, seed, targetNode):
            if set([x for x in seedSet if x != seed]).isdisjoint(path):
                yield path






for path in getAllPaths(pG, [1,2], 3):
    print path






# makeTimePathDictionary(pG, [1])
