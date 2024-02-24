n , m = map(int,input().split())

nodes = []
values = [99999999999 for i in range(n+1)]
values[1] = 0
for i in range(m):
    nodes.append(list(map(int,input().split())))

for j in range(n):
    copy_val = values[:]
    hit = 0
    for i in nodes:
        a, b, c = i
        if values[a] == 99999999999:
            continue
        if values[a] + c < values[b]:
            values[b] = values[a] + c
            hit = 1
    
if hit == 1:
        print(-1)
        exit(0)
for i in range(2, n+1):

    print(values[i] if values[i] != 99999999999 else -1)
    