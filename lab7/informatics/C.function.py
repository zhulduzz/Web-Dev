def xor(a, b):
    return int((a or b) and not (a and b))


x = int(input())
y = int(input())


print(xor(x, y))
