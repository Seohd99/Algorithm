n = int(input())

l = [[0,0] for i in range(n+1)]
l[1] = [1,2]
for i in range(2,n+1):
    for j in range(2):
        if j == 0:
            l[i][j] = sum(l[i-1]) % 9901
        else:
            l[i][j] = l[i-1][0] * 2 + l[i-1][1] % 9901
    
print(sum(l[-1]) % 9901)  