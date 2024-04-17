def solution(lines):
    answer = 0
    
    cnt = [0] * 201
    
    for i in lines:
        for j in range(i[0],i[1]):
            cnt[j+100] += 1
            print(cnt[j+100])
            if cnt[j+100] == 2:
                answer += 1 
    return answer