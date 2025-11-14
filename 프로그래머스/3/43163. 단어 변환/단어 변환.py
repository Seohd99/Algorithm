from collections import deque
def ck_change(b, t):
    dif = 0
    for i in range(len(b)):
        if b[i] != t[i]:
            dif += 1
        if dif > 1:
            return False
    return True
    
def solution(begin, target, words):
    q = deque()
    q.append([begin, 0])
    ck = [0 for _ in range(len(words))]
    while q:
        word, cnt = q.popleft()
        for i in range(len(words)):
            if ck[i] == 0 and ck_change(word, words[i]):
                if words[i] == target:
                    return cnt + 1
                ck[i] = 1
                q.append([words[i], cnt + 1])
    
    return 0
