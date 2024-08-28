x,y = map(int,input().split())
np = [-1, 0, 1]
MIN = 9999999
MAP = []

def FIND(xx, yy, bf, C):
    global MIN
    C += MAP[xx][yy]

    if xx + 1 == len(MAP):
        if MIN > C:
            MIN = C
        return
    for i in np:
        if bf == i:
            continue
        ny = i + yy
        if ny >= 0 and ny < len(MAP[0]):
            FIND(xx+1, ny, i, C)
    return


# MIN = [[0 for i in range(y)]for j in range(x)]

for i in range(x):
    MAP.append(list(map(int,input().split())))

for i in range(y):
    FIND(0,i,2,0)

print(MIN)
