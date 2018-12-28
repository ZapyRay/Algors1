# Uses python3


def gcd_naive(a, b):
    
    smaller = min(a, b)
    for d in range( smaller , 0 , -smaller):
        if a % d == 0 and b % d == 0:
            return d




x = input().split()
a = int(x[0])
b = int(x[1])
print(gcd_naive(a, b))
