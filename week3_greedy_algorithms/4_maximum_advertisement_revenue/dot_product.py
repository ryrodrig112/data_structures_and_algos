#Uses python3

import sys

def max_dot_product(a, b):
    # Multiply the highest numbers in each list by eachother
    if len(a) == 1:
        # print("{} * {}".format(a[0], b[0]))
        return a[0] * b[0]
    else:
        max_a = max(a)
        max_b = max(b)
        a.remove(max_a)
        b.remove(max_b)
        # print("{} * {}".format(max_a, max_b))
        return (max_a * max_b) + max_dot_product(a, b)

def test_algo():
    assert max_dot_product([23], [39]) == 897, "Expected 897, returned {}".format(max_dot_product([23], [39]))
    assert max_dot_product([1, 3, -5], [-2, 4, 1]) == 23, "Expected 23, returned {}"\
        .format(max_dot_product([1, 3, -5], [-2, 4, 1]))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    # test_algo()
