n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int,input().split())))


def CCW(l):
    x = l[0][0] * l[1][1] + l[1][0] * l[2][1] + l[2][0] * l[0][1]
    y = l[1][0] * l[0][1] + l[2][0] * l[1][1] + l[0][0] * l[2][1]
    z = x - y
    return z / 2
area = 0
for i in range(n-2):
    test = []
    test.append(lst[0])
    test.append(lst[i+1])
    test.append(lst[i+2])
    area += CCW(test)

if area < 0:
    area *= -1
print(area)

    

