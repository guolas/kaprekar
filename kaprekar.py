#!/bin/python3

"""
Get the range to search for modified Kaprekar numbers
"""
a = int(input().strip())
b = int(input().strip())

output = "INVALID RANGE"
for number in range(a, b + 1):
    square = str(number ** 2)
    L = len(square) // 2
    if L == 0:
        left = 0
        right = int(square)
    elif L == 1:
        left = int(square[0])
        right = int(square[1])
    else:
        left = int(square[:L])
        right = int(square[L:])
    if left + right == number:
        if output == "INVALID RANGE":
            output = str(number)
        else:
            output = " ".join([output, str(number)])

print(output)
