class Graph:
    def __init__ (self, n):
        self.size = n
        self.graph = [[] for _ in range(n)]
    def add (self, u, v):
        if 0> u or self.size<=u or 0>v or self.size<=v:
            return
        if u not in self.graph[v]:
            self.graph[v].append(u)
        if v not in self.graph[u]:
            self.graph[u].append(v)
    
    def remove(self, u, v):
        if 0> u or self.size<=u or 0>v or self.size<=v:
            return
        if v in self.graph[u]:
            self.graph[u].remove(v)

        if u in self.graph[v]:
            self.graph[v].remove(u)

    def subgraphs(self):
        count = 0
        visited = [False]*self.size

        for i in range(self.size):
            if not visited[i]:
                count+=1
                stack = [i]
                while stack:
                    cur = stack.pop()
                    if not visited[cur]:
                        visited[cur]= True
                        for neighbor in self.graph[cur]:
                            stack.append(neighbor)
                
        return count

    

if __name__ == "__main__":
  graph = Graph(6)

  edges = ((0, 4), (2, 1), (2, 5), (3, 0), (5, 1))
  for u, v in edges:
      graph.add(u, v)
  

  print(graph.graph)
  print(graph.subgraphs())
  
  more_edges = ((0, 2), (2, 3), (3, 5), (4, 5))
  for u, v in more_edges:
      graph.add(u, v)

  print(graph.subgraphs())