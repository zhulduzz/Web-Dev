binaryNumber = str(input())

decimalNumber = 0

for i in range(len(binaryNumber)):
    digit = int(binaryNumber[i])
    decimalNumber += digit * 2 ** (len(binaryNumber) - i - 1)

print(decimalNumber)