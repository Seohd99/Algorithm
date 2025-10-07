n, m = map(int,input().split())
nx = [-1,1,0,0]
ny = [0,0,-1,1]
MAP = []
for _ in range(n):
  MAP.append(list(map(int,input().strip())))

Q = [[0, 0, 1]]
MAP[0][0] = 0
for y, x, d in Q:
  if x + 1 == m and y + 1 == n:
    print(d)
    break
  for i in range(4):
    xx = x + nx[i]
    yy = y + ny[i]
    if xx >= 0 and xx < m and yy >= 0 and yy < n and MAP[yy][xx] == 1:
      Q.append([yy,xx,d+1])
      MAP[yy][xx] = 0
  
    

