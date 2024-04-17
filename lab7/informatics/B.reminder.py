a = int(input())
b = int(input())
c = int(input())
d = int(input())

result = ""
for i in range(a, b, +1):
    if i % d == c:
        print(i, end=" ")
    else:
        continue
