from collections import deque

x, y = map(int,input().split())
visit = [0] * 100001 
Q = deque([[x, 0]])
visit[x] = 1
while Q:
  v, t = Q.popleft()
  if v == y:
    print(t)
    break
  for i in [v+1, v-1, v*2]:
    if i < 0 or i > 100000 or visit[i] == 1:
      continue
    Q.append([i, t+1])
    visit[i] = 1
