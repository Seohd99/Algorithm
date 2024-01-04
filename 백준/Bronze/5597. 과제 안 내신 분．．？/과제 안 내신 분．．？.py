lst = [0 for i in range(31)]

for i in range(28):
	x = int(input())
	lst[x] = 1
for i in range(1,31):
	if lst[i] == 0:
		print(i)