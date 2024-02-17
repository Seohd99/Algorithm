import sys
n = int(input())

lst = []
for i in range(n):
    a, b = map(int,sys.stdin.readline().split())
    lst.append((a,1))
    lst.append((b,-1))

lst.sort()
sw = 0
SUM = 0
for i in lst:
    if 1 == i[1]:
        sw += 1
        if sw == 1:
            s = i[0]
    else:
        sw -= 1
        if sw == 0:
            SUM += (i[0] - s)
print(SUM)




