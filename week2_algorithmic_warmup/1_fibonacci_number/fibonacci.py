# Uses python3
def calc_fib(n):
    fibb = [0,1]
    for x in range(2,n+1):
        fibb.append(fibb[x-1]+fibb[x-2])
        
    return fibb[n]

n = int(input())
print(calc_fib(n))
