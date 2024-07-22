n, k = map(int,input().split())
arr =[0,1]
for i in range(2,n+1):
    arr.append(arr[i-1]*i)
if arr[k]*arr[n-k] == 0:
    print(1)
else:
    print(arr[n]//(arr[k]*arr[n-k])%10007)

