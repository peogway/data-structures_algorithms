def jumps(n, a, b):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        if i >= a:
            dp[i] += dp[i - a]
        if i >= b:
            dp[i] += dp[i - b]
    
    return dp[n]

if __name__ == "__main__":
    print(jumps(4, 1, 2))     # Output: 5
    print(jumps(8, 2, 3))     # Output: 4
    print(jumps(11, 6, 7))    # Output: 0
    print(jumps(30, 3, 5))    # Output: 58
    print(jumps(100, 4, 5))   # Output: 1167937
