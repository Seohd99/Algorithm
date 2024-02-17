n = int(input())

x_list = []
y_list = []
box = []
for i in range(n):
    x , y , xx , yy = map(float,input().split())
    xx += x
    yy += y
    x_list.append(x)
    x_list.append(xx)
    y_list.append(y)
    y_list.append(yy)
    box.append((x,y,xx,yy))

x_list.sort()
y_list.sort()
area = 0
for i in range(n*2-1):
    for j in range(n*2-1):
        x = x_list[i]
        xx = x_list[i+1]
        y = y_list[j]
        yy = y_list[j+1]
        if xx == x or yy == y:
            continue
        for b in box:
            if b[0] <= x and b[2] >= xx and b[1] <= y and b[3] >= yy:
                area += ((xx-x)*(yy-y))
                break
 
print(int(area) if area % 1 == 0 else "%.2f"%area)
    
    

