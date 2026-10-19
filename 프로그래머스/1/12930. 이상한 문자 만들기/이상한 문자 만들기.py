def solution(s):
    i = 1
    answer = ''
    for c in s:
        if c == ' ':
            i = 0
        elif i % 2 == 1:
            c = c.upper()
        else:
            c = c.lower()
        i += 1
        answer += c
    return answer