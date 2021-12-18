
a = 1
b = 1
sum = 0

for i in range(2, 4000):
    a, b = b, b + a
    if b % 2 == 0:
        sum += b
        print(b, end=' ')
    if b > 4000000:
        break

print(f"Summa: {sum}")



