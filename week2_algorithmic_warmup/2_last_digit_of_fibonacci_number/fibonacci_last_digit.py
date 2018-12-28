# Uses python3


def get_fibonacci_last_digit_naive(n):
    fibb = [0,1]
    for x in range(2,n+1):
        fibb.append((fibb[x-1]+fibb[x-2])%10)
        
    return fibb[n]

x = int(input())
print(get_fibonacci_last_digit_naive(x))
