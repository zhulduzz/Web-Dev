n = int(input())
zeros = 0

for i in range(n):
    numbers = int(input())
    if numbers == 0:
        zeros += 1

print(zeros)