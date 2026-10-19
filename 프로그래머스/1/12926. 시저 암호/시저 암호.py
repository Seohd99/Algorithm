def solution(s, n):    
    answer = []
    for c in s:
        if c.isalpha():
            t = 97 if c.islower() else 65
            c = chr(t + ((ord(c) - t + n) % 26))
        answer.append(c)
    return ''.join(answer)