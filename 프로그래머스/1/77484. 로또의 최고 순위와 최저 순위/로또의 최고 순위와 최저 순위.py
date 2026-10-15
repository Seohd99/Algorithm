def solution(lottos, win_nums):
    answer = 7
    for i in win_nums:
        if i in lottos:
            answer -= 1
    return [ x if x != 7 else 6 for x in [answer - lottos.count(0) , answer]]