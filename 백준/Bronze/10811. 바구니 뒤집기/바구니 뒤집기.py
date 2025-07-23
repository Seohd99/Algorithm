n, m = map(int,input().split())
lst = [i for i in range(1, n+1)]
def action(s, e):
    ran = (e - s) // 2 + (e - s) % 2
    for i in range(ran): 
        lst[s + i], lst[e-i] = lst[e-i], lst[s + i]
for i in range(m):
    x, y = map(int,input().split())
    x -= 1
    y -= 1
    action(x, y)
print(*lst)