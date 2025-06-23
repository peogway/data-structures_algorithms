class Graph:
    def __init__(self, n):
        self.size = n 
        self.graph = [[0]*n for _ in range(n)]
        self.adj = [[] for _ in range(n)]

    def add(self, u, v, w):
        if 0> u or self.size<=u or 0>v or self.size<=v:
            return
        
        self.graph[u][v] = w
        if v not in self.adj[u]:
            self.adj[u].append(v)

    def remove (self, u, v):
        if 0> u or self.size<=u or 0>v or self.size<=v:
            return
        self.graph[u][v] = 0

        if v in self.adj[u]:
            self.adj[u].remove(v)

    def all_paths(self):
        res = [[0]*self.size for _ in range(self.size)]
        for i in range(self.size):
            cal = self.dijkstra(i)
            for j in range(self.size):
                res[i][j] = -1 if cal[j] == float('inf') else cal[j]

        return res

    def dijkstra(self, start_vertex):
        distances = [float('inf')] * self.size
        distances[start_vertex] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            min_distance = float('inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i

            if u is None:
                break

            visited[u] = True

            for v in range(self.size):
                if self.graph[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.graph[u][v]
                    if alt < distances[v]:
                        distances[v] = alt

        return distances

if __name__ == "__main__":
    def display(M):
        for weights in M:
            for weight in weights:
                print(f"{weight:3d}", end="")
            print()
    graph = Graph(6)

    connections = (( 1,  2, 17), ( 4,  6, 14), ( 2,  5, 15),
                ( 3,  4,  3), ( 0,  5, 18), ( 3,  5,  8),
                ( 2,  0,  9), ( 0,  2, 19), ( 0,  1, 10),
                ( 1,  0, 13), ( 4,  1, 12), ( 5,  1,  3))

    for u, v, w in connections:
        graph.add(u, v, w)

    A = graph.all_paths()

    display(A)
    print()
    print()
    # display(graph.adj)
    print()
    graph.remove(3, 4)
    graph.remove(1, 0)
    graph.remove(4, 1)

    display(graph.graph)
    print()
    for i in range(graph.size):
        print(f'{i}: {graph.adj[i]}')
    print()

    A = graph.all_paths()
    display(A)
