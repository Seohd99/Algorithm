st1 = input()

st2 = input()

lst = [['' for i in range(len(st2)+1)]for j in range(len(st1)+1)]
dp =  [['' for i in range(len(st2)+1)]for j in range(len(st1)+1)]
for i in range(1,len(st1)+1):
    for j in range(1, len(st2)+1):
        if st1[i-1] == st2[j-1]:
            lst[i][j] = lst[i-1][j-1] + st2[j-1]
        else:
            if len(lst[i-1][j]) < len(lst[i][j-1]):
                lst[i][j] = lst[i][j-1]
            else:
                lst[i][j] = lst[i-1][j] 
print(len(lst[-1][-1]))
if len(lst[-1][-1]):
    print(lst[-1][-1])
