import sys
n = int(input())

lst = []
for i in range(n):
    a, b = map(int,sys.stdin.readline().split())
    lst.append((a,1))
    lst.append((b,-1))

lst.sort()
sw = 0
result = 0
for i in lst:
    sw += i[1]
    result = max(result,sw)
print(result)
