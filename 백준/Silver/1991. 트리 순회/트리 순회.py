n = int(input())


lst = [0 for i in range(26)]

def tree1(n):
    if n == -19:
        return
    a, b = lst[n].split()
    print(chr(n+65),end="")
    tree1(ord(a)-65)
    tree1(ord(b)-65)
def tree2(n):
    if n == -19:
        
        return
    a, b = lst[n].split()
    tree2(ord(a)-65)
    print(chr(n+65),end="")
    tree2(ord(b)-65)
    
def tree3(n):
    if n == -19:
        return
    a, b = lst[n].split()
    
    tree3(ord(a)-65)
    tree3(ord(b)-65)
    print(chr(n+65),end="")


for i in range(n):
    st = input()
    f = st[0]
    lst[ord(f)-65] = st[2:]
tree1(0)
print()
tree2(0)
print()
tree3(0)
print()