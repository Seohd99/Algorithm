n = int(input())

def rsp(A, B):
    ran = min(A[0], B[0])
    listA = sorted(A[1:], reverse = True)
    listB = sorted(B[1:], reverse = True)
    for i in range(ran):
        if listA[i] > listB[i]:
            return "A"
        elif listA[i] < listB[i]:
            return "B"
    if len(listA) > len(listB):
        return "A"
    elif len(listA) < len(listB):
            return "B"
    else:
        return "D"
        
for i in range(n):
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    
    print(rsp(A,B))

