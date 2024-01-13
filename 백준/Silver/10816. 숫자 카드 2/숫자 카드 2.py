import sys

alst = [[]for i in range(170873)]
blst = [[]for i in range(170873)]

def push(x):
    if x in alst[(x+ 1000000) % 170873]:
        y = alst[(x+ 1000000) % 170873].index(x)
        blst[(x+ 1000000) % 170873][y] += 1
    else:
        alst[(x+ 1000000) % 170873].append(x)
        blst[(x+ 1000000) % 170873].append(1)

def find(x):
    if x in alst[(x+ 1000000) % 170873]:
        y = alst[(x+ 1000000) % 170873].index(x)
        return blst[(x+ 1000000) % 170873][y]
    else:
        return 0

cnt = 0 
n = int(input())
lst1 = list(map(int,input().split()))
for i in lst1:
    push(i)

m = int(input())

lst2 = list(map(int,input().split()))
for i in lst2:
    print(find(i),end=" ")