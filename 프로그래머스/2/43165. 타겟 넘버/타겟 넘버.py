def dfs(i,x,numbers, target):
    if len(numbers) == i:
        return 1 if x == target else 0
    return dfs(i+1, x+numbers[i], numbers, target) + dfs(i+1, x-numbers[i], numbers, target)

def solution(numbers, target):
    return dfs(0,0,numbers,target)