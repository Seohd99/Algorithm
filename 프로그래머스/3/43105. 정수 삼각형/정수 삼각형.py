def solution(triangle):
    dp = []
    for i in triangle:
        dp.append([0 for j in range(len(i))])
    dp[0][0] = triangle[0][0]
    for i in range(1,len(dp)):
        for j in range(len(dp[i])):
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i-1][j]
            elif i == j:
                dp[i][j] = triangle[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] = triangle[i][j] + max(dp[i-1][j],dp[i-1][j-1])
    return max(dp[-1])