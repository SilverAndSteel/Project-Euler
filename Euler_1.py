# Euler 1

sum_num = 0

for i in range(1, 1001):
    if i % 3 == 0 or i % 5 == 0:
        sum_num += i

print(sum_num)