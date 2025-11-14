from collections import deque
def solution(n, computers):
    q = deque()
    answer = 0
    ck = [0 for _ in range(n)]
    for i in range(n):
        if ck[i] == 1: continue
        answer += 1
        q.append(i)
        while q:
            x = q.popleft()
            ck[x] = 1
            for j in range(n):
                if x == j: continue
                if computers[x][j] == 1 and ck[j] == 0:
                    ck[j] = 1
                    q.append(j)
            
    return answer