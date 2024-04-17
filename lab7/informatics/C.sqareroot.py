import math

a = int(input())
b = int(input())

for i in range(a, b, +1):
    if math.pow(i, 0.5) == round(math.pow(i, 0.5)):
        print(i, end=" ")

