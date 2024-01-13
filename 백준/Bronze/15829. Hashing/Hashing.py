L = int(input())
ST = input()
H = 0
for i in range(L):
    H += ((ord(ST[i])-96)*31**i) 

print(H% 1234567891)