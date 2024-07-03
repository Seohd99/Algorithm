al = ["c=","c-","dz=","d-","lj","nj","s=","z="]
inp = input()

for i in al:
    inp = inp.replace(i,"a")
print(len(inp))
