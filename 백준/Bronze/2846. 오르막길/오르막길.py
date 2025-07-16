n = int(input())
arr = list(map(int, input().split()))

ans = 0
start = arr[0]

for i in range(1, n):
    if arr[i] > arr[i - 1]:
        continue
    else:
        ans = max(ans, arr[i - 1] - start)
        start = arr[i]
ans = max(ans, arr[-1] - start)
print(ans)
