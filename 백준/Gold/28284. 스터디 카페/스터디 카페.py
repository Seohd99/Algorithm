import sys
input = sys.stdin.readline
from itertools import accumulate

n, m = map(int,input().split())

seat_list = list(map(int,input().split()))
seat_list.sort()
prefix_sum = [0] + list(accumulate(seat_list)) 

s_days= []
e_days= []

for i in range(m):
    s, e = map(int,input().split())
    s_days.append(s)
    e_days.append(e+1)

s_days.sort()
e_days.sort()

customer = 0
today = 0
s_index = 0
e_index = 0
min_pay = 0
max_pay = 0

def add_pay(d, c):
    global min_pay
    global max_pay
    if c == 0:
        return
    min_pay += d * prefix_sum[c]
    max_pay += d * (prefix_sum[-1] - prefix_sum[-(c+1)])
    
while e_index != m:
    if s_index == m:
        end = e_days[e_index]
        add_pay(end - today, customer)
        today = end
        customer -= 1
        e_index += 1
        continue
    start = s_days[s_index]
    end = e_days[e_index]
    if min(start, end) == today:
        if start == today:
            s_index += 1
            customer += 1
        if end == today:
            e_index += 1
            customer -= 1
    elif end >= start:
        add_pay(start - today, customer)
        today = start
        customer += 1
        s_index += 1
    elif start > end:
        add_pay(end - today, customer)
        today = end
        customer -= 1
        e_index += 1
print(min_pay, max_pay)