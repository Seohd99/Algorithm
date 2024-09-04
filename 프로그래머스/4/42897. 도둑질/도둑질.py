def solution(money):
    l = len(money)
    dp = [[0 for i in range(l)]for j in range(2)]
    dp[0][0] = money[0]
    
    for i in range(1,l):
        if i + 1 != l:
            dp[0][i] = max(dp[0][i-1], dp[0][i-2] + money[i])
        dp[1][i] = max(dp[1][i-1], dp[1][i-2] + money[i])

 
    return max(max(dp[0]),max(dp[1]))