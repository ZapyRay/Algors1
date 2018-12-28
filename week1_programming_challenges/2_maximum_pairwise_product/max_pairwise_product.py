# python3


def max_pairwise_product(numbers):
    max_product = numbers[0] * numbers[1]
    product = 0
    n = len(numbers)
    for x in range(1,n - 1,1):
        product = numbers[x] * numbers[x+1]
        if ( product > max_product):
            max_product = product

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
