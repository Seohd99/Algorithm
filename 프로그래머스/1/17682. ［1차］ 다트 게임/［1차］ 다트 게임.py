def solution(dartResult):
    
    stack = []
    temp = ''
    dic = {'S': 1, 'D': 2, 'T': 3}
    
    for c in dartResult:
        if c in dic:
            stack.append(int(temp) ** dic[c])
        elif c == '*':
            stack[-1] *= 2
            if len(stack) >= 2:
                stack[-2] *= 2
        elif c == '#':
            stack[-1] *= -1
        else:
            temp += c
            continue
        temp = ''
    
    return sum(stack)