myName = list(input())
herName = list(input())
lst = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1] 

nameList = []

for i in range(len(myName)):
    nameList.append(lst[ord(myName[i])-65])
    nameList.append(lst[ord(herName[i])-65])

while(len(nameList) != 2):
    copyList = nameList[:]
    nameList = []
    for i in range(len(copyList)-1):
        nameList.append((copyList[i] + copyList[i+1])%10)
ans = str(nameList[0]) + str(nameList[1])

print(ans) 