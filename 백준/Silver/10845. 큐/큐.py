from collections import deque
import sys
input = sys.stdin.readline
n = int(input())

Q = deque()

for i in range(n):
    command = input()
    if " " in command:
        a, b = command.split()
        Q.append(b)
    else:
        a = command.rstrip()
        if a == "front":
            if len(Q):
                print(Q[0])
            else:
                print(-1)
        elif a == "back":
            if len(Q):
                print(Q[-1])
            else:
                print(-1) 
        elif a == "empty":
            if len(Q):
                print(0)
            else:
                print(1) 
        elif a == "pop":
            if len(Q):
                print(Q.popleft())
            else:
                print(-1) 
        elif a == 'size':
            print(len(Q))
            
    