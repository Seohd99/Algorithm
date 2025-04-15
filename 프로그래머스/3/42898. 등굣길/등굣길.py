def solution(m, n, puddles):
    answer = 0
    map =[[0 for i in range(m)]for i in range(n)]
    
    map[0][0] = 1
    for x, y in puddles:
        map[y-1][x-1] = -1
    for i in range(n):
        for j in range(m): 
            if map[i][j] != -1 and j + 1 < m and map[i][j+1] != -1:
                map[i][j+1] += map[i][j]
            if map[i][j] != -1 and i + 1 < n and map[i+1][j] != -1:
                map[i+1][j] += map[i][j]
    
    return map[-1][-1] % 1000000007