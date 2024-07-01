def solution(land):
    
    dp = [[0 for i in range(4)]for j in range(len(land))]
    
    for i in range(4):
        dp[0][i] = land[0][i]
    
    for i in range(1,len(land)): # 행 위치
        for j in range(4): # 현재 열 위치
            for k in range(4): # 비교 대상 열 위치
                if j != k:
                    dp[i][j] = max(dp[i][j], dp[i-1][k] + land[i][j])
    
    
    return max(dp[-1])