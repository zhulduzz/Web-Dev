
N = int(input())

current_number = 1

while current_number**2 <= N:
    print(current_number**2, end=" ")
    current_number += 1

print()
