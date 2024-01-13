L = int(input())
ST = input()
H = 0
for i in range(L):
    H += ((ord(ST[i])-96)*31**i) % 1234567891

print(H)