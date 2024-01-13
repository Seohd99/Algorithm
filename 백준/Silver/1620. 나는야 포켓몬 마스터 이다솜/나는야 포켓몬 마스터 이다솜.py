import sys
n,m = map(int,input().split())

def key(s):
    num = 0
    for i in range(len(s)):
        num += ((ord(s[i])-64)*53**i)
    return num % 500009

hs = [ [] for i in range(500009)]
name = [""]


for i in range(n):
    name.append(sys.stdin.readline().rstrip())
for i in range(1,n+1):
    hs[key(name[i])].append(i)

for i in range(m):
    st = sys.stdin.readline().rstrip()
    if st[0] <= "9" and st[0] >= "0":
        print(name[int(st)])
    else:
        k = key(st)
        for j in hs[k]:
            if st == name[j]:
                print(j)
                break
