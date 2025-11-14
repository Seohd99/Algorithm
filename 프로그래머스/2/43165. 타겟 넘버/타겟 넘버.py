def dfs(i,x,numbers, target):
    if len(numbers) == i:
        return 1 if x == target else 0
    return dfs(i+1, x+numbers[i], numbers, target) + dfs(i+1, x-numbers[i], numbers, target)

from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    
    q.append([0,0])
    
    while q:
        x,i = q.popleft()
        if i == len(numbers):
            if target == x:
                answer += 1
            continue
        q.append([x + numbers[i],i + 1])
        q.append([x - numbers[i],i + 1])
    
    return answer