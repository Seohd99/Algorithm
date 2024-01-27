import sys
sys.setrecursionlimit(150000)

n = int(sys.stdin.readline())
lst = [[]for i in range(n+1)]
d_lst = [0 for i in range(n+1)]
ck  = [0 for i in range(n+1)]
parent = [0 for i in range(n+1)]
def dfs(n, l):
    ck[n] = 1
    d_lst[n] = l

    for i in lst[n]:
        if ck[i] == 0:
            parent[i] = n
            dfs(i,l+1)

def find_P(x, y):
    while(1):
        if x == y:
            return x
        x_l = d_lst[x]
        y_l = d_lst[y]
        if x_l>y_l:
            x = parent[x]
        elif x_l == y_l:
            x = parent[x]
            y = parent[y]
        else:
            y = parent[y]
    return
for i in range(n-1):
    a, b = map(int,sys.stdin.readline().split())
    lst[a].append(b)
    lst[b].append(a)
dfs(1,0)
m = int(sys.stdin.readline())
for i in range(m):
    x, y = map(int,sys.stdin.readline().split())
    print(find_P(x,y))

