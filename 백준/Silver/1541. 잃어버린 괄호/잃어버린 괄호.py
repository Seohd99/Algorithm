st = input()
dab = 0
def intsum(s):
    isum = 0
    for i in s.split('+'):
        isum += int(i)
    return(isum) 

lst = st.split('-')
dab = intsum(lst[0])

for i in range(1,len(lst)):
    dab -= intsum(lst[i])

print(dab)