def solution(num):
    answer = 0
    for i in range(500):
        if num == 1:
            return answer
        num = num * 3 + 1 if num % 2 == 1 else num // 2
        answer += 1
    if num == 1:
        return answer
    return -1