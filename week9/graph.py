class Graph:
    def __init__(self,n):
        self.n = n
        self.graph = [[] for i in range(n)]
    
    def dft(self, start):
        stack = [start]
        visits = [False for _ in range(self.n)]
        while stack:
            cur = stack.pop()
            if not visits[cur]:
              print(cur, end = ' ')
              for neighbor in self.graph[cur][::-1]:
                  stack.append(neighbor)
              visits[cur] = True
        print()
    def add(self,u,v):
        if u>self.n or v>self.n or v<0 or u<0: return
        # print(u,v)
        def node_pos(node, neighbors,l,r):
            if len(neighbors) == 0: return 0
            if len(neighbors) ==1: return 0 if node < neighbors[0] else 1
            # print(neighbors,l,r, node)
            if l >= r-1:
                if node < neighbors[l]: return l
                elif node > neighbors[r]: return r+1
                else: return r
            middle = (r+l)//2
            if node < neighbors[middle]:
                return node_pos(node, neighbors,l,middle-1 )
            else:
                return node_pos(node, neighbors, middle+1, r)
        if v not in self.graph[u]:
            self.graph[u].insert(node_pos(v,self.graph[u],0, len(self.graph[u])-1),v)
            # self.graph[u].append(v)
        if u not in self.graph[v]:
            self.graph[v].insert(node_pos(u,self.graph[v],0, len(self.graph[v])-1),u)
            # self.graph[v].append(u)

            
    
    def remove(self,u,v):
        for i,x in enumerate(self.graph[u]):
            if x == v: self.graph[u].pop(i)
        for i,x in enumerate(self.graph[v]):
            if x == u: self.graph[v].pop(i)


if __name__ == "__main__":

  graph = Graph(15)

  connections = ((0, 3), (0, 5), (0, 11), (1, 7), (1, 9),
                   (1, 14), (2, 10), (2, 11), (2, 12), (3, 4),
                   (3, 5), (3, 10), (4, 8), (4, 13), (6, 12),
                   (6, 14), (7, 8), (7, 10), (8, 9), (9, 10),
                   (9, 11), (10, 14), (13, 14), (14, 2), (2, 6))
                
  for u, v in connections:
      graph.add(u, v)
  for i in range(graph.n):
      print(i, graph.graph[i])
  # print(0, graph.graph[0])
  graph.dft(3)
  # graph.dft(9)
  # graph.dft(12)
  # graph.dft(6)
  # graph.dft(0)
  # graph.dft(13)
  # graph.dft(14)