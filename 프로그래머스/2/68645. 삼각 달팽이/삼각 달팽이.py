def solution(n):
    
    def down(idx, inp, n, f):
        for i in range(n):
            lst[idx] = inp 
            inp += 1
            if i != n - 1:
                idx += f
                f += 1
        return idx, f, inp
    
    def right(idx, inp, n):
        for i in range(n): 
            lst[idx] = inp
            inp += 1
            if i != n - 1:
                idx += 1
        return idx, inp
    
    def up(idx, inp, n, f):
        print(idx, inp, n)
        for i in range(n): 
            lst[idx] = inp 
            inp += 1
            if i != n - 1:
                idx -= f
                f -= 1
            
        return idx, f, inp 
    x = 0
    for i in range(1, n + 1):
        x += i
    
    lst = [0] * x
    inp = 1
    idx = 0
    f = 0
    while(n>0):
        idx, f, inp = down(idx+f,inp,n,f+1)
        n -= 1
        if n == 0:
            break
        idx, inp = right(idx+1,inp,n)
        n -= 1
        if n == 0:
            break
        idx, f, inp = up(idx-f,inp,n,f-1)
        n -= 1
        if n == 0:
            break
        
        
            
    return lst