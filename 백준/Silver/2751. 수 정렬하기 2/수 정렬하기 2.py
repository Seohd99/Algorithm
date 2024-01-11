def merge(a,b,c,d,):
    dab = []
    st = a
    while(a<=b and c<=d):
        if lst[a] < lst[c]:
            dab.append(lst[a])
            a += 1
        else:
            dab.append(lst[c])
            c += 1
    
    if a <= d:
        for i in range(a,b+1):
            dab.append(lst[i])
    else:
        for i in range(c,d+1):
            dab.append(lst[i])
    for i in dab:
        lst[st] = i
        st += 1

def mergesort(s,e):
    if s == e:
        return

    mergesort(s,(s+e)//2)
    mergesort((s+e)//2+1,e)

    merge(s,(s+e)//2,(s+e)//2+1,e)

n = int(input())
lst = []

for i in range(n):
    lst.append(int(input()))

mergesort(0,n-1)
for i in lst:
    print(i)

