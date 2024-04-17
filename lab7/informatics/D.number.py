x = str(input())
d = str(input())
summ = 0
for i in range(len(x)):
    if x[i] == d:
        summ += 1

print(summ)