n , k = map(int,input().split())
bag = []
for i in range(n):
    bag.append(list(map(int,input().split())))


# 비재귀 버전

dp = [0 for i in range(k+1)]
 
for w, v in bag:
    for i in range(k,w-1,-1):
        wv = dp[i-w]+v
        if dp[i] < wv:
            dp[i] = wv

print(dp[-1])
