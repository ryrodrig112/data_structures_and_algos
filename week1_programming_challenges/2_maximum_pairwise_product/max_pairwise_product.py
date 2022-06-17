def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def test_solution():
    # Test Provided Solutions
    assert max_pairwise_product([1, 2, 3]) == 3
    assert max_pairwise_product([7, 5, 14, 2, 8, 8, 10, 1, 2, 3,]) == 140
    # Test Large Numbers
    assert max_pairwise_product([1000000,1000000]) == 1000000000000
    # Test Time with large array
    ...
    # Create random test
    ...


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
