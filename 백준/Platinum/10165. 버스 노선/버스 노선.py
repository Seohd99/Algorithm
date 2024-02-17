import sys
n = int(input())
m = int(input())
result = [i for i in range(m+1)]
lst = []
for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    if a > b:
        b += n
        lst.append((a,b,i+1))
    else:
        lst.append((a,b,i+1))
        lst.append((a+n,b+n,i+1))
        
lst.sort(key= lambda x : (x[0],-x[1]))
x = 0
for i in lst:
    if x >= i[1]:
        result[i[2]] = 0
    else:
        x = i[1]

for i in result:
    if i != 0:
        print(i,end=" ")
