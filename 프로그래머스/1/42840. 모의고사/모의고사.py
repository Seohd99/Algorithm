def solution(answers):
    supo = [[1,2,3,4,5],
            [2,1,2,3,2,4,2,5],
            [3,3,1,1,2,2,4,4,5,5]]
    score = [0, 0, 0]
    
    for i, x in enumerate(answers):
        for j, s in enumerate(supo):
            if s[i % len(s)] == x:
                score[j] += 1
    MAX = max(score)
    
    return [i + 1 for i, x in enumerate(score) if x == MAX]