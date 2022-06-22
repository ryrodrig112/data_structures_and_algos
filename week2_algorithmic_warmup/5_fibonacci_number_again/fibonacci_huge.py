# Uses python3
import sys
import time
import random


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_huge_algo(n, m):
    def calc_fib_list(i):
        fib_list = [0, 1]
        for k in range(2, i + 1):
            fib_list.append(fib_list[k - 1] + fib_list[k - 2])
        return fib_list

    def calc_period(pattern):
        period_len = 1
        searching = True
        cycle = None
        while searching:
            first_test = pattern[0:period_len]
            second_test = pattern[period_len:2 * period_len]
            if first_test == second_test:

                testing = True
                iterations = 2
                while testing == True & iterations <= 3:
                    if pattern[(iterations + 1) * period_len:(iterations + 2) * period_len] != \
                            pattern[iterations * period_len:(iterations + 1) * period_len]:
                        testing = False
                        period_len += 1
                    else:
                        iterations += 1
                searching = False
                cycle = pattern[0:period_len]
            else:
                period_len += 1
        return cycle, period_len

    #  1. Determine Pattern and Period for f(n) % m
    fib_list = calc_fib_list(10000)
    pattern = [i % m for i in fib_list]
    fib_cycle, fib_period_len = calc_period(pattern)

    #  2. Calculate m % period = Remainder
    index = n % fib_period_len
    #  3. Pattern[Remainder]
    return fib_cycle[index]


def test_get_fibonacci_huge_algo():
    assert get_fibonacci_huge_algo(239, 1000) == 161  # Test for given values
    assert get_fibonacci_huge_algo(2816213588, 239) == 151  # Test for given values
    print("Successful for given values")
    #  Test Time with large numbers
    t0 = time.process_time()
    a = 10 ** 13
    b = 1000
    get_fibonacci_huge_algo(a, b)
    t1 = time.process_time()
    assert t1 - t0 < 1, "Slow with large data: Time elapsed{}".format(t1 - t0)
    print("Succesful for large values")
    #  Test with random data
    num_tests = 1000
    test = 0
    options = [i for i in range(1, 101)]
    while test < num_tests:  # continue testing until num_tests exceeded
        a = random.choice(options)
        b = random.choice(options)
        print(test, a, b)
        assert get_fibonacci_huge_algo(a, b) == get_fibonacci_huge_naive(a, b), "Values not equal for {}".format([a, b])
        test += 1


if __name__ == '__main__':
    # input = sys.stdin.read();
    # n, m = map(int, input.split())
    print(get_fibonacci_huge_algo(58, 10))
    test_get_fibonacci_huge_algo()
