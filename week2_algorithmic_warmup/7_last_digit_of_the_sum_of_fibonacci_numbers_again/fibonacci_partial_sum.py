# Uses python3
import sys
import time
import random


def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

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
    pattern = get_fibonacci_cycle(10)
    pattern_size = len(pattern)
    pattern_sum = sum(pattern)
    #  2. Floor division for number of times to sum cycle
    multiple = n // pattern_size
    #  3. Mod division for sum of numbers to get
    remainder = n % pattern_size
    answer = ((multiple*pattern_sum) + sum(pattern[:remainder]))
    return answer


def fibonacci_partial_sum_algo(m, n):
    m_sum = fibonacci_sum_algo(m)
    n_sum = fibonacci_sum_algo(n+1)
    return (n_sum - m_sum) % 10


def test_algo():
    assert fibonacci_partial_sum_algo(10, 10) == 5, "Given example"
    assert fibonacci_partial_sum_algo(3, 7) == 1, "Given example"

    t0 = time.process_time()
    fibonacci_partial_sum_algo(10**13,10**14)
    t1 = time.process_time()
    assert  t1-t0 < 1, "Slow with large values, time elapsed: {}".format(t1-t0)

    num_tests = 1000
    max_value = 100
    for i in range(num_tests):
        val1 = random.choice([i for i in range(max_value)])
        val2 = random.choice([i for i in range(max_value)])
        m = min(val1, val2)
        n = max(val1, val2)
        print(i, m, n)
        assert fibonacci_partial_sum_algo(m, n) == fibonacci_partial_sum_naive(m, n), "Fails for: m = {}, n = {}".format(m, n)



if __name__ == '__main__':
    # input = sys.stdin.read();
    # from_, to = map(int, input.split())
    test_algo()
