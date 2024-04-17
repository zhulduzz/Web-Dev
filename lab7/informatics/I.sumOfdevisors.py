x = int(input())

summa = 0

for i in range(x + 1):
    if i > 0:
        if x % i == 0:
            summa += 1

print(summa)
