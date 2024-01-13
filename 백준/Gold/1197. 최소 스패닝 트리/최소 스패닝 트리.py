import sys

n, m = map(int,input().split())

lst = []

def find(x):
    if lst[x] == x: return lst[x]
    lst[x] = find(lst[x])
    return lst[x]


for i in range(n+1):
    lst.append(i)

SUM = 0
pay = []
for i in range(m):
    pay.append(list(map(int,sys.stdin.readline().split())))

pay.sort(key=lambda x : x[2])

for i in pay:
    x = find(i[0])
    y = find(i[1])
    if x != y:
        SUM += i[2]
        lst[y] = x
print(SUM)