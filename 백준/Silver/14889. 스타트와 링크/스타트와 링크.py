import sys
input = sys.stdin.readline

n = int(input())
MAP = []
startTeam = []
MIN = 10000000000
def countStat():    
    global MIN
    SUM_link = 0
    SUM_start = 0
    linkTeam = []
    for i in range(n):
        if i in startTeam:
            continue
        else:
            linkTeam.append(i)
    for i in range(n//2):
        for j in range(n//2):
            SUM_start += MAP[startTeam[i]][startTeam[j]]
            SUM_start += MAP[startTeam[j]][startTeam[i]]
            SUM_link += MAP[linkTeam[i]][linkTeam[j]]
            SUM_link += MAP[linkTeam[j]][linkTeam[i]]
    startTeam.pop()
    MIN = min(abs(SUM_start - SUM_link) // 2,MIN) 
    return

def pick(p):
    if MIN == 0:
        return
    startTeam.append(p)
    if len(startTeam) == n//2:
        countStat()
        return
    for i in range(p+1,n):
        pick(i)
    startTeam.pop()
    return
for i in range(n):
    MAP.append(list(map(int,input().split())))
    

for i in range(n):
    pick(i)
        
print(MIN)