def solution(price, money, count):
    All = 0
    for i in range(1,count+1):
        All += price * i
    
    answer = 0 if money - All >= 0 else All - money
    

    return answer