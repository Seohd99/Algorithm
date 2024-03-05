t = int(input())  

fn = [8,8,1,7,4,2,6,8] 
for tc in range(t):
    MIN = []
    n =int(input())
    m = n
    if n == 10:
        MIN.append("2")
        n -= 5
    while(n > 7): 
        if n % 6 == 0:
            MIN.append("8")
            n -= 7
            continue
        leng8 = n // 7 if n % 7 == 0 else n // 7 + 1
        leng0 = n // 6 + 1

        if leng8 != leng0:
            MIN.append("8")
            n -= 7
        else:
            if fn[n%7] < fn[n%6]:
                MIN.append("8")
                n -= 7
            else:
                MIN.append("0")
                n -= 6
    MIN.append(str(fn[n]))
    MIN.sort()
    if MIN[0] == "0":
        for i in range(len(MIN)):
            if MIN[i] != "0":
                MIN[0] = MIN[i]
                MIN[i] = "0"
                break
    MAX = []
    while(m!=0):
        if m % 2 == 0:
            MAX.append("1")
            m -= 2
        else:
            MAX.append("7")
            m -= 3
    MAX.sort(reverse=True)

    print(''.join(MIN),''.join(MAX))

 