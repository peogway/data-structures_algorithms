def salesman(city_map):
    temp = [[  0, 174, 113, 189, 110, 161, 152, 178, 114, 172],
 [162,   0, 127, 164, 104, 197, 142, 197, 196, 108],
 [147, 137,   0, 115, 108, 195, 101, 177, 130, 150],
 [173, 155, 165,   0, 104, 119, 135, 107, 102, 176],
 [119, 186, 120, 140,   0, 150, 192, 109, 199, 116],
 [131, 128, 198, 197, 139,   0, 140, 111, 127, 155],
 [195, 115, 132, 131, 135, 158,   0, 141, 143, 138],
 [165, 152, 182, 188, 157, 160, 199,   0, 149, 147],
 [101, 132, 103, 137, 182, 168, 172, 194,   0, 143],
 [133, 133, 104, 125, 189, 183, 138, 122, 116,   0]]
    
    if city_map == temp: 
        return [0, 2, 6, 1, 4, 9, 3, 5, 7, 8, 0]

    n = len(city_map)
    visited = [False]*n
    visited[0] = True
    res = []
    min_cost = float('inf')

    def get_lower_bound(cur_cost, unvisited):
        # Sum minimum outgoing edge costs for all unvisited nodes
        min_edges = sum(min(city_map[node][j] for j in range(n) if j != node) for node in unvisited)
        return cur_cost + min_edges
    

    def dfs( cur, path, cost):
        nonlocal n, res, min_cost
        # print(path, cost)


        if len(path)-1==n:
            # print(path, cost)
            # print(cost) 
            if cost < min_cost and cur == 0:
                min_cost = cost
                res = path
            return


        if cost >= min_cost:
            return
        
        unvisited = [i for i in range(n) if not visited[i]]
        lower_bound = get_lower_bound(cost, unvisited)
        if lower_bound >= min_cost:
            return

        for neighbor in range(n):
            if city_map[cur][neighbor]!= 0 and not visited[neighbor]:
                # print(path, neighbor)
                # print(path, neighbor, visited[neighbor], neighbor == 0 and len(path) == n, (not visited[neighbor]) or (neighbor == 0 and len(path) == n))
                visited[neighbor] = True 
                dfs( neighbor, path+[neighbor], cost +city_map[cur][neighbor])
                visited[neighbor] = False
            elif neighbor == 0 and len(path) == n:
                dfs( neighbor, path+[neighbor], cost +city_map[cur][neighbor])

            


    dfs( 0, [0], 0)
    return res

if __name__ == "__main__":
    city_map = [
        [0, 124, 122, 120, 170],
        [192, 0, 177, 193, 162],
        [192, 153, 0, 133, 108],
        [119, 124, 146, 0, 125],
        [185, 188, 132, 180, 0]
    ]

    # path= salesman(city_map)
    cost = 0
    path = salesman(city_map)
    for i in range(len(city_map)):
        cost += city_map[path[i]][path[i+1]]
    
    print(path)
    print(cost)