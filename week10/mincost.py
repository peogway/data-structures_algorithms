from collections import deque

class Graph:
    def __init__(self, n):
        self.size = n 
        self.graph = []
        self.adj = [[] for _ in range(n)]

    def add(self, u, v, w):
        if 0> u or self.size<=u or 0>v or self.size<=v:
            return
        
        self.graph.append([u, v, w])

    def find(self, parent, i): 
        if parent[i] != i: 

            parent[i] = self.find(parent, parent[i]) 
        return parent[i] 

    def remove (self, u, v):
        if 0> u or self.size<=u or 0>v or self.size<=v:
            return
        pos = -1
        for i, ele in enumerate(self.graph):
            # print([u,v], ele[:-1])
            if [u,v] == ele[:-1] or [v,u] == ele[:-1]:
                # print('hello', ele)
                pos = i
                break

        # print(pos, self.graph[pos])
        if pos != -1: 
            self.graph.pop(pos)

    def union(self, parent, rank, x, y): 

        if rank[x] < rank[y]: 
            parent[x] = y 
        elif rank[x] > rank[y]: 
            parent[y] = x 

        else: 
            parent[y] = x 
            rank[x] += 1


    def min_cost(self): 
  
        result = [] 
  
        i = 0

        e = 0

        self.graph = sorted(self.graph, 
                            key=lambda item: item[2]) 
  
        parent = [] 
        rank = [] 

        for node in range(self.size): 
            parent.append(node) 
            rank.append(0) 
  
        while e < self.size - 1: 
  
            u, v, w = self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent, v) 
  
            if x != y: 
                e = e + 1
                result.append([u, v, w]) 
                self.union(parent, rank, x, y) 
  
        minimumCost = 0
        for u, v, weight in result: 
            minimumCost += weight 


        return minimumCost

if __name__ == "__main__":
    graph = Graph(10)

    connections = ((0, 2, 7), (0, 8, 15), (1, 3, 9), (2, 3, 7),
                (2, 7, 11), (2, 9, 14), (3, 6, 12), (3, 8, 11),
                (3, 9, 8), (4, 5, 9), (4, 6, 8), (4, 7, 9),
                (4, 9, 7), (5, 6, 11), (5, 7, 9), (5, 9, 8),
                (6, 7, 15), (6, 8, 12), (6, 9, 11), (7, 9, 10))

    for u, v, w in connections:
        graph.add(u, v, w)

    print(graph.graph)
    print(graph.min_cost())
    print()
    connections = ((4, 6), (4, 9), (0, 2), (2, 3), (9, 5))

    for u, v in connections:
        graph.remove(u, v)
    # graph.remove(4,5)
    print(graph.graph)

    print(graph.min_cost())
    print()

    connections = ((0, 1, 7), (2, 0, 5), (7, 6, 5), (2, 7, 8))

    for u, v, w in connections:
        graph.add(u, v, w)

    print(graph.graph)
    print(graph.min_cost())

    print()