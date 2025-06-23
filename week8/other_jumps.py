def jumps(n, a, b):
    dp = [-1] * (n + 1)
    dp[0]=1
    def cal(n,a,b):
        # if n<0:
        #     return 0
        if n ==0: return 1
        if dp[n] != -1:
            return dp[n]
        ways_from_a = cal(n - a, a, b) if n - a >= 0 else 0
        ways_from_b = cal(n - b, a, b) if n - b >= 0 else 0
        dp[n] = ways_from_a + ways_from_b
        return dp[n]
    
    return cal(n,a,b)

if __name__ == "__main__":
    print(jumps(4, 1, 2))     # Output: 5
    print(jumps(8, 2, 3))     # Output: 4
    print(jumps(11, 6, 7))    # Output: 0
    print(jumps(30, 3, 5))    # Output: 58
    print(jumps(100, 4, 5))   # Output: 1167937
