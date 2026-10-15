def solution(n, wires):
    MAP = [[] for _ in range(n  + 1)]
    size = [0 for _ in range(n  + 1)]
    for x, y in wires:
        MAP[x].append(y)
        MAP[y].append(x)
    
    dfs(1, 0, MAP, size)
    return min([abs(size[v] - (n - size[v])) for v in range(1, n + 1)])
def dfs(v, p, MAP, size):
    size[v] = 1
    for i in MAP[v]:
        if i == p: continue
        size[v] += dfs(i, v, MAP, size)
    return size[v]
