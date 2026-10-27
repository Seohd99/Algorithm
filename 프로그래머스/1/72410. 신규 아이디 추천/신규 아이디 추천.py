import re
def solution(new_id):
    temp = new_id.lower()
    new_id = ''
    answer = ''
    
    for s in temp:
        if s.isalpha() or s in ['_', '-', '.'] or s.isdigit():
            answer += s
    answer = re.sub(r'\.{2,}', '.', answer)
    if len(answer) and answer[-1] == '.': answer = answer[:-1]
    if len(answer) and answer[0] == '.': answer = answer[1:]
    if len(answer) == 0: answer ='a'
    if len(answer) >= 16: answer = answer[:15]
    if len(answer) and answer[-1] == '.': answer = answer[:-1]    
    while len(answer) <= 2:
        answer+= answer[-1]

        
    return answer