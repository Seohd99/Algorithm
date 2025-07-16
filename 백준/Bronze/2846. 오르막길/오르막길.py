n = int(input())
Input_List = list(map(int,input().split()))
List = []
ans = 0
now = 0
for i in Input_List:
    if now < i:
        List.append(i)
        now = i
    else:
        ans = max(ans, List[-1] - List[0])
        now = i
        List = [i]
if(List):
    ans = max(ans, List[-1] - List[0])
print(ans)