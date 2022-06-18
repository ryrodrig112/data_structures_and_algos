import time
import random


def max_pairwise_product(numbers):
    max_one = 0
    max_two = 0
    n = len(numbers)
    for idx in range(0, n):
        if numbers[idx] > max_two:# check to see if number at idx > than max two
            if numbers[idx] > max_one: # if it is, see if it is greater than max one
                # if it is greater than both, set max one to numbers[idx] and max_two to max_one
                max_two, max_one = max_one, numbers[idx]
            else:
                # otherwise set max_two to num[idx]
                max_two = numbers[idx]
    max_product = max_one * max_two
    return max_product


def max_pairwise_product_naive(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])
    return max_product


def test_solution():
    try:
        # Test Provided Solutions
        assert max_pairwise_product([1, 2, 3]) == 6, "Fails provided test 1"
        assert max_pairwise_product([7, 5, 14, 2, 8, 8, 10, 1, 2, 3, ]) == 140, "Fails provided test 2"

        # Test Large Numbers
        assert max_pairwise_product([1000000, 1000000]) == 1000000000000, "Issue with large numbers"

        # Test Time with large array
        t0 = time.process_time()
        nums = [i for i in range(2 * 10 ** 5)]
        max_pairwise_product(nums)
        t1 = time.process_time()
        assert t1 - t0 < 1, "Slow with large data"

        # Create random test
        num_tests = 100000
        test = 0
        while test < num_tests:  # continue testing until num_tests exceeded

            len_options = [i for i in range(2, 11)]
            max_value = 100
            list_len = random.choice(len_options)  # pick a random length between 1-10
            nums = []
            for num in range(list_len):  # generate n random integers between 1 and max
                nums.append(random.choice([i for i in range(0, max_value)]))
            assert max_pairwise_product(nums) == max_pairwise_product_naive(nums), "Values not equal for {}".format(nums)
            test += 1
    except AssertionError as msg:
        print(msg)


if __name__ == '__main__':
    # test_solution()
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
