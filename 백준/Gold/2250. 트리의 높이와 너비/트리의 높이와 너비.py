def IN(l,i):
    global d
    if d < l:
        d = l
    posi[l].append(i)




def tree(n,l): # 중
    global IDX
    if n == -1:
        
        return
    a = lst[n][0]
    b = lst[n][1]

    tree(a,l+1)
    IN(l,IDX)
    IDX += 1
    tree(b,l+1)



n = int(input())
ck = [0 for i in range(n+1)]
ck[0] = 1
posi = [[]for j in range(n+1)]
lst = [[]for j in range(n+1)]

for i in range(n):
    a,b,c = map(int,input().split())
    lst[a].append(b)
    lst[a].append(c)
    if b != -1:
        ck[b] = 1
    if c != -1:        
        ck[c] = 1

d = 0
IDX = 1 
for i in range(1,n+1):
    if ck[i] == 0:
        r = i
        break
tree(r,1)
MAX = 0

for i in range(1,d+1):
    leng = max(posi[i]) - min(posi[i]) + 1
    if MAX < leng:
        MAX = leng
        level = i

print(level, MAX)