# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(max(a,b),a*b + 1,min(a,b)):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

x = input().split()
a = int(x[0])
b = int(x[1])
print(lcm_naive(a, b))
