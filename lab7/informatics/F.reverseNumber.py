x = int(input())
res = 0
m = 1
for i in str(x):
    res += int(i) * m
    m *= 10

print(res)