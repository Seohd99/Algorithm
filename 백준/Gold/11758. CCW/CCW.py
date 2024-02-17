def CCW(l):
    x = l[0][0] * l[1][1] + l[1][0] * l[2][1] + l[2][0] * l[0][1]
    y = l[1][0] * l[0][1] + l[2][0] * l[1][1] + l[0][0] * l[2][1]
    z = x - y
    if z > 0:
        return 1
    elif z < 0:
        return -1
    else:
        return 0

lst = []
for i in range(3):
    lst.append(list(map(int,input().split())))

print(CCW(lst))