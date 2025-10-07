from collections import deque

x, y = map(int,input().split())
visit = [-1] * 100001
Q = deque([x])
visit[x] = 0
cnt = 0
T = -1
while Q:
  v = Q.popleft()
  if v == y:
    T = visit[v]
    cnt += 1
  for i in [v+1, v-1, v*2]:
    if i < 0 or i > 100000:
      continue
    if visit[i] == visit[v] + 1 or visit[i] == -1:
      Q.append(i)
      visit[i] = visit[v] + 1

print(T)
print(cnt)