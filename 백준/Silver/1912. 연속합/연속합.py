import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n+1)]
n_list = [0] + list(map(int,input().split()))
for i in range(1,n+1):
    dp[i] = n_list[i] + dp[i-1] if n_list[i] + dp[i-1] > n_list[i] else n_list[i]

print(max(dp[1:]))