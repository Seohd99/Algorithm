

dp= [[0,1,1,1,1,1,1,1,1,1]]


for i in range(100):
    app = [0 for _ in range(10)]
    for j in range(10):
        if j - 1 >= 0:
            app[j-1] += dp[i][j]
        if j + 1 < 10:
            app[j+1] += dp[i][j]
    dp.append(app)
n = int(input())
print(sum(dp[n-1])%1000000000) 

