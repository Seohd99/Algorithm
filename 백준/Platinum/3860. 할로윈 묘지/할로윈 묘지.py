INF = int(1e12)
import sys
while(True): 

    w, h =map(int,sys.stdin.readline().split())
    if (w == 0 and h == 0):
        break
    
    MAP = [INF for i in range(w*h)]
    MAP[0] = 0
    nodes = []

    g = int(sys.stdin.readline())
    for i in range(g):  # 묘비처리
        x, y = map(int,sys.stdin.readline().split())
        MAP[y*w+x] = -1

    e = int(sys.stdin.readline())
    for i in range(e):  # 묘지구멍
        x1, y1, x2, y2, time = map(int,sys.stdin.readline().split())
        nodes.append([y1*w+x1,y2*w+x2,time])
        MAP[y1*w+x1] = -2

    for i in range(w*h):
        if MAP[i] == -1:
            continue
        elif MAP[i] == -2:
            MAP[i] = INF
            continue
        else:
            if w*h > i+w and MAP[i+w] != -1: # 위 연결
                nodes.append([i, i+w, 1])
            if w > i%w+1 and MAP[i+1] != -1: # 오른쪽 연결
                nodes.append([i, i+1, 1]) 
            if -1 < i-w and MAP[i-w] != -1: # 아래 연결
                nodes.append([i, i-w, 1]) 
            if -1 < i%w-1 and MAP[i-1] != -1: # 왼쪽 연결
                nodes.append([i, i-1, 1])
            
    nodes.sort(key=lambda x : x[0])
    
    for j in range(w*h): 
        hit = 0
        for i in nodes:
            a, b, c = i
            if MAP[a] == INF or a == w*h-1:
                continue
            if MAP[a] + c < MAP[b]:
                MAP[b] = MAP[a] + c
                if b == w*h-1:
                    break
                hit = 1    
    if hit == 1:
        print("Never")
    else:
        print("Impossible" if MAP[-1] == INF else MAP[-1])