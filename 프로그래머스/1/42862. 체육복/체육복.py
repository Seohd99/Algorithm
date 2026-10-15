def solution(n, lost, reserve):
    t = lost
    lost = [i for i in t if i not in reserve]
    reserve = [i for i in reserve if i not in t]
    lost.sort()
    answer = n
    
    for i in lost:
        answer -= 1
        for j in [-1, 1]:
            if (i + j) in reserve:
                reserve.pop(reserve.index(i + j))
                answer += 1
                break
    return answer
