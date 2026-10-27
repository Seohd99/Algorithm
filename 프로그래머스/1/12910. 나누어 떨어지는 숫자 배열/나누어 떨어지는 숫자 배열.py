def solution(arr, divisor):
    arr.sort()
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i) 
    return answer if answer else [-1]