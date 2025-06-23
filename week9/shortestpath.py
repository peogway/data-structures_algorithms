class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = [[0] * n for _ in range(n)]
        self.adj = [[] for _ in range(n)]

    def add(self, u, v, w):
        if u >= self.n or v >= self.n or v < 0 or u < 0:
            return
        self.graph[u][v] = w
        self.adj[u].append(v)

    def shortest_path(self, start, end):
        res = -1
        all_path = set()
        visited = [False] * self.n
        min_sum = float('inf')

        def dfs(start, current_sum, path):
            nonlocal min_sum, res
            visited[start] = True
            if start == end:
                path_tuple = tuple(path + [start])
                if (path_tuple, current_sum) not in all_path: 
                    all_path.add((path_tuple, current_sum))
                if current_sum < min_sum:
                    min_sum = current_sum
                    res = path + [start]
            else:
                for neighbor in self.adj[start]:
                    if not visited[neighbor]:
                        dfs(neighbor, current_sum + self.graph[start][neighbor], path + [start])

            visited[start] = False 

        dfs(start, 0, [])
        if res == -1:
            return -1
        
        for node in res: print(node, end = ' ')
        print()
        return 

if __name__ == "__main__":
    graph = Graph(7)

    connections = ((0, 2, 10), (0, 3, 9), (1, 3, 9),
                   (1, 5, 8), (2, 5, 13), (3, 4, 9),
                   (4, 1, 14), (5, 1, 7), (5, 4, 13),
                   (5, 6, 15), (6, 0, 10), (6, 1, 12))

    for u, v, w in connections:
        graph.add(u, v, w)

    graph.shortest_path(0, 1)
    graph.shortest_path(3, 2)
    graph.shortest_path(4, 6)

    connections = ((0, 4, 15), (5, 2, 7), (2, 6, 5))

    for u, v, w in connections:
        graph.add(u, v, w)

    graph.shortest_path(0, 1)
    graph.shortest_path(3, 2)
    graph.shortest_path(4, 6)
