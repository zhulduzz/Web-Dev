
N = int(input())

count_ones = 0


while N > 0:
    if N & 1 == 1:
        count_ones += 1
    N >>= 1


if count_ones == 1:
    print("YES")
else:
    print("NO")
