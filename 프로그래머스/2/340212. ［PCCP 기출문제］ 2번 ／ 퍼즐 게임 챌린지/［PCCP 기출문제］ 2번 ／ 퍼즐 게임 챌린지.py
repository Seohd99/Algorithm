def solution(diffs, times, limit):
    sec = 0
    l = 0
    r = max(diffs)+100
    level = 1
    
    while r >= l:
        sec = 0
        level = (l+r)//2
        prev = 0
        for i in range(len(diffs)):
            if limit < sec:
                break
            fail = 0 if level >= diffs[i] else diffs[i] - level
            sec += fail * (prev+times[i])
            sec += times[i]
            prev = times[i]  
        if limit >=sec:
            r = level -1
        else:
            l = level + 1 
    
    return l if l > 0 else 1