x = int(input())

for i in range(x+1):
    if i > 0:
        if x % i == 0:
            print(i, end=" ")