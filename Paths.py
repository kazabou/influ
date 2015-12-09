
class Paths:
    """
    Find all paths from a seed set to all the nodes in 
    the graph that are not part of the seed set.
    """
    
    def findAllPaths(self, G, seeds):
        paths = set()
        for seed in seeds:
            self.dfs(paths, G, seed, seeds)
        return paths
    
    
    def dfs(self, paths, G, seed, seeds):
        s = []
        s.append(seed)
        discovered = []    
        while s:
            v = s.pop(0)
            if v not in discovered:
                discovered.append(v)
                
                if v in G.neighbors(seed):
                    path = (seed, v)
                    paths.add(path)

                if paths:
                    newPathSet = set()
                    for path in paths:
                        if path[-1] in G.predecessors(v):
                            newpath = list(path)+[v]
                            newPathSet.add(tuple(newpath))

                    for path in newPathSet:
                        paths.add(path)
                    
                for n in [x for x in G.neighbors(v) if x not in seeds]:
                    s.append(n)




