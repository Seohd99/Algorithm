def solution(s):
    sl = s.split()
    
    answer = ''
    for word in sl:
        for i, c  in enumerate(word):
            if i % 2 == 0:
                answer += c.upper()
            else:
                answer += c.lower()
        answer += ' '

    return answer.rstrip()

