x = int(input())

for i in range(x):
    if i > 0 and i > 1:
        if x % i == 0:
            print(i, end=" ")
            break
