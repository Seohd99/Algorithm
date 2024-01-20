n, m = map(int,input().split())
enter = [0 for i in range(n+1)]
go = [[]for i in range(n+1)]
q = []
for i in range(m):
    a , b = map(int,input().split())
    go[a].append(b)
    enter[b] += 1

def mi(x):
    for i in go[x]:
        enter[i] -= 1
        if enter[i] == 0:
            q.append(i)


for i in range(1,len(enter)):
    if enter[i] == 0:
        q.append(i)

for i in q:
    mi(i)

print(*q)