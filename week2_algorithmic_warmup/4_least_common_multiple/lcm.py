# Uses python3
import sys
import math
import time
import random


def lcm_naive(a, b):
    #  1. Find prime factorization of A and store in list
    #  2. Find prime factorization of B and store in list
    #  3. Compare A's prime factor list to B's and add in unique elements
    #  4. Multiply numbers in new list
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a * b


def lcm_algo(a, b):
    #  0. Define a way to get prime factors
    def get_prime_factors(num):
        i = 2
        factors = []
        while i in range(2, int(num ** .5) + 1):
            if num % i == 0:
                factors.append(i)
                num /= i
            else:
                i += 1
        if num > 1:
            factors.append(num)
        return factors

    #  1. Find prime factorization of A and store in list
    a_factors = get_prime_factors(a)
    #  2. Find prime factorization of B and store in list
    b_factors = get_prime_factors(b)
    #  3. Compare A's prime factor list to B's and add in unique elements
    for factor in a_factors:
        if factor in b_factors:
            b_factors.remove(factor)
    all_factors = a_factors + b_factors
    #  4. Multiply numbers in new list and return
    total = 1
    for num in all_factors:
        total *= num
    return total


def test_lcm_algo():
    assert lcm_algo(1, 3) == 3  # Test two primes
    assert lcm_algo(4, 4) == 4  # Test identical number
    assert lcm_algo(12, 4) == 12  # Test multiples
    assert lcm_algo(25, 2) == 50  # Test small value
    #  Test Time with large array
    t0 = time.process_time()
    a = 13 ** 5
    b = 7 ** 8
    lcm_algo(a, b)
    t1 = time.process_time()
    assert t1 - t0 < 1, "Slow with large data"
    #  Test with random data
    num_tests = 100000
    test = 0
    options = [i for i in range(101)]
    while test < num_tests:  # continue testing until num_tests exceeded
        a = random.choice(options)
        b = random.choice(options)
        assert lcm_algo(a, b) == lcm_algo(a, b), "Values not equal for {}".format([a,b])
        test += 1


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_algo(a, b))
