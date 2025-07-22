import sys
input = sys.stdin.readline
n = int(input())

MAP = []
for i in range(n):
    MAP.append(list(input().rstrip()))

MAX = 0
def cnt_candy():
    eat_candy = 0
    for i in range(n):
        pi_cnt = 1
        pj_cnt = 1
        pi = ""
        pj = ""
        for j in range(n):
            if pi == "" and pj == "":
                pi = MAP[i][j]
                pj = MAP[j][i]
                continue
            if MAP[i][j] == pi:
                pi_cnt += 1
            else:
                pi_cnt = 1
            pi = MAP[i][j]
            if MAP[j][i] == pj:
                pj_cnt += 1
            else:
                pj_cnt = 1
            pj = MAP[j][i]
            eat_candy = max(eat_candy, pi_cnt, pj_cnt)
    return eat_candy
        
for i in range(n):

    for j in range(n):
        if n > j + 1 and MAP[i][j] != MAP[i][j+1]:
            MAP[i][j], MAP[i][j+1] = MAP[i][j+1], MAP[i][j]
            MAX = max(cnt_candy(),MAX)
            MAP[i][j], MAP[i][j+1] = MAP[i][j+1], MAP[i][j]
        if n > i + 1 and MAP[i][j] != MAP[i+1][j]:
            MAP[i][j], MAP[i+1][j] = MAP[i+1][j], MAP[i][j]
            MAX = max(cnt_candy(),MAX)
            MAP[i][j], MAP[i+1][j] = MAP[i+1][j], MAP[i][j]
print(MAX)
