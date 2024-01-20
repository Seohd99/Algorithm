dp = [[1,0],[0,1]]
for i in range(2, 41):
    dp.append([dp[i-1][0]+dp[i-2][0],dp[i-1][1]+dp[i-2][1]])

n = int(input())
for i in range(n):
    t = int(input())
    print("%d %d"%(dp[t][0],dp[t][1]))

