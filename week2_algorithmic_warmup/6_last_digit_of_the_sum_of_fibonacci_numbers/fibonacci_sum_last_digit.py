# Uses python3
import sys
import time
import random

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    _sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10

def get_fibonacci_cycle(m):
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

    return fib_cycle

def fibonacci_sum_algo(n):
    #  0. Last digit is mod 10
    #  1. Get the mod 10 pattern and cycle
    n +=1
    pattern = get_fibonacci_cycle(10)
    pattern_size = len(pattern)
    pattern_sum = sum(pattern)
    #  2. Floor division for number of times to sum cycle
    multiple = n // pattern_size
    #  3. Mod division for sum of numbers to get
    remainder = n % pattern_size
    answer = ((multiple*pattern_sum) + sum(pattern[:remainder])) % 10
    return answer

def test_algo():
    assert fibonacci_sum_algo(3) == 4, "Given test case"
    assert fibonacci_sum_algo(100) == 5, "Given test case"

    t0 = time.process_time()
    fibonacci_sum_algo(10**14)
    t1 = time.process_time()
    assert t1-t0 < 1, "Slow for large data: Time elapsed {}".format(t1-t0)

    num_tests = 1000
    max_n = 1000
    for i in range(num_tests):
        n = random.choice([i for i in range(max_n)])
        assert fibonacci_sum_algo(n) == fibonacci_sum_naive(n), "Fails for n value: {}".format(n)


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_algo(n))
