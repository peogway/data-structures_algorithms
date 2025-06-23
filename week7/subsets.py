def subsets(n: int) -> list:
    dp = {}
    dp[1] = [[1]]
    for i in range (2, n+1):
        dp[i] = [*dp[i-1], [i]]
        for subset in dp[i-1]:
            dp[i].append([ *subset,i])
    return dp[n]


if __name__ == "__main__":
    print(subsets(1))
    print(subsets(2)) 
    print(subsets(3)) 
    print(subsets(4)) 

    S = subsets(10)
    print(S[95])
    print(S[254])
    print(S[826])